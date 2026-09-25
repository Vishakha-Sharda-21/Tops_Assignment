"""
Session 5 - Task 3
A basic Streamlit chatbot UI where users can ask about food recommendations
and see a bot response, fetching the most relevant review from the vector
DB / similarity search built in Task 2.

Run:
    streamlit run task3_streamlit_food_chatbot.py
"""

import streamlit as st
from sentence_transformers import SentenceTransformer, util

reviews = [
    "The best pizza in town, crispy crust and generous cheese every time.",
    "Their biryani is rich, fragrant, and always perfectly spiced.",
    "Great sushi rolls, super fresh fish and beautiful presentation.",
    "Amazing pasta with a creamy alfredo sauce, generous portions too.",
    "Best paneer tikka I've had, smoky flavor and soft texture.",
]


@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


model = load_model()
review_embeddings = model.encode(reviews, convert_to_tensor=True)


def find_best_match(query: str) -> str:
    query_embedding = model.encode(query, convert_to_tensor=True)
    similarities = util.cos_sim(query_embedding, review_embeddings)[0]
    best_idx = int(similarities.argmax())
    return reviews[best_idx]


st.set_page_config(page_title="Food Recommendation Bot", page_icon="🍴")
st.title("🍴 Food Recommendation Bot")
st.caption("Ask about a dish or cuisine and I'll pull the closest matching review.")

user_query = st.text_input("What are you craving?", placeholder="e.g. best pizza")

if user_query:
    answer = find_best_match(user_query)
    st.markdown("**Bot:**")
    st.write(answer)
