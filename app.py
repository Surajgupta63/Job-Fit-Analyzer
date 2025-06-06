import os
import io
import base64
from PIL import Image
import streamlit as st
import PyPDF2 as pdf
from dotenv import load_dotenv
import google.generativeai as genai 

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content, prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += str(page.extract_text())
        return text
    else:
        raise FileNotFoundError('Please upload a file!')
    
## Streamlit Setup
st.set_page_config(page_title='Job Fit: ATS')
st.header("Job Fit Analyzer")

input_text = st.text_area('Job Description', key='input')
uploaded_file = st.file_uploader('Upload your resume(PDF only)', type=['pdf'])

if uploaded_file is not None:
    st.success('File succesfully uploaded')


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("Percentage match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and deep ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1 and uploaded_file is not None:
    pdf_content = input_pdf_setup(uploaded_file)
    response = get_gemini_response(input_prompt1, pdf_content, input_text)
    st.subheader('The Response is')
    st.write(response)

elif submit2 and uploaded_file is not None:
    pdf_content = input_pdf_setup(uploaded_file)
    response = get_gemini_response(input_prompt2, pdf_content, input_text)
    st.subheader('The Response is:')
    st.write(response)