# Session 5 - Task 4

**How RAG improves answer quality vs. a plain LLM with no document retrieval:**

A plain language model can only answer from what it memorized during
training, so it has no way to know about our specific restaurant reviews or
menu, and it's likely to either say it doesn't know or hallucinate a
plausible-sounding but wrong answer. Retrieval-Augmented Generation fixes
this by first searching a knowledge source (our Chroma vector DB of reviews)
for the most relevant piece of real text, and then feeding that retrieved
text into the LLM's prompt as grounding context before it answers. This
means the chatbot's response is anchored to actual, up-to-date data we
control, rather than the model's frozen training knowledge — so answers are
more accurate, specific to our restaurants, and far less likely to be made
up, and we can update the reviews/menu at any time without retraining
anything.
