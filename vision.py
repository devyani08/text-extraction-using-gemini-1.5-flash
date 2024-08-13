import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the generative AI with the API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("No API key found. Please set the GOOGLE_API_KEY environment variable.")
genai.configure(api_key=api_key)

def get_gemini_response(input_prompt, image_data, user_input):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Updated model name
    try:
        response = model.generate_content([input_prompt, image_data[0], user_input])
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def prepare_image_for_api(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        return [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
    else:
        return None

# Streamlit UI setup
st.set_page_config(page_title="Invoice Analysis with Gemini")
st.header("Invoice Analysis Application")

st.write("This application uses Google's Gemini AI to analyze invoices. Upload an image of an invoice and ask questions about it.")

user_input = st.text_input("Enter your question about the invoice:", key="input")
uploaded_file = st.file_uploader("Upload an invoice image (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_column_width=True)

submit_button = st.button("Analyze Invoice")

input_prompt = """
You are an expert in understanding invoices.
You will receive input images as invoices and
you will have to answer questions based on the input image.
"""

if submit_button:
    if not uploaded_file:
        st.error("Please upload an image before analyzing.")
    elif not user_input:
        st.error("Please enter a question about the invoice.")
    else:
        with st.spinner("Analyzing the invoice..."):
            image_data = prepare_image_for_api(uploaded_file)
            response = get_gemini_response(input_prompt, image_data, user_input)
            st.subheader("Analysis Result")
            st.write(response)
