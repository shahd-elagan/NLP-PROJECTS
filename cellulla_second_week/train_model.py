import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model
import torch

# Load dataset
df = pd.read_csv("cellula_toxic.csv")

df = df[["query", "toxic category"]]
df.columns = ["text", "label"]

# Convert labels to numbers
label_map = {label: i for i, label in enumerate(df["label"].unique())}
df["label"] = df["label"].map(label_map)

dataset = Dataset.from_pandas(df)

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

def tokenize(example):
    return tokenizer(example["text"], truncation=True, padding="max_length")

dataset = dataset.map(tokenize)

model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=len(label_map)
)

# LoRA configuration
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_lin","v_lin"],
    lora_dropout=0.1,
    bias="none",
    task_type="SEQ_CLS"
)

model = get_peft_model(model, lora_config)

training_args = TrainingArguments(
    output_dir="./toxic_model",
    per_device_train_batch_size=8,
    num_train_epochs=2,
    logging_steps=10
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

trainer.train()

model.save_pretrained("toxic_model")
tokenizer.save_pretrained("toxic_model")

print("Training finished")