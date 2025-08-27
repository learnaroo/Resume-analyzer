from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from src.exceptions import CustomException
from src.logger import logging
from src.pipeline.resume_analyser_pipeline import initiate_resume_analyser_pipeline
import shutil
import os
import uuid

app = FastAPI(title="Resume Analyzer API", version="1.0")

UPLOAD_DIR = "uploaded_resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/analyze_resume")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    """
    API Endpoint to analyze a resume against a job description.
    - Accepts resume file (PDF or DOCX)
    - Accepts job description (string)
    - Returns evaluation results in JSON
    """
    file_path = None
    try:
        logging.info(f"📥 Received request to analyze resume: {file.filename}")
        logging.info(f"Job description length: {len(job_description)} characters")

        # Validate file type
        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext not in [".pdf", ".docx"]:
            logging.warning(f"Unsupported file format: {file_ext}")
            raise HTTPException(status_code=400, detail="Only PDF and DOCX formats are supported.")

        # Save uploaded file temporarily
        unique_filename = f"{uuid.uuid4()}{file_ext}"
        file_path = os.path.join(UPLOAD_DIR, unique_filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        logging.info(f"✅ File saved at {file_path}")

        # Run pipeline
        result = initiate_resume_analyser_pipeline(file_path, job_description)

        logging.info("🎯 Resume analysis pipeline completed successfully.")
        return JSONResponse(content={"status": "success", "result": result})

    except CustomException as ce:
        logging.exception("❌ CustomException occurred during resume analysis.")
        raise HTTPException(status_code=500, detail=str(ce))

    except HTTPException:
        raise  # re-raise explicit HTTP exceptions (e.g., bad file format)

    except Exception as e:
        logging.exception("❌ Unexpected error occurred during resume analysis.")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    finally:
        # Clean up temp file
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
            logging.info(f"🧹 Temporary file {file_path} deleted.")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
