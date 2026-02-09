import streamlit as st
from openai import OpenAI

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="OpenAI Streamlit Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 OpenAI Chatbot")
st.write("Chat with an OpenAI-powered assistant")

# -----------------------------
# API Key Input
# -----------------------------
api_key = st.sidebar.text_input(
    "Enter your OpenAI API Key",
    type="password"
)

if not api_key:
    st.warning("Please enter your OpenAI API key in the sidebar.")
    st.stop()

client = OpenAI(api_key=api_key)

# -----------------------------
# Session State Initialization
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# -----------------------------
# Display Chat History
# -----------------------------
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# -----------------------------
# User Input
# -----------------------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call OpenAI API
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.responses.create(
                model="gpt-5.2",
                input=st.session_state.messages
            )

            bot_reply = response.output_text
            st.markdown(bot_reply)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )
