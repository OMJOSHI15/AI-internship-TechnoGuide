import streamlit as st
from google import genai

# API setup
client = genai.Client(api_key="AIzaSyBMXQ3vpH2shIeYx2cYmxhvCd9fUJTqfuA")

# Streamlit UI
st.title("🤖 Gemini AI Chatbot")

user_input = st.text_input("Ask something")

if st.button("Send"):

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_input
    )

    st.success(response.text)