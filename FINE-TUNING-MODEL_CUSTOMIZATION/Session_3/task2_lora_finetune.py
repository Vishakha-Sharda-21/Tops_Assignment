"""
Session 3 - Task 2: Fine-tune a text classification model on 10 tweets using LoRA (peft),
save the adapter weights to disk and report the file size.

Install: pip install transformers torch peft
Run    : python task2_lora_finetune.py
"""
import os
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from peft import LoraConfig, get_peft_model, TaskType
from custom_data import TEXTS, LABELS

MODEL = "distilbert-base-uncased"
SAVE_DIR = "lora_sentiment_adapter"

tokenizer = AutoTokenizer.from_pretrained(MODEL)
base = AutoModelForSequenceClassification.from_pretrained(MODEL, num_labels=2)

config = LoraConfig(task_type=TaskType.SEQ_CLS, r=8, lora_alpha=16,
                    lora_dropout=0.1, target_modules=["q_lin", "v_lin"])
model = get_peft_model(base, config)          # hint: get_peft_model + LoraConfig
model.print_trainable_parameters()

enc = tokenizer(TEXTS, padding=True, truncation=True, return_tensors="pt")
labels = torch.tensor(LABELS)

optimizer = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=5e-4)

model.train()
for epoch in range(10):
    out = model(**enc, labels=labels)
    out.loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    print(f"Epoch {epoch+1:2d}  loss = {out.loss.item():.4f}")

# quick test
model.eval()
test = tokenizer(["Loved the food and quick delivery!", "Very bad app, always crashing"],
                 padding=True, return_tensors="pt")
with torch.no_grad():
    pred = model(**test).logits.argmax(dim=-1).tolist()
print("Predictions (1=positive, 0=negative):", pred)

# save ONLY the LoRA adapter weights
model.save_pretrained(SAVE_DIR)
size = sum(os.path.getsize(os.path.join(SAVE_DIR, f)) for f in os.listdir(SAVE_DIR))
for f in os.listdir(SAVE_DIR):
    print(f"  {f}: {os.path.getsize(os.path.join(SAVE_DIR, f))/1024:.1f} KB")
print(f"Total adapter size on disk: {size/1024:.1f} KB ({size/1024/1024:.2f} MB)")
print("(Full DistilBERT is about 255 MB, so the adapter is much smaller.)")
