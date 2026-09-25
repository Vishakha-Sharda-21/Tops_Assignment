"""
Session 5 - Task 5
Modify the Streamlit chatbot so it connects to a local text file of food
facts (one per line), generates embeddings for each line, and uses
similarity search over that file as its knowledge source.

Run:
    streamlit run task5_streamlit_textfile_rag.py
"""

import streamlit as st
from sentence_transformers import SentenceTransformer, util

FACTS_FILE = "food_facts.txt"


@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


@st.cache_data
def load_facts(path):
    with open(path, "r") as f:
        # one fact per line, skip any blank lines
        return [line.strip() for line in f if line.strip()]


model = load_model()
facts = load_facts(FACTS_FILE)
fact_embeddings = model.encode(facts, convert_to_tensor=True)


def find_best_fact(query: str) -> str:
    query_embedding = model.encode(query, convert_to_tensor=True)
    similarities = util.cos_sim(query_embedding, fact_embeddings)[0]
    best_idx = int(similarities.argmax())
    return facts[best_idx]


st.set_page_config(page_title="Food Facts Bot", page_icon="🥑")
st.title("🥑 Food Facts Bot")
st.caption(f"Knowledge source: {FACTS_FILE} ({len(facts)} facts loaded)")

user_query = st.text_input("Ask me a food question:", placeholder="e.g. does honey go bad?")

if user_query:
    answer = find_best_fact(user_query)
    st.markdown("**Bot:**")
    st.write(answer)
