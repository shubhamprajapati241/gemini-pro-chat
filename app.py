from dotenv import load_dotenv
import streamlit as st 
from PIL import Image 
import google.generativeai as genai 
import os

# load the environment variable 
load_dotenv()

# set the Google API key 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = genai.GenerativeModel('gemini-1.5-flash')
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

# function to generate text 
def generate(input_question, image):
    task = [input_question, image]
    response = model.generate_content(task)
    return response.text

# streamlit app 
st.title("Generative AI Vision App")
st.markdown("""
Welcome to the Generative AI Vision App!
Ask a question about the uploaded image, and let the model describe it.  
""")

# user input for question 
input_question = st.text_input("Input your question here : ", key="input")

# File upload for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.")

# button to trigger image description generative 
submit_button = st.button("Tell me about the image")

# Generate and display response on button click 
if submit_button:
    if input_question == "":
        st.error("Please enter a question")
        st.stop()
    
    if image == "":
        st.error("Please upload the image")
        st.stop()

    with st.spinner("Generating response..."):
        response = generate(input_question, image)
    st.success(response)