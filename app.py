import streamlit as st
from dotenv import load_dotenv
import os
from google import genai
load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
client=genai.Client(api_key=api_key)
st.set_page_config(
    page_title="Gemini AI chatbot",
    page_icon="🤖",
    layout="centered"
)
st.title("🤖 Gemini AI chatbot")
st.write("Ask Gemini anything!")
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words..."
)
if st.button("Generate Response"):
    if prompt:
        with st.spinner("Gemini is thinking..."):
            response = client.models.generate_content(
                model="Gemini-3.5-flash-lite",
                contents=prompt
            )
        st.success("Response generated!")
        st.write(response.text)
    else:
        st.warning("please enter a prompt.")