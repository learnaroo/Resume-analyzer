# Resume Analyzer API

A FastAPI-based resume analysis tool that evaluates resumes against job descriptions using AI-powered text processing and analysis.

## 📁 Project Structure

```
RESUME_ANALYSER/
├── data/                           # Data storage directory
├── logs/                          # Application logs
├── src/                           # Source code
│   ├── components/                # Core components
│   │   ├── __init__.py
│   │   ├── evaluator.py          # Resume evaluation logic
│   │   └── text_extracter.py     # Text extraction from files
│   ├── constants/                 # Application constants
│   │   └── __init__.py
│   ├── entity/                    # Data models and entities
│   │   ├── __init__.py
│   │   ├── artifacts.py          # Artifact definitions
│   │   └── config.py             # Configuration settings
│   ├── exceptions/                # Custom exception handling
│   │   └── __init__.py
│   ├── logger/                    # Logging configuration
│   │   └── __init__.py
│   ├── pipeline/                  # Processing pipeline
│   │   ├── __init__.py
│   │   └── resume_analyser_pipeline.py
│   └── __init__.py
├── venv/                          # Virtual environment
├── .env                           # Environment variables
├── .gitignore                     # Git ignore rules
├── app.py                         # FastAPI application
└── requirements.txt               # Python dependencies
```

## 🚀 Features

- **Resume Upload**: Support for PDF and DOCX file formats
- **Job Description Analysis**: Compare resumes against job requirements
- **AI-Powered Evaluation**: Intelligent matching and scoring
- **RESTful API**: Easy integration with web applications
- **Structured Logging**: Comprehensive logging for debugging
- **Error Handling**: Robust exception management
- **File Cleanup**: Automatic temporary file management

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd RESUME_ANALYSER
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

5. **Create necessary directories**
   ```bash
   mkdir -p data logs uploaded_resumes
   ```

## 🏃‍♂️ Running the Application

### Development Mode

```bash
python app.py
```

The API will be available at `http://localhost:8000`

### Production Mode

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

## 📚 API Documentation

### Analyze Resume Endpoint

**POST** `/analyze_resume`

Analyzes a resume file against a job description and returns evaluation results.

#### Request Parameters

- `file` (form-data): Resume file (PDF or DOCX format)
- `job_description` (form-data): Job description text

#### Example Request

```bash
curl -X POST "http://localhost:8000/analyze_resume" \
  -F "file=@resume.pdf" \
  -F "job_description=Software Engineer position requiring Python, FastAPI, and machine learning experience..."
```

#### Response Format

```json
{
  "status": "success",
  "result": {
    "score": 85,
    "match_percentage": 78,
    "key_skills_found": ["Python", "FastAPI", "Machine Learning"],
    "missing_skills": ["Docker", "Kubernetes"],
    "recommendations": ["Add containerization experience", "Include cloud platform knowledge"]
  }
}
```

#### Error Responses

- `400 Bad Request`: Invalid file format
- `500 Internal Server Error`: Processing error

### Interactive API Documentation

Visit `http://localhost:8000/docs` for Swagger UI documentation or `http://localhost:8000/redoc` for ReDoc documentation.

## 🧪 Testing

### Manual Testing

1. Start the server
2. Navigate to `http://localhost:8000/docs`
3. Use the interactive interface to test the `/analyze_resume` endpoint

### Example Files

Create test files in a `test_data/` directory:
- Sample PDF resume
- Sample DOCX resume
- Various job descriptions

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG_MODE=True

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/app.log

# File Processing
MAX_FILE_SIZE=10485760  # 10MB
ALLOWED_EXTENSIONS=pdf,docx

# AI/ML Configuration
MODEL_NAME=your_model_name
API_KEY=your_api_key
```

### Supported File Formats

- **PDF**: Adobe Portable Document Format
- **DOCX**: Microsoft Word Document

## 📋 Dependencies

Key dependencies include:

- **FastAPI**: Modern web framework for APIs
- **uvicorn**: ASGI server implementation
- **python-multipart**: File upload support
- **PyPDF2/pdfplumber**: PDF text extraction
- **python-docx**: DOCX file processing
- **Additional ML/NLP libraries**: As specified in requirements.txt

## 🚨 Error Handling

The application includes comprehensive error handling:

- **File Format Validation**: Ensures only supported formats
- **Custom Exceptions**: Structured error management
- **Logging**: Detailed error tracking
- **Graceful Failures**: User-friendly error messages

## 🧹 File Management

- Temporary files are automatically cleaned up after processing
- Upload directory is created automatically
- File size limits prevent abuse

## 📊 Logging

Logs are stored in the `logs/` directory and include:

- Request processing information
- Error details and stack traces
- Performance metrics
- File operations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

[Add your license information here]

## 🆘 Support

For issues and questions:
- Check the logs in the `logs/` directory
- Review the API documentation at `/docs`
- Create an issue in the repository

## 🔮 Future Enhancements

- Support for additional file formats
- Batch processing capabilities
- Advanced matching algorithms
- Integration with job boards
- Resume improvement suggestions
- Multi-language support