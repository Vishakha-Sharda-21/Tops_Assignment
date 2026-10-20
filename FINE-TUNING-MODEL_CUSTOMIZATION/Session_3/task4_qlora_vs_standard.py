"""
Session 3 - Task 4: QLoRA (4-bit) vs standard fine-tuning, with RAM/GPU memory monitoring.

Install: pip install transformers torch peft bitsandbytes accelerate psutil
REQUIREMENT: QLoRA needs bitsandbytes and an NVIDIA GPU (use Google Colab free T4 if your laptop has none).

Run two times and compare the memory numbers:
    python task4_qlora_vs_standard.py standard
    python task4_qlora_vs_standard.py qlora
Also open Task Manager (Windows) or `top`/`htop` (Linux) during training and take a screenshot.
"""
import sys
import psutil
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training, TaskType
from custom_data import TEXTS, LABELS

mode = sys.argv[1] if len(sys.argv) > 1 else "qlora"
MODEL = "distilbert-base-uncased"
proc = psutil.Process()


def ram_mb():
    return proc.memory_info().rss / 1024 / 1024


def gpu_mb():
    return torch.cuda.max_memory_allocated() / 1024 / 1024 if torch.cuda.is_available() else 0.0


print(f"Mode: {mode}")
print(f"RAM before loading model: {ram_mb():.0f} MB")

tokenizer = AutoTokenizer.from_pretrained(MODEL)

if mode == "qlora":
    bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                             bnb_4bit_compute_dtype=torch.float16, bnb_4bit_use_double_quant=True)
    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL, num_labels=2, quantization_config=bnb, device_map="auto")
    model = prepare_model_for_kbit_training(model)
else:
    model = AutoModelForSequenceClassification.from_pretrained(MODEL, num_labels=2)
    if torch.cuda.is_available():
        model = model.to("cuda")

config = LoraConfig(task_type=TaskType.SEQ_CLS, r=8, lora_alpha=16, lora_dropout=0.1,
                    target_modules=["q_lin", "v_lin"])
model = get_peft_model(model, config)
model.print_trainable_parameters()
print(f"RAM after loading model : {ram_mb():.0f} MB | GPU peak: {gpu_mb():.0f} MB")

enc = tokenizer(TEXTS, padding=True, truncation=True, return_tensors="pt").to(model.device)
labels = torch.tensor(LABELS).to(model.device)
opt = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=5e-4)

model.train()
for epoch in range(10):
    loss = model(**enc, labels=labels).loss
    loss.backward()
    opt.step()
    opt.zero_grad()
    print(f"Epoch {epoch+1:2d} loss={loss.item():.4f} | RAM={ram_mb():.0f} MB | GPU peak={gpu_mb():.0f} MB")

print(f"\nFINAL ({mode}): RAM={ram_mb():.0f} MB, GPU peak={gpu_mb():.0f} MB")
