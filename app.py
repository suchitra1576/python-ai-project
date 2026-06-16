import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Page title
st.set_page_config(
    page_title="AI Student Assistant",
    page_icon="🎓"
)

st.title("🎓 AI Student Assistant")
st.write("Ask me anything about studies, internships, resumes, or interviews.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask a question...")

if prompt:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Student assistant prompt
    system_prompt = f"""
    You are an AI Student Assistant.

    Help students with:
    - Study planning
    - Internship guidance
    - Resume improvement
    - Interview preparation
    - Time management

    Student Question:
    {prompt}
    """

    # Gemini response
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=system_prompt
    )

    answer = response.text

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
    