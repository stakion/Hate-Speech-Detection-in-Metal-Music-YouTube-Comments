# Hate Speech Detection in Metal Music YouTube Comments  
## Abstract
This project presents a controlled experimental study on hate speech detection in YouTube comments associated with metal music videos. The investigation evaluates Transformer-based architectures (BERT-base) and domain-adapted toxic language models (HateBERT) under multiple training configurations using the HateXplain and ETHOS datasets.

A structured pipeline was implemented including dataset normalization, binary corpus construction, early stopping analysis, and cross-dataset training. Eight controlled experiments were conducted to analyze overfitting behavior, dataset bias, generalization stability, and false positive rates when transferring models to real-world YouTube comments collected via automated scraping.

Results show that BERT exhibits rapid overfitting after 2–3 epochs, while domain-specific models require fine-tuning to reduce severe false positive behavior. The findings highlight the importance of early stopping, dataset diversity, and domain adaptation when deploying hate speech classifiers in culturally expressive online communities.
<br>

## Objectives:
### General:
Analyze and compare the performance of Transformer-based models and Mamba-based architectures in detecting hate speech in YouTube comments across metal bands.

### Specific:
1. Train and evaluate Transformer-based and Mamba-based models on labeled datasets to detect hate speech in metal music video youtube comments.
2. Test models on multiple labeled datasets and measure the variation in performance to assess dataset bias and generalization potential.


## Research Motivation
Online music communities frequently exhibit aggressive linguistic styles that may be misclassified by traditional hate speech detection systems. <br>
Metal music discussions in particular contain:
- Sarcasm
- Slang
- Aggressive tone
- Contextual irony

This project evaluates whether Transformer-based models can distinguish between stylistic aggression and actual hate speech.


## Research Questions
- How does **BERT-base (uncased)** compare with **HateBERT (RoBERTa toxic-pretrained)**?
- Does combining HateXplain and ETHOS improve generalization?
- How does dataset selection impact false positives?
- Does longer training increase overfitting?
- How well do trained models transfer to real YouTube comments?


## Related Work
This project builds upon recent advances in hate speech detection for social media platforms. 

Prior work such as *“Misogynistic Attitude Detection in YouTube Comments and Replies”* proposes high-quality annotated datasets and algorithmic models for toxic language classification in video platforms. 

The study *“DweshVaani: An LLM for Detecting Religious Hate Speech in Code-Mixed Hindi-English”* demonstrates the effectiveness of large language models in handling multilingual and culturally nuanced hate speech.

Additionally, *“Detection of Homophobia and Transphobia in YouTube Comments”* highlights the importance of context-aware classification in identity-based hate detection. 

These works collectively show that hate speech detection is highly dependent on dataset construction, linguistic diversity, and domain adaptation. Inspired by these findings, this project evaluates Transformer-based architectures (BERT, HateBERT) under controlled experimental conditions to analyze overfitting, dataset bias, and cross-domain generalization in metal music YouTube comments.

## Datasets Used
### HateXplain: https://github.com/hate-alert/HateXplain
- Explainable hate speech dataset (2020)

### ETHOS: https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset
- Binary classification corpus constructed for this study


## Pipeline Structure Steps
1. Dataset normalization  
2. English-language filtering  
3. Tokenization  
4. Binary corpus construction  
5. Transformer fine-tuning
6. GPU Optimizations through a RTX 4090
7. Evaluation (Accuracy, F1, Loss curves)  
8. Inference on real YouTube comments


## YouTube English Comments Per Musical Video
| Music Video                         | English Comments  |
|-------------------------------------|-------------------|
| Black Sabbath – War Pigs            | 29068             |
| Hallowed Be Thy Name (Remaster)     | 1793              |
| Master of Puppets (Remastered)      | 10149             |
| Pantera – Cowboys From Hell         | 10724             |
| Slayer – Raining Blood              | 17852             |


## Experimental Summary Table
| Exp | Model      | Data Used               | Epochs | Core Observation                          | Main Conclusion |
|-----|------------|------------------------|--------|--------------------------------------------|-----------------|
| 1   | BERT       | HateXplain             | 10     | Val loss ↑ after early epochs              | Early overfitting (2–3 epochs) |
| 2   | BERT       | HateXplain             | 30     | No val improvement, instability ↑          | Longer training worsens generalization |
| 3   | BERT       | HateXplain             | 100    | Train loss → 0, val loss high              | Severe memorization, no real gain |
| 4   | BERT       | HateXplain             | 2      | Stable val loss, improved F1               | Early stopping optimal |
| 5   | BERT       | HateXplain + ETHOS     | 2      | Slight robustness improvement              | Dataset diversity helps but domain bias remains |
| 6   | HateBERT   | None (Pretrained only) | —      | Massive over-prediction on YouTube         | Domain mismatch → extreme false positives |
| 7   | HateBERT   | HateXplain + ETHOS     | 2      | False positives drastically reduced        | Fine-tuning essential for adaptation |
| 8   | HateBERT   | HateXplain + ETHOS     | 10     | Slight improvement, mild overfitting signs | Controlled early stopping still required |


