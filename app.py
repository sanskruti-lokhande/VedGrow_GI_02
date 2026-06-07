import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="BCA FAQ Chatbot")

st.title("🎓 BCA Student FAQ Chatbot")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

SYSTEM_PROMPT = """
You are a BCA Student FAQ Assistant.

You only answer questions related to:
- BCA
- Programming
- Internships
- Career guidance
- Software development
- Computer science education

If a question is outside these topics, politely respond:
'Sorry, I can only answer BCA and technology-related questions.'
"""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask your question")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    memory = st.session_state.messages[-11:]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=memory
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    st.rerun()
