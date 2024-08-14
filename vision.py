from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure the Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the function to get response from the AI model
model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input_text, image):
    if input_text:
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

# Set the page configuration
st.set_page_config(page_title="VISION AI", page_icon="👁️", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .stApp {
        background-color: #1e1e1e;
    }
    .stButton > button {
        background-color: #007ACC;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        border: none;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #005F99;
    }
    .stTextInput > div > input {
        border-radius: 5px;
        border: 1px solid #ccc;
        padding: 0.5rem;
        background-color: #333;
        color: white;
    }
    .stFileUploader > div > div > div > button {
        background-color: #007ACC;
        color: white;
        border-radius: 5px;
    }
    .stImage > img {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    }
    .stHeader {
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    .stMarkdown {
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Create the main app layout
st.title("Vision AI Application")
st.write("Analyze images and prompts using advanced AI.")

# Input and file uploader
input_text = st.text_input("Enter a prompt or leave it blank to analyze only the image:", key="input")
uploaded_file = st.file_uploader("Choose an image file (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Button to submit the input and image
submit = st.button("Analyze Image")

# Display the response when the button is clicked
if submit:
    with st.spinner("Analyzing..."):
        response = get_gemini_response(input_text, image)
    st.header("AI Response")
    st.write(response)

# Dark mode toggle button
# dark_mode = st.checkbox("Toggle Dark Mode", value=True)

# # JavaScript to toggle dark mode
# st.markdown("""
#     <script>
#     const darkMode = %s;
#     if (!darkMode) {
#         document.body.style.backgroundColor = '#f5f5f5';
#         document.body.style.color = '#000000';
#     }
#     </script>
# """ % dark_mode, unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr style="margin-top: 3rem;"/>
    <div style="text-align: center;">
        <p>Created by Ashish Pandey | Made with Streamlit</p>
    </div>
""", unsafe_allow_html=True)
