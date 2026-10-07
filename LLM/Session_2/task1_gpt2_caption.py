"""
Session 2 - Task 1
Install:  pip install transformers torch
Loads GPT-2 and generates a short Instagram-style caption for the prompt
'Sunset vibes at the beach'.
"""
from transformers import pipeline, set_seed

set_seed(42)  # same output every run

# Load GPT-2 text-generation model (downloads ~500 MB the first time)
generator = pipeline("text-generation", model="gpt2")

prompt = "Sunset vibes at the beach"

result = generator(
    prompt,
    max_new_tokens=25,        # keep the caption short
    num_return_sequences=1,
    do_sample=True,
    temperature=0.9,
    top_k=50,
    pad_token_id=50256,       # GPT-2 has no pad token, use EOS
)

caption = result[0]["generated_text"]
print("Prompt  :", prompt)
print("Caption :", caption)
