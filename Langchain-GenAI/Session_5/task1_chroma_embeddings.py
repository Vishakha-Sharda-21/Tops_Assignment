"""
Session 5 - Task 1
Install Chroma locally and store embeddings for 5 restaurant reviews.

Requires:
    pip install chromadb sentence-transformers
"""

import chromadb
from chromadb.utils import embedding_functions

reviews = [
    "The best pizza in town, crispy crust and generous cheese every time.",
    "Their biryani is rich, fragrant, and always perfectly spiced.",
    "Great sushi rolls, super fresh fish and beautiful presentation.",
    "Amazing pasta with a creamy alfredo sauce, generous portions too.",
    "Best paneer tikka I've had, smoky flavor and soft texture.",
]

client = chromadb.PersistentClient(path="./chroma_db")

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.get_or_create_collection(
    name="restaurant_reviews", embedding_function=embedding_fn
)

collection.add(
    documents=reviews,
    ids=[f"review_{i}" for i in range(len(reviews))],
)

print(f"Stored {len(reviews)} restaurant review embeddings in Chroma collection 'restaurant_reviews'.")
