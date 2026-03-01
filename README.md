# Hate Speech Detection in Metal Music YouTube Comments  

<br>
<br>

## Objectives:
### General:
Analyze and compare the performance of Transformer-based models and Mamba-based architectures in detecting hate speech in YouTube comments across metal bands.

### Specific:
1. Train and evaluate Transformer-based and Mamba-based models on labeled datasets to detect hate speech in metal music video youtube comments.
2. Test models on multiple labeled datasets and measure the variation in performance to assess dataset bias and generalization potential.
<br>
<br>

## 1. Research Motivation
Online music communities frequently exhibit aggressive linguistic styles that may be misclassified by traditional hate speech detection systems. <br>
Metal music discussions in particular contain:
- Sarcasm
- Slang
- Aggressive tone
- Contextual irony

This project evaluates whether Transformer-based models can distinguish between stylistic aggression and actual hate speech.
<br>
<br>

## 2. Research Questions
- How does **BERT-base (uncased)** compare with **HateBERT (RoBERTa toxic-pretrained)**?
- Does combining HateXplain and ETHOS improve generalization?
- How does dataset selection impact false positives?
- Does longer training increase overfitting?
- How well do trained models transfer to real YouTube comments?
<br>
<br>

## 3. Related Work
This project builds upon recent advances in hate speech detection for social media platforms. <br>

Prior work such as *“Misogynistic Attitude Detection in YouTube Comments and Replies”* proposes high-quality annotated datasets and algorithmic models for toxic language classification in video platforms. <br>

The study *“DweshVaani: An LLM for Detecting Religious Hate Speech in Code-Mixed Hindi-English”* demonstrates the effectiveness of large language models in handling multilingual and culturally nuanced hate speech. <br>

Additionally, *“Detection of Homophobia and Transphobia in YouTube Comments”* highlights the importance of context-aware classification in identity-based hate detection. <br>

These works collectively show that hate speech detection is highly dependent on dataset construction, linguistic diversity, and domain adaptation. Inspired by these findings, this project evaluates Transformer-based architectures (BERT, HateBERT) under controlled experimental conditions to analyze overfitting, dataset bias, and cross-domain generalization in metal music YouTube comments.
<br>
<br>

## 4. Datasets Used
### HateXplain: https://github.com/hate-alert/HateXplain
- Explainable hate speech dataset (2020)

### ETHOS: https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset
- Binary classification corpus constructed for this study
<br>
<br>

## 5. Pipeline Structure Steps
1. Dataset normalization  
2. English-language filtering  
3. Tokenization  
4. Binary corpus construction  
5. Transformer fine-tuning
6. GPU Optimizations through a RTX 4090.
7. Evaluation (Accuracy, F1, Loss curves)  
8. Inference on real YouTube comments  
<br>
<br>

## 6. Experimental Analysis
### Experiment 1 – BERT (HateXplain, 10 Epochs)
A BERT-base (uncased) model was trained using only the HateXplain dataset for 10 epochs. While training loss decreased steadily, validation loss increased after early epochs, indicating early overfitting. Although accuracy remained relatively stable (~83%), the F1 score fluctuated. <br>
**Main Finding:** The model begins overfitting after 2–3 epochs, suggesting that longer training does not improve generalization.
<br>

### Experiment 2 – BERT (HateXplain, 30 Epochs)
To confirm the overfitting behavior, training was extended to 30 epochs. Validation performance did not improve and instability increased across epochs. <br>
**Main Finding:** Additional training time worsens generalization. Overfitting is confirmed and early stopping is necessary.
<br>

### Experiment 3 – BERT (HateXplain, 100 Epochs, GPU Optimized)
A long training run (100 epochs) was executed with GPU optimization to test whether extended convergence improves robustness, reaching 1 Epoch / min. Training loss approached zero, while validation loss remained high. <br>
**Main Finding:** Severe overfitting occurs. The model memorizes training data without improving real-world performance.
<br>

