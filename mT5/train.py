import torch
from torch.utils.data import DataLoader
from transformers import MT5ForConditionalGeneration, MT5Tokenizer
from torch.optim import AdamW
from tqdm import tqdm

from dataset import Copus

MODEL_NAME = "google/mt5-small"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
EPOCHS = 200
BATCH_SIZE = 16
LR = 3e-4

tokenizer = MT5Tokenizer.from_pretrained(MODEL_NAME)
model = MT5ForConditionalGeneration.from_pretrained(MODEL_NAME).to(DEVICE)

dataset = Copus(
    csv_path="data/file01.csv",
    tokenizer=tokenizer
)

loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

optimizer = AdamW(model.parameters(), lr=LR)

model.train()
for epoch in range(EPOCHS):
    total_loss = 0

    progress_bar = tqdm(
        loader,
        desc=f"Epoch {epoch+1}/{EPOCHS}",
        leave=True
    )

    for batch in progress_bar:
        optimizer.zero_grad()

        outputs = model(
            input_ids=batch["input_ids"].to(DEVICE),
            attention_mask=batch["attention_mask"].to(DEVICE),
            labels=batch["labels"].to(DEVICE)
        )

        loss = outputs.loss
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        progress_bar.set_postfix(loss=f"{loss.item():.4f}")

    avg_loss = total_loss / len(loader)
    print(f"\nEpoch {epoch+1} completed | Avg Loss: {avg_loss:.4f}\n")

model.save_pretrained("mt5-khmer-summary")
tokenizer.save_pretrained("mt5-khmer-summary")