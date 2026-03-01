# Hate Speech Detection in Metal Music YouTube Comments  
### Transformer vs Domain-Specific Toxic Language Models

---

## Abstract
This project investigates hate speech detection in YouTube comments associated with metal music videos. It compares general-purpose Transformer architectures (BERT Base) against domain-adapted toxic language models (HateBERT) using benchmark datasets (HateXplain, ETHOS) and real-world scraped YouTube comments.

The objective is to analyze generalization performance, dataset bias, overfitting behavior, and domain adaptation impact when detecting hate speech in culturally dense online communities.

---

## 1. Research Motivation

Online music communities frequently exhibit aggressive linguistic styles that may be misclassified by traditional hate speech detection systems.

Metal music discussions in particular contain:
- Sarcasm
- Slang
- Aggressive tone
- Contextual irony

This project evaluates whether Transformer-based models can distinguish between stylistic aggression and actual hate speech.

---

## 2. Research Questions

- How does **BERT-base (uncased)** compare with **HateBERT (RoBERTa toxic-pretrained)**?
- Does combining HateXplain and ETHOS improve generalization?
- How does dataset selection impact false positives?
- Does longer training increase overfitting?
- How well do trained models transfer to real YouTube comments?

---

## 3. Datasets Used

### HateXplain: https://github.com/hate-alert/HateXplain
- Explainable hate speech dataset (2020)

### ETHOS: https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset
- Binary classification corpus constructed for this study

---
