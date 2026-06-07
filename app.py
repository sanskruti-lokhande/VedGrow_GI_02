import streamlit as st

st.title("🎓 BCA Student FAQ Chatbot")

st.write("Ask me questions about BCA, programming, internships, and career options.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask a question...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    if len(st.session_state.messages) > 10:
        st.session_state.messages = st.session_state.messages[-10:]

    response = (
        "This is a placeholder response. "
        "In the next step we will connect OpenAI API."
    )

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()
