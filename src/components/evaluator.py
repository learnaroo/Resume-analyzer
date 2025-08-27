import sys
import json
from openai import OpenAI
from src.exceptions import CustomException
from src.logger import logging
from src.entity.config import ConfigEntity, EvaluatorConfig


class Evaluator:
    def __init__(self):
        try:
            logging.info("Initializing Evaluator configuration...")
            # Load configuration
            self.evaluator_config = EvaluatorConfig(config=ConfigEntity())
            # Initialize OpenAI client with API key
            self.client = OpenAI(api_key=self.evaluator_config.open_api_key)
            logging.info("Evaluator initialized successfully with provided configuration.")
        except Exception as e:
            logging.error("Error occurred during Evaluator initialization.")
            raise CustomException(e, sys)

    def llm_evaluator(self, question: str) -> str:
        """
        Sends the evaluation prompt to the LLM and returns the raw response text.
        """
        try:
            logging.info("Sending prompt to LLM for evaluation...")
            response = self.client.chat.completions.create(
                model=self.evaluator_config.open_api_model,
                messages=[
                    {"role": "system", "content": "You are an AI evaluator that outputs only valid JSON."},
                    {"role": "user", "content": question}
                ],
                temperature=0.9,
                max_tokens=512,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            logging.info("Received response from LLM successfully.")
            return response.choices[0].message.content
        except Exception as e:
            logging.error("Error occurred while communicating with LLM.")
            raise CustomException(e, sys)

    def prompt(self, resume: str, job_description: str) -> str:
        """
        Builds a structured prompt for resume-job description evaluation.
        """
        try:
            logging.info("Constructing evaluation prompt using resume and job description.")
            prompt = f"""
Your task is to analyze the resume provided and compare it with the job description to evaluate the candidate’s suitability for the role. 
Provide the analysis in a structured JSON format. Include the following components in your JSON response:

Match Score: A number representing how well the resume matches the job description (0-100).

Extracted Skills and Qualifications:
- Technical skills
- Soft skills

Experience Levels and Domains:
- Categorized experiences with associated levels (beginner, intermediate, advanced)
- Relevant domains (e.g., industry or technical fields)

Skill Relationships and Synonyms:
- Identified synonym pairs for skills
- Relevant related skills

Improvement Suggestions:
- Specific areas for improvement
- Recommendations for enhancing skills and experiences

Resume Formatting Tips:
- Insights for improving clarity, consistency, and visual appeal of the resume

Provide the analysis based on the text within the following triple quotes:

Resume:
\"\"\"{resume}\"\"\" 

Job Description:
\"\"\"{job_description}\"\"\" 

Please format the output using the structure below:

{{
    "match_score": 0,
    "skills_and_qualifications": {{
        "technical_skills": [],
        "soft_skills": []
    }},
    "experience_levels_and_domains": {{
        "beginner": [],
        "intermediate": [],
        "advanced": []
    }},
    "skill_relationships_and_synonyms": {{
        "synonym_pairs": [],
        "related_skills": []
    }},
    "improvement_suggestions": [],
    "resume_formatting_tips": []
}}
"""
            logging.info("Prompt constructed successfully.")
            return prompt
        except Exception as e:
            logging.error("Error occurred while constructing evaluation prompt.")
            raise CustomException(e, sys)

    def initiate_llm_evaluator(self, resume: str, job_description: str):
        """
        Orchestrates prompt building, sending it to LLM, and parsing the response.
        """
        try:
            logging.info("Starting resume evaluation process...")
            prompt = self.prompt(resume, job_description)

            raw_response = self.llm_evaluator(prompt)
            logging.debug(f"Raw LLM response: {raw_response[:200]}...")  # log only first 200 chars

            # Try parsing JSON output
            try:
                parsed_response = json.loads(raw_response)
                logging.info("LLM response parsed successfully into JSON.")
                return parsed_response
            except json.JSONDecodeError:
                logging.warning("⚠️ LLM response is not valid JSON. Returning raw text instead.")
                return raw_response

        except Exception as e:
            logging.error("Error occurred during evaluation pipeline.")
            raise CustomException(e, sys)
