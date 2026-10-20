"""
Session 3 - Task 1: Load a pre-trained sentiment model, apply LoRA with peft,
and print trainable parameters BEFORE and AFTER.

Install: pip install transformers torch peft
Run    : python task1_lora_params.py
"""
from transformers import AutoModelForSequenceClassification
from peft import LoraConfig, get_peft_model, TaskType

MODEL = "distilbert-base-uncased-finetuned-sst-2-english"   # pre-trained sentiment model


def count_params(model):
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    return trainable, total


model = AutoModelForSequenceClassification.from_pretrained(MODEL)
t, total = count_params(model)
print(f"BEFORE LoRA -> trainable: {t:,} / total: {total:,}  ({100*t/total:.2f}%)")

lora_config = LoraConfig(
    task_type=TaskType.SEQ_CLS,
    r=8,                               # rank of the small matrices
    lora_alpha=16,
    lora_dropout=0.1,
    target_modules=["q_lin", "v_lin"], # DistilBERT attention layers
)
peft_model = get_peft_model(model, lora_config)

t, total = count_params(peft_model)
print(f"AFTER  LoRA -> trainable: {t:,} / total: {total:,}  ({100*t/total:.2f}%)")
peft_model.print_trainable_parameters()   # peft's built-in helper