### Experiment 4 – BERT (HateXplain, 2 Epochs)
Based on previous findings, training was reduced to 2 epochs. Validation loss stabilized and F1-score improved compared to longer runs. <br>
**Main Finding:** Early stopping significantly improves generalization. Optimal performance occurs within the first 2 epochs.
<br>

### Experiment 5 – BERT (HateXplain + ETHOS, 2 Epochs)
Datasets were combined to increase diversity and reduce dataset bias. The model was trained for 2 epochs. <br>
**Main Finding:** Dataset combination slightly improves robustness and reduces overfitting effects, but domain transfer limitations persist.
<br>

### Experiment 6 – HateBERT (No Fine-Tuning)
HateBERT (RoBERTa variant pre-trained on toxic Reddit comments) was tested without fine-tuning. The model massively over-predicted hate speech in YouTube comments. <br>
**Main Finding:** Domain mismatch causes extreme false positives. Pretrained toxic models do not generalize automatically to music-related discourse.
<br>

### Experiment 7 – HateBERT (Fine-Tuned, 2 Epochs)
HateBERT was fine-tuned using HateXplain and ETHOS. False positives were drastically reduced compared to the non-fine-tuned version. <br>
**Main Finding:** Domain adaptation via fine-tuning is essential for reducing misclassification in culturally specific contexts. <br>
<br>

### Experiment 8 – HateBERT (Fine-Tuned, 10 Epochs)
Fine-tuning was extended to 10 epochs to test performance stability. Results showed moderate improvement in detection but signs of slight overfitting reappeared. <br>
**Main Finding:** Even domain-adapted models benefit from controlled early stopping. Optimal training duration remains short.
<br>
<br>

## 7. Key Findings
- BERT overfits rapidly on HateXplain
- Validation loss increases after early epochs
- Dataset bias impacts classification stability
- Domain-adapted models require fine-tuning
- Real-world YouTube comments demand multilingual expansion
- False positive control is critical for production systems
<br>
<br>

## 8. Evaluation Metrics
### Classification Metrics
- Accuracy
- F1 Score
- Training Loss
- Validation Loss
<br>

### Representation Metrics
- Cosine Distance
- Euclidean Distance
- Perplexity
<br>

### Information Retrieval Metrics
- Mean Average Precision (MAP)
- NDCG (Normalized Discounted Cumulative Gain)
<br>
<br>

## 9. File Descriptions
### PROYECT_05.pptx
Project presentation summarizing the research motivation, problem statement, experimental design, dataset selection, evaluation metrics, and comparative results between BERT and HateBERT architectures. It documents the research questions, related work, and conclusions regarding overfitting and domain adaptation in hate speech detection for YouTube metal comments.
<br>

### PROGRESS_02.ipynb
Main experimentation notebook containing the full machine learning pipeline. It includes dataset preprocessing, binary corpus construction, tokenization, Transformer fine-tuning, training/validation loss tracking, evaluation metrics computation (Accuracy, F1-score), and inference over real YouTube comments. All experimental variants (BERT, HateBERT, multi-dataset training) are implemented and evaluated here.
<br>

### Capture_comments_04.py
Data acquisition script responsible for extracting YouTube comments using `yt_dlp`. It retrieves comment text and metadata (likes, author, timestamps), structures the information into pandas DataFrames, and exports CSV files for downstream preprocessing and model inference. This file enables real-world validation of trained models.
<br>

### HATEXPLAIN_CLEAN_True_Final_01.csv
Preprocessed version of the HateXplain dataset adapted into a binary classification format (hate vs non-hate). Includes normalized and filtered text data used for supervised training and evaluation of Transformer-based models.
<br>

### Ethos_Dataset_Binary.csv
Binary-labeled version of the ETHOS hate speech dataset. Used both independently and in combination with HateXplain to analyze dataset bias, cross-dataset generalization, and false positive behavior in hate speech detection models.
<br>
<br>

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