## Hate Speech Detections per Experiment (YouTube Inference)
| Music Video                         | Exp 1 | Exp 2 | Exp 3 | Exp 4 | Exp 5 | Exp 6 | Exp 7 | Exp 8 |
|-------------------------------------|-------|-------|-------|-------|-------|-------|-------|-------|
| Black Sabbath – War Pigs            | 337   | 154   | 225   | 170   | 207   | 3388  | 209   | 229   |
| Hallowed Be Thy Name (Remaster)     | 9     | 7     | 6     | 0     | 3     | 265   | 1     | 3     |
| Master of Puppets (Remastered)      | 32    | 14    | 20    | 10    | 9     | 1664  | 3     | 7     |
| Pantera – Cowboys From Hell         | 81    | 45    | 52    | 32    | 30    | 1686  | 31    | 39    |
| Slayer – Raining Blood              | 182   | 94    | 144   | 78    | 61    | 2424  | 70    | 111   |


## Key Findings
- BERT overfits rapidly on HateXplain
- Validation loss increases after early epochs
- Dataset bias impacts classification stability
- Domain-adapted models require fine-tuning
- Real-world YouTube comments demand multilingual expansion
- False positive control is critical for production systems


## File Descriptions
| File Name                          | Description |
|------------------------------------|-------------|
| PROYECT_05.pptx                    | Project presentation summarizing the research motivation, problem statement, experimental design, dataset selection, evaluation metrics, and comparative results between BERT and HateBERT architectures. It documents the research questions, related work, and conclusions regarding overfitting and domain adaptation in hate speech detection for YouTube metal comments. |
| PROGRESS_02.ipynb                  | Main experimentation notebook containing the full machine learning pipeline. It includes dataset preprocessing, binary corpus construction, tokenization, Transformer fine-tuning, training/validation loss tracking, evaluation metrics computation (Accuracy, F1-score), and inference over real YouTube comments. All experimental variants (BERT, HateBERT, multi-dataset training) are implemented and evaluated here. |
| Capture_comments_04.py             | Data acquisition script responsible for extracting YouTube comments using `yt_dlp`. It retrieves comment text and metadata (likes, author, timestamps), structures the information into pandas DataFrames, and exports CSV files for downstream preprocessing and model inference. This file enables real-world validation of trained models. |
| HATEXPLAIN_CLEAN_True_Final_01.csv | Preprocessed version of the HateXplain dataset adapted into a binary classification format (hate vs non-hate). Includes normalized and filtered text data used for supervised training and evaluation of Transformer-based models. |
| Ethos_Dataset_Binary.csv           | Binary-labeled version of the ETHOS hate speech dataset. Used both independently and in combination with HateXplain to analyze dataset bias, cross-dataset generalization, and false positive behavior in hate speech detection models. |
| Experimental_Tags/Hate_Speech_001  | Labeling of comments using BERT trained on HateXplain (10 epochs) |
| Experimental_Tags/Hate_Speech_002  | Labeling of comments using BERT trained on HateXplain (30 epochs) |
| Experimental_Tags/Hate_Speech_003  | Labeling of comments using BERT trained on HateXplain (100 epochs) |
| Experimental_Tags/Hate_Speech_004  | Labeling of comments using BERT trained on HateXplain (2 epochs) |
| Experimental_Tags/Hate_Speech_005  | Labeling using BERT trained on HateXplain + ETHOS |
| Experimental_Tags/Hate_Speech_006  | Labeling using pretrained HateBERT (no fine-tuning) |
| Experimental_Tags/Hate_Speech_007  | Labeling using fine-tuned HateBERT (2 epochs) |
| Experimental_Tags/Hate_Speech_008  | Labeling using fine-tuned HateBERT (10 epochs) |

## Reproducibility
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

## Future Work
Several research directions emerge from this investigation.

First, the implementation of State Space Models such as Mamba should be revisited. Although preliminary attempts were made, training instability and convergence issues prevented reliable evaluation. Future work should focus on architectural adaptation, hyperparameter tuning, and longer sequence optimization to properly assess whether Mamba-based models provide advantages over Transformer architectures in hate speech detection tasks.

Second, multilingual expansion is necessary. The current pipeline restricts analysis to English-language comments, limiting generalization in real YouTube environments. Future work should include automatic translation, multilingual tokenizers, or multilingual pre-trained models to evaluate cross-lingual robustness.

Third, false positive rate analysis should be quantified more rigorously. While qualitative observations revealed severe over-prediction in non-fine-tuned HateBERT, a systematic statistical comparison across experiments (e.g., precision-recall trade-offs, confusion matrices, ROC curves) would provide stronger deployment-oriented insights.

Fourth, dataset bias and cross-domain generalization require deeper investigation. Controlled experiments across multiple music genres (e.g., rap, pop, electronic) could reveal whether aggressive linguistic styles uniquely impact hate speech classifiers in metal communities.

Finally, semi-supervised or agent-assisted labeling approaches could be explored. Large language models may be used to generate pseudo-labels for unlabeled YouTube comments, enabling expanded domain adaptation while maintaining supervised control.

These directions aim to improve robustness, reduce false positives, and enhance the applicability of hate speech detection systems in culturally expressive online communities.
