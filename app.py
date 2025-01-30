import streamlit as st 
import os 
import google.generativeai as genai
from apikey import google_gemini_api_key

genai.configure(api_key=google_gemini_api_key)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

# setting up model
model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)


# Setiing app to wide mode
st.set_page_config(layout='wide')

# Title of an app ✍🏻🎭
st.title('🎭 BlogChef: Your AI Writing Companion')

# Subheader
st.subheader('Now you can cook perfect blogs with the help of AI \n BlogChef is your new AI Blog companion')

# Sidebar for user inputs
with st.sidebar:
    st.title('Enter your Blog Details:')

    blog_title = st.text_input('Blog Title:')
    keywords = st.text_area('keywords (comma-separated):')
    num_words = st.slider('Number of words', min_value=250, max_value=2000, step=10)
    num_images = st.number_input('Number of Images', min_value=1, max_value=5, step=1)
    submit_button = st.button('Generate Blog')

if submit_button:
    prompt = f"""Generate a comprehensive, engaging blog post relevant to the given title: "{blog_title}" 
        and keywords: "{keywords}". Ensure the content is approximately {num_words} words long, suitable for an online audience. 
        The blog should be original, informative, and maintain a consistent tone throughout. Also make sure not to include any kind of starting line like (Okay, here's a blog post based on your requirements:) in the response."""

    # Generate response from Gemini
    response = model.generate_content(prompt)

    # Display generated blog content
    st.subheader("Your AI-Generated Blog Post is cooked 🍲 ")
    st.write(response.text)
     