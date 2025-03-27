# Job Fit Analyzer
Deployed on Hugging Face: [https://huggingface.co/spaces/surajsde/Job-Fit-Analyzer]

**Job Fit Analyzer** is a Streamlit-based web application that uses Google's Gemini AI and an ATS (Applicant Tracking System) approach to analyze and evaluate resumes against job descriptions. The tool provides feedback on resume alignment and calculates a percentage match between the job description and the uploaded resume.

## Features
- **Job Description Analysis:** Input a job description to be evaluated.
- **Resume Evaluation:** Upload a PDF resume to check its alignment with the provided job description.
- **Strengths and Weaknesses Report:** Receive an AI-generated evaluation of the applicant's strengths and weaknesses.
- **Percentage Match:** Get a percentage score reflecting how well the resume matches the job description, along with missing keywords and final thoughts.

## Prerequisites
Make sure you have the following installed before running the project:
- Python 3.x
- Streamlit
- `PyPDF2` for converting PDF files to text
- `Pillow` (PIL) for image handling
- `python-dotenv` for loading environment variables
- `google-generativeai` for AI-based resume analysis

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Surajgupta63/Job-Fit-Analyzer.git
   cd Job-Fit-Analyzer
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables**:
   Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

## Project Structure
- `app.py`: The main application file containing the Streamlit interface and AI-based resume analysis logic.
- `.env`: Stores the Google API key for authentication (add your API key here).
- `requirements.txt`: Lists all required Python packages.

## Usage
1. **Enter the Job Description**: Paste or type the job description into the text area.
2. **Upload a Resume**: Upload your resume in PDF format.
3. **Submit for Evaluation**:
   - **"Tell Me About the Resume"**: Get an evaluation of strengths, weaknesses, and alignment with the job description.
   - **"Percentage Match"**: Calculate the match percentage and view missing keywords.

## Example Prompts
The app uses the following prompts to generate its AI responses:
- **Prompt 1:** Professional evaluation of the resume, focusing on strengths and weaknesses.
- **Prompt 2:** ATS-style evaluation with percentage match, missing keywords, and final thoughts.

## Technologies Used
- **Streamlit**: Frontend UI framework for easy web app deployment.
- **Google's Gemini AI**: AI-based text generation for resume analysis.
- **PDF to Image Conversion**: `pdf2image` and Poppler for processing PDF resumes.
- **Python Libraries**: `PIL` (image handling), `dotenv` (environment variables), `base64` (encoding).

## Contributing
Feel free to contribute to this project by submitting issues or pull requests.


