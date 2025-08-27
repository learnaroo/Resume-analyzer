from src.components.text_extracter import TextExtracter
from src.components.evaluator import Evaluator
from src.exceptions import CustomException
from src.logger import logging
import sys


# Initialize components
try:
    logging.info("Initializing TextExtracter and Evaluator components...")
    text_extractor = TextExtracter()
    evaluator = Evaluator()
    logging.info("Components initialized successfully.")
except Exception as e:
    logging.error("Error occurred while initializing components.")
    raise CustomException(e, sys)


def initiate_resume_analyser_pipeline(file_path, jd):
    """
    Orchestrates the resume analysis pipeline:
    1. Extracts text from the resume file.
    2. Passes extracted text + JD to Evaluator.
    3. Returns structured evaluation result.
    """
    try:
        logging.info(f"Starting resume analysis pipeline for file: {file_path}")

        # Step 1: Extract text
        extracted_text = text_extractor.extract_text(file_path)
        logging.info(f"Text extraction successful. Extracted {len(extracted_text.text)} characters.")

        # Step 2: Evaluate resume against job description
        result = evaluator.initiate_llm_evaluator(extracted_text.text, jd)
        logging.info("Resume evaluation completed successfully.")

        return result

    except Exception as e:
        logging.error("Error occurred during resume analysis pipeline execution.")
        raise CustomException(e, sys)
