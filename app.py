# app.py

import streamlit as st
from main import ask_question

st.set_page_config(
    page_title="✈️ AeroRAG",
    layout="centered"
)

st.title("✈️ Air-India-Assistant")

st.markdown("Ask questions about Air India booking policies")

# =========================
# SESSION MEMORY (CHAT HISTORY)
# =========================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =========================
# INPUT BOX
# =========================
user_query = st.text_input("Ask your question:")

if st.button("Submit"):

    if user_query:
        answer = ask_question(user_query)

        st.session_state.chat_history.append(("You", user_query))
        st.session_state.chat_history.append(("Bot", answer))


# =========================
# DISPLAY CHAT
# =========================
for role, message in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"🧑‍💻 **You:** {message}")
    else:
        st.markdown(f"🤖 **Bot:** {message}")