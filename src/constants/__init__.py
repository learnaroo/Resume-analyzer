OUTPUT_DIR = "artifacts"
DATA_DIR = "data"

# PROMPT = f"""
# Your task is to analyze the resume provided and compare it with the job description to evaluate the candidate’s suitability for the role. Provide the analysis in a structured JSON format. Include the following components in your JSON response:

# Match Score: A number representing how well the resume matches the job description (0-100).

# Extracted Skills and Qualifications:

# Technical skills
# Soft skills
# Experience Levels and Domains:

# Categorized experiences with associated levels (beginner, intermediate, advanced)
# Relevant domains (e.g., industry or technical fields)
# Skill Relationships and Synonyms:

# Identified synonym pairs for skills
# Relevant related skills
# Improvement Suggestions:

# Specific areas for improvement
# Recommendations for enhancing skills and experiences
# Resume Formatting Tips:

# Insights for improving clarity, consistency, and visual appeal of the resume
# Provide the analysis based on the text within the following triple quotes:

# Resume:
# {resume}

# Job Description:
# {JD}

# Please format the output using the structure below:

# {
#   "match_score": 0,
#   "skills_and_qualifications": {
#     "technical_skills": [],
#     "soft_skills": []
#   },
#   "experience_levels_and_domains": {
#     "beginner": [],
#     "intermediate": [],
#     "advanced": []
#   },
#   "skill_relationships_and_synonyms": {
#     "synonym_pairs": [],
#     "related_skills": []
#   },
#   "improvement_suggestions": [],
#   "resume_formatting_tips": []
# }"""


import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_MODEL = os.getenv("OPENAI_API_MODEL")