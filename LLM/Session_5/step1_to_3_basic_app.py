# Session 5 - Tasks 1, 2 and 3 (basic UI, no API yet)
# Run:  streamlit run step1_to_3_basic_app.py
import streamlit as st

# Task 1: welcome text
st.title("Welcome to Insta Caption Generator!")

# Task 2: text input + button
description = st.text_input("Describe your photo")
generate = st.button("Generate Caption")

# Task 3: show user's input when button is clicked
if generate:
    st.write("Your Description:")
    st.write(description)
