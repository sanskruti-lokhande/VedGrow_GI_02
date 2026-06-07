import streamlit as st

st.set_page_config(page_title="BCA FAQ Chatbot")

st.title("BCA Student FAQ Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

faq = {
    "what is bca": "BCA stands for Bachelor of Computer Applications.",
    "best language for bca": "Python, Java, JavaScript and SQL are excellent choices.",
    "career after bca": "You can become a Software Developer, Web Developer, Data Analyst, QA Engineer, or pursue MCA.",
    "internship tips": "Build projects, maintain GitHub repositories, and improve your coding skills."
}

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask a question")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    answer = "Sorry, I can only answer BCA-related questions."

    for key in faq:
        if key in user_input.lower():
            answer = faq[key]
            break

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()
