"""
Session 5 - Insta Caption Generator (Tasks 1 to 5 in one file)

Setup:
    pip install streamlit requests
    set OPENAI_API_KEY=your_key_here          (Windows CMD)
    export OPENAI_API_KEY=your_key_here       (Mac/Linux)
Run:
    streamlit run insta_caption_generator.py

Uses the 'requests' library to call the OpenAI API (as per the hint).
Hugging Face alternative is given at the bottom (commented).
"""
import os
import requests
import streamlit as st

# ---------------------------------------------------------------- Task 1
st.title("Welcome to Insta Caption Generator!")

# API key: from environment variable or typed in the sidebar
api_key = os.getenv("OPENAI_API_KEY") or st.sidebar.text_input(
    "OpenAI API Key", type="password"
)

API_URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-4o-mini"


# ---------------------------------------------------------------- Task 4
def generate_caption(description: str) -> str:
    """Call the OpenAI API and return an Instagram caption."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You write short, catchy Instagram captions with 2-3 emojis and 3 hashtags.",
            },
            {
                "role": "user",
                "content": f"Write one Instagram caption for a photo of: {description}",
            },
        ],
        "max_tokens": 80,
        "temperature": 0.8,
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        return f"Error while calling the API: {e}"


# ---------------------------------------------------------------- Task 5
# session_state keeps the chat history alive between button clicks
if "history" not in st.session_state:
    st.session_state.history = []     # list of (user_text, ai_caption)

# ---------------------------------------------------------------- Task 2
description = st.text_input("Describe your photo")
generate = st.button("Generate Caption")

# ---------------------------------------------------------------- Task 3 + 4
if generate:
    if not description.strip():
        st.warning("Please describe your photo first.")
    elif not api_key:
        st.error("Please add your OpenAI API key (sidebar or OPENAI_API_KEY).")
    else:
        # Task 3: show the user's input
        st.write("Your Description:")
        st.write(description)

        with st.spinner("Generating caption..."):
            caption = generate_caption(description)

        # Task 4: show AI caption below
        st.subheader("Generated Caption")
        st.success(caption)

        # Task 5: save to history
        st.session_state.history.append((description, caption))

# ---------------------------------------------------------------- Task 5
# show the last 3 exchanges as chat bubbles
if st.session_state.history:
    st.divider()
    st.subheader("Recent Captions")
    for user_text, ai_text in st.session_state.history[-3:]:
        with st.chat_message("user"):
            st.write(user_text)
        with st.chat_message("assistant"):
            st.write(ai_text)

# ------------------------------------------------------------------------
# Hugging Face alternative for generate_caption():
#   HF_URL = "https://api-inference.huggingface.co/models/<model-name>"
#   headers = {"Authorization": f"Bearer {HF_TOKEN}"}
#   r = requests.post(HF_URL, headers=headers, json={"inputs": prompt})
#   text = r.json()[0]["generated_text"]
