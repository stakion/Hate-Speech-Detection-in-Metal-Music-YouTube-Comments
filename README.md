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

### 3. Related Work

## Related Work
This project builds upon recent advances in hate speech detection for social media platforms. 

Prior work such as *“Misogynistic Attitude Detection in YouTube Comments and Replies”* proposes high-quality annotated datasets and algorithmic models for toxic language classification in video platforms. 

The study *“DweshVaani: An LLM for Detecting Religious Hate Speech in Code-Mixed Hindi-English”* demonstrates the effectiveness of large language models in handling multilingual and culturally nuanced hate speech. 

Additionally, *“Detection of Homophobia and Transphobia in YouTube Comments”* highlights the importance of context-aware classification in identity-based hate detection. 

These works collectively show that hate speech detection is highly dependent on dataset construction, linguistic diversity, and domain adaptation. Inspired by these findings, this project evaluates Transformer-based architectures (BERT, HateBERT) under controlled experimental conditions to analyze overfitting, dataset bias, and cross-domain generalization in metal music YouTube comments.

---

## 4. Datasets Used

### HateXplain: https://github.com/hate-alert/HateXplain
- Explainable hate speech dataset (2020)

### ETHOS: https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset
- Binary classification corpus constructed for this study

---

## 5. Pipeline Structure Steps
1. Dataset normalization  
2. English-language filtering  
3. Tokenization  
4. Binary corpus construction  
5. Transformer fine-tuning  
6. Evaluation (Accuracy, F1, Loss curves)  
7. Inference on real YouTube comments  

---

## 6. Model Variants Evaluated
### Experiments 1–4
- BERT-base (uncased)
- HateXplain only
- 2–100 epochs
- Overfitting observed after 2–3 epochs

### Experiment 5
- HateXplain + ETHOS combined

### Experiment 6
- HateBERT without fine-tuning
- Severe over-prediction of hate speech (high false positives)

### Experiments 7–8
- HateBERT fine-tuned on combined datasets
- Significant reduction in false positives
- Improved domain adaptation

---

## 7. Key Findings

- BERT overfits rapidly on HateXplain
- Validation loss increases after early epochs
- Dataset bias impacts classification stability
- Domain-adapted models require fine-tuning
- Real-world YouTube comments demand multilingual expansion
- False positive control is critical for production systems

---

## 8. Evaluation Metrics

### Classification Metrics
- Accuracy
- F1 Score
- Training Loss
- Validation Loss

### Representation Metrics
- Cosine Distance
- Euclidean Distance
- Perplexity

### Information Retrieval Metrics
- Mean Average Precision (MAP)
- NDCG (Normalized Discounted Cumulative Gain)

---

## 9. Repository Structure
├── Capture_comments_04.py
├── PROGRESS_02.ipynb
├── PROYECT_05.pptx
├── HATEXPLAIN_CLEAN_True_Final_01.csv
├── Ethos_Dataset_Binary.csv

---

## 10. Reproducibility

### Install Dependencies
```bash
pip install transformers torch pandas yt-dlp numpy
```

### Run Experiments: 
```bash
jupyter notebook PROGRESS_02.ipynb
```

### Extract YouTube Comments: 
```bash
python Capture_comments_04.py
```

