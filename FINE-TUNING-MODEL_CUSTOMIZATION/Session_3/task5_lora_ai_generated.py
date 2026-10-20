"""
Session 3 - Task 5: LoRA on a Hugging Face model for text classification
(code snippet generated with an AI assistant, then cleaned up).

Install: pip install transformers datasets peft torch accelerate
Run    : python task5_lora_ai_generated.py
"""
import numpy as np
from datasets import Dataset
from transformers import (AutoTokenizer, AutoModelForSequenceClassification,
                          TrainingArguments, Trainer)
from peft import LoraConfig, get_peft_model, TaskType
from custom_data import TEXTS, LABELS

MODEL = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(MODEL)

ds = Dataset.from_dict({"text": TEXTS, "label": LABELS})
ds = ds.map(lambda x: tokenizer(x["text"], truncation=True, padding="max_length", max_length=64),
            batched=True)
ds = ds.train_test_split(test_size=0.3, seed=42)

model = AutoModelForSequenceClassification.from_pretrained(MODEL, num_labels=2)
model = get_peft_model(model, LoraConfig(task_type=TaskType.SEQ_CLS, r=8, lora_alpha=16,
                                         lora_dropout=0.1, target_modules=["q_lin", "v_lin"]))
model.print_trainable_parameters()


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    return {"accuracy": float((np.argmax(logits, axis=-1) == labels).mean())}


args = TrainingArguments(output_dir="lora_trainer_out", num_train_epochs=5,
                         per_device_train_batch_size=4, learning_rate=5e-4,
                         eval_strategy="epoch", save_strategy="no", report_to="none",
                         logging_steps=1)
trainer = Trainer(model=model, args=args, train_dataset=ds["train"],
                  eval_dataset=ds["test"], compute_metrics=compute_metrics)
trainer.train()
print(trainer.evaluate())
model.save_pretrained("lora_trainer_adapter")
