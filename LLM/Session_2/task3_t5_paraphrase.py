"""
Session 2 - Task 3
Install:  pip install transformers torch sentencepiece
Paraphrase a sentence with T5-base using the prefix 'paraphrase: '.

Note: the original t5-base was not specially trained for paraphrasing, so the
output may be close to the input. A paraphrase-tuned T5 gives better results.
"""
from transformers import T5Tokenizer, T5ForConditionalGeneration

model_name = "t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

sentence = "BookMyShow makes movie ticket booking easy and fast."
input_text = "paraphrase: " + sentence          # required prefix

inputs = tokenizer(input_text, return_tensors="pt", truncation=True)

outputs = model.generate(
    **inputs,
    max_length=40,
    num_beams=5,
    num_return_sequences=1,
    early_stopping=True,
)

paraphrase = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Original   :", sentence)
print("Paraphrased:", paraphrase)
