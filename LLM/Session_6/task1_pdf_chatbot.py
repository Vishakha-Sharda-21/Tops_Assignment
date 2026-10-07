"""
Session 6 - Task 1: Simple PDF Chatbot (upload PDF -> extract text -> show in browser)
Setup:  pip install streamlit PyPDF2
Run  :  streamlit run task1_pdf_chatbot.py
"""
import streamlit as st
from PyPDF2 import PdfReader


def extract_text(pdf_file) -> str:
    """Read every page of the uploaded PDF and return the combined text."""
    reader = PdfReader(pdf_file)
    text = ""
    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""
        text += f"\n--- Page {page_number} ---\n{page_text}"
    return text


if __name__ == "__main__":
    st.title("PDF Chatbot")
    st.write("Upload a PDF (college timetable, IRCTC ticket, notes...) and see its text.")

    uploaded = st.file_uploader("Upload your PDF", type=["pdf"])

    if uploaded is not None:
        extracted = extract_text(uploaded)
        if extracted.strip():
            st.success("Text extracted successfully!")
            st.text_area("Extracted text", extracted, height=400)

            # tiny bonus: keyword search inside the PDF
            question = st.text_input("Search a word in the PDF (e.g., 'Monday' or 'PNR')")
            if question:
                lines = [l for l in extracted.splitlines() if question.lower() in l.lower()]
                if lines:
                    st.write(f"Found {len(lines)} matching line(s):")
                    for line in lines:
                        st.write("-", line)
                else:
                    st.info("No match found.")
        else:
            st.warning("No text found. This may be a scanned PDF (image only).")
