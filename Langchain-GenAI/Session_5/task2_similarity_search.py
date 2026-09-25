"""
Session 5 - Task 2
Takes a user's search query and finds the most similar stored review
using cosine similarity, via sentence-transformers embeddings.
"""

from sentence_transformers import SentenceTransformer, util

reviews = [
    "The best pizza in town, crispy crust and generous cheese every time.",
    "Their biryani is rich, fragrant, and always perfectly spiced.",
    "Great sushi rolls, super fresh fish and beautiful presentation.",
    "Amazing pasta with a creamy alfredo sauce, generous portions too.",
    "Best paneer tikka I've had, smoky flavor and soft texture.",
]

model = SentenceTransformer("all-MiniLM-L6-v2")
review_embeddings = model.encode(reviews, convert_to_tensor=True)


def find_best_match(query: str) -> str:
    query_embedding = model.encode(query, convert_to_tensor=True)
    similarities = util.cos_sim(query_embedding, review_embeddings)[0]
    best_idx = int(similarities.argmax())
    return reviews[best_idx]


if __name__ == "__main__":
    query = "best pizza"
    print(f"Query: {query}")
    print(f"Most similar review: {find_best_match(query)}")
