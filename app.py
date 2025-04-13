import streamlit as st
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# Page configuration
st.set_page_config(
    page_title="Ask Nietzsche here 🖤",
    page_icon="assets/ask.png",
    layout="centered"
)

# Load and inject custom CSS
with open("custom.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# App Logo
st.image("assets/ask.png", width=250)

# Title and Intro
st.title("Ask Nietzsche 🖤")
st.markdown("_Beyond morality, beyond convention. Ask your deepest question._")
st.markdown("---")

# Nietzsche GPT System Prompt
SYSTEM_PROMPT = """
You are Friedrich Nietzsche, the 19th-century German philosopher known for your bold, poetic, and intense tone.
You provoke deep reflection, challenge morals, question existence, and embrace the complexity of human nature.
Answer with philosophical depth, metaphorical expressions, and occasionally rhetorical questions.
"""

# GPT call function updated for openai>=1.0.0
def ask_nietzsche(question):
    client = openai.OpenAI(api_key=openai.api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        temperature=0.9,
        max_tokens=300
    )
    return response.choices[0].message.content.strip()

# User interaction
question = st.text_input("", placeholder="What is the meaning of suffering?")

if st.button("Ask Nietzsche"):
    if question:
        with st.spinner("Nietzsche is contemplating..."):
            answer = ask_nietzsche(question)
            st.markdown("---")
            st.markdown(f"**NietzscheGPT:** {answer}")
    else:
        st.warning("You must ask a question to gaze into the abyss.")
