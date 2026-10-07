"""
Session 2 - Task 2
Install:  pip install transformers torch
Classify sentiment of a Zomato review using a BERT model.

Note: plain 'bert-base-uncased' is only a pre-trained base model (it has no
sentiment head), so for real predictions we use a BERT-base-uncased model that
was FINE-TUNED on sentiment (SST-2). The quick-setup default pipeline from the
hint is also shown (it uses DistilBERT, a smaller BERT).
"""
from transformers import pipeline

review = "The food was absolutely delicious and the delivery was super fast."

# --- Method 1: quick setup (as given in the hint) ---
quick = pipeline("sentiment-analysis")
print("Default pipeline  :", quick(review))

# --- Method 2: BERT-base-uncased fine-tuned for sentiment ---
bert = pipeline(
    "sentiment-analysis",
    model="textattack/bert-base-uncased-SST-2",
)
out = bert(review)[0]
# this model returns LABEL_1 = positive, LABEL_0 = negative
label = "POSITIVE" if out["label"] == "LABEL_1" else "NEGATIVE"
print("BERT-base-uncased :", label, f"(confidence {out['score']:.2f})")
