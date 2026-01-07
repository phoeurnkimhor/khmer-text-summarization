# Khmer Text Summarization

[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Models-yellow?logo=huggingface)](https://huggingface.co)
[![PyTorch](https://img.shields.io/badge/PyTorch-Framework-EE4C2C?logo=pytorch)](https://pytorch.org)

This project builds an automatic summarization system for Khmer text. It explores both extractive and abstractive methods and highlights Khmer-specific challenges like word segmentation, complex morphology, and script handling.

The system is applied to news articles, educational content, and social media posts.


## Features

* **Extractive Summarization:**

  * TF-IDF ranking
  * TextRank algorithm
  * Clustering-based sentence selection

* **Abstractive Summarization (Transformer-based):**

  * mT5 and mBART (`facebook/mbart-large-50`)
  * KhmerBERT

* **Evaluation:** ROUGE scores and manual inspection

* **Address Khmer-specific challenges:** Tokenization, slang, formal vs. informal text

## Evaluation Metrics

* **ROUGE-1, ROUGE-2, ROUGE-L** for automated comparison.
* Manual inspection for **fluency**, **faithfulness**, and **summary readability**.

## Contributors

This project was conducted at the Institute of Technology of Cambodia, [Department of Applied Mathematics and Statistics](https://www.facebook.com/ams.itc.edu.kh/).

- Lecturer: [**Mr. KHEAN Vesal**](https://github.com/kheanvesal)
- Team Members:
    - [**NGORN Panha**](https://github.com/PanhaNgorn)
    - [**OEUN Pao**](https://github.com/Oeunpao99) 
    - [**PAV Limseng**](https://github.com/PLSeng)
    - [**PEANG Rattanak**](https://github.com/Peang-Rattanak)
    - [**PHOEURN Kimhor**](https://github.com/phoeurnkimhor)
    - [**PHORN Sreypov**](https://github.com/Povsundra)



