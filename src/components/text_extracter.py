from src.exceptions import CustomException
from src.logger import logging
from src.entity.config import ConfigEntity, TextExtracterConfig
from src.entity.artifacts import TextExtractionArtifact
import sys
import os
import PyPDF2
import pdfplumber
from docx import Document


class TextExtracter:
    def __init__(self):
        try:
            logging.info("Initializing TextExtracter configuration...")
            self.text_extracter_config = TextExtracterConfig(config=ConfigEntity())
            logging.info("TextExtracter configuration initialized successfully.")
        except Exception as e:
            logging.error("Error occurred while initializing TextExtracter.")
            raise CustomException(e, sys)

    def extract_text(self, file_path) -> TextExtractionArtifact:
        """
        Extracts text from PDF or DOCX file and returns a TextExtractionArtifact.
        Supports PDF (pdfplumber → fallback PyPDF2) and DOCX.
        """
        try:
            logging.info(f"Starting text extraction for file: {file_path}")

            # Get file extension
            ext = os.path.splitext(file_path)[1].lower()
            text = ""

            # Handle PDF
            if ext == ".pdf":
                try:
                    logging.info("Attempting text extraction using pdfplumber...")
                    with pdfplumber.open(file_path) as pdf:
                        for page_num, page in enumerate(pdf.pages, start=1):
                            page_text = page.extract_text()
                            if page_text:
                                text += page_text + "\n"
                            logging.debug(f"Extracted text from page {page_num}")
                    logging.info("PDF text extraction with pdfplumber completed.")
                except Exception as e:
                    logging.warning("pdfplumber failed. Falling back to PyPDF2...")
                    try:
                        with open(file_path, "rb") as file:
                            reader = PyPDF2.PdfReader(file)
                            for page_num, page in enumerate(reader.pages, start=1):
                                page_text = page.extract_text()
                                if page_text:
                                    text += page_text + "\n"
                                logging.debug(f"Extracted text from page {page_num} using PyPDF2")
                        logging.info("PDF text extraction with PyPDF2 completed.")
                    except Exception as inner_e:
                        logging.error("Both pdfplumber and PyPDF2 failed for PDF extraction.")
                        raise CustomException(inner_e, sys)

            # Handle DOCX
            elif ext == ".docx":
                try:
                    logging.info("Attempting text extraction from DOCX...")
                    doc = Document(file_path)
                    text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
                    logging.info("DOCX text extraction completed successfully.")
                except Exception as e:
                    logging.error("Error occurred during DOCX text extraction.")
                    raise CustomException(e, sys)

            else:
                logging.error(f"Unsupported file format: {ext}")
                raise ValueError("Unsupported file format. Please use PDF or DOCX.")

            if not text.strip():
                logging.warning("Text extraction completed but no text found in file.")
            else:
                logging.info(f"Text extraction successful. Extracted {len(text)} characters.")

            return TextExtractionArtifact(text=text.strip())

        except Exception as e:
            logging.error("Error occurred during text extraction process.")
            raise CustomException(e, sys)
