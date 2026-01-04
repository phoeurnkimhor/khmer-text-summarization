import pandas as pd
from torch.utils.data import Dataset

class Copus(Dataset):
    def __init__(self, csv_path, tokenizer, max_input_len=512, max_target_len=128):
        self.df = pd.read_csv(csv_path)
        self.tokenizer = tokenizer
        self.max_input_len = max_input_len
        self.max_target_len = max_target_len

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        article = str(self.df.iloc[idx]["content"])
        summary = str(self.df.iloc[idx]["summary"])

        # 🔑 mT5 task prefix
        article = "summary: " + article

        inputs = self.tokenizer(
            article,
            max_length=self.max_input_len,
            truncation=True,
            padding="max_length",
            return_tensors="pt"
        )

        labels = self.tokenizer(
            summary,
            max_length=self.max_target_len,
            truncation=True,
            padding="max_length",
            return_tensors="pt"
        ).input_ids

        return {
            "input_ids": inputs.input_ids.squeeze(),
            "attention_mask": inputs.attention_mask.squeeze(),
            "labels": labels.squeeze()
        }