import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
import PyPDF2
import io

# Load environment variables
load_dotenv()

# Configure the generative AI with the API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("No API key found. Please set the GOOGLE_API_KEY environment variable.")
genai.configure(api_key=api_key)

def get_gemini_response(input_prompt, file_content, user_input):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Updated model name
    try:
        response = model.generate_content([input_prompt, file_content, user_input])
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def prepare_file_for_api(uploaded_file):
    if uploaded_file is not None:
        file_type = uploaded_file.type
        if file_type in ['image/jpeg', 'image/png']:
            return prepare_image_for_api(uploaded_file)
        elif file_type == 'application/pdf':
            return prepare_pdf_for_api(uploaded_file)
        else:
            return None
    else:
        return None

def prepare_image_for_api(uploaded_file):
    bytes_data = uploaded_file.getvalue()
    return [
        {
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }
    ]

def prepare_pdf_for_api(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.getvalue()))
    text_content = ""
    for page in pdf_reader.pages:
        text_content += page.extract_text() + "\n"
    return text_content

# Streamlit UI setup
st.set_page_config(page_title="Invoice Analysis with Gemini")
st.header("Invoice Analysis Application")

st.write("This application uses Google's Gemini AI to analyze invoices. Upload an image or PDF of an invoice and ask questions about it.")

user_input = st.text_input("Enter your question about the invoice:", key="input")
uploaded_file = st.file_uploader("Upload an invoice file (jpg, jpeg, png, pdf)", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file:
    if uploaded_file.type in ['image/jpeg', 'image/png']:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Invoice", use_column_width=True)
    elif uploaded_file.type == 'application/pdf':
        st.success("PDF uploaded successfully")

submit_button = st.button("Analyze Invoice")

input_prompt = """
You are an expert in understanding invoices.
You will receive either an image of an invoice or text extracted from a PDF invoice.
You will have to answer questions based on the provided invoice data.
"""

if submit_button:
    if not uploaded_file:
        st.error("Please upload an invoice file before analyzing.")
    elif not user_input:
        st.error("Please enter a question about the invoice.")
    else:
        with st.spinner("Analyzing the invoice..."):
            file_content = prepare_file_for_api(uploaded_file)
            response = get_gemini_response(input_prompt, file_content, user_input)
            st.subheader("Analysis Result")
            st.write(response)
