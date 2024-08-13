# text-extraction-using-gemini-1.5-flash
 A Streamlit web application that uses Google's Gemini AI to analyze uploaded invoice images and answer user questions about the invoice content. This tool streamlines invoice interpretation by leveraging advanced image recognition and natural language processing capabilities.

 # Invoice Analysis AI

## Description
Invoice Analysis AI is a Streamlit web application that leverages Google's Gemini AI to analyze uploaded invoice images and answer user questions about the invoice content. This tool streamlines invoice interpretation by combining advanced image recognition and natural language processing capabilities.

## Workflow and Pipeline

1. **User Interface (Streamlit)**
   - Users interact with a web-based interface built using Streamlit.
   - The interface allows users to:
     - Upload an invoice image
     - Enter a question about the invoice
     - Submit for analysis

2. **Image Upload and Preprocessing**
   - When a user uploads an image, it's processed using the `prepare_image_for_api` function.
   - The image is converted into a format suitable for the Gemini AI API.

3. **User Input Processing**
   - The user's question is captured as text input.
   - A predefined prompt is combined with the user's question to guide the AI's analysis.

4. **Gemini AI Integration**
   - The application uses the `google.generativeai` library to interact with the Gemini AI model.
   - The model used is 'gemini-1.5-flash', which is capable of processing both images and text.

5. **API Request**
   - The `get_gemini_response` function sends a request to the Gemini AI API.
   - This request includes:
     - The preprocessed image
     - The user's question
     - A predefined prompt to guide the AI's analysis

6. **Response Processing**
   - The API's response is captured and processed.
   - Any errors during this process are caught and reported to the user.

7. **Result Display**
   - The processed response from the Gemini AI is displayed to the user in the Streamlit interface.

## Setup and Installation

1. Clone the repository
2. Install required dependencies: (present in `requirement.txt` file)
3. Set up a `.env` file with your Google API key: `GOOGLE_API_KEY=your_actual_api_key_here`
4. Run the Streamlit app: `text-extraction-ui.py`
5. Run the output command in the terminal window, it will redirect you to streamlit app UI

## Usage

1. Upload an invoice image (supported formats: jpg, jpeg, png)
2. Enter a question about the invoice
3. Click "Analyze Invoice"
4. View the AI-generated analysis of your invoice


## Note
Ensure your Google API key has the necessary permissions to use the Gemini AI models. Keep your API key confidential and never share it publicly.
