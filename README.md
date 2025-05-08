# Query-Focused EHR Summarization

This repository contains the official implementation of our reproduction of the paper:  
**[Query-Focused Electronic Health Record Summarization for Diagnostic Support](https://arxiv.org/abs/2211.08346)**  
by McInerney et al., EMNLP 2022.

We reproduce the core methodology using MIMIC-III data, ClinicalBERT embeddings, and distant supervision via ICD codes.

---

## 📋 Abstract

We investigate the reproducibility of a transformer-based model that generates EHR summaries targeted at radiological diagnosis queries. By using distant supervision from future ICD codes, we train ClinicalBERT-based classifiers to label pre-discharge sentences as relevant to post-imaging diagnostic outcomes. Our implementation follows the methodology of McInerney et al. and explores ablations such as pooling strategies to understand inductive biases. We report quantitative performance metrics and discuss reproducibility barriers in computational and data availability.

---

## 📺 Video

[Watch our final project video here](https://example.com/final-video-link)

---

## 🔗 GitHub Repo

[GitHub Repository: liamshen10/CS598_Final_Project](https://github.com/liamshen10/CS598_Final_Project.git)

---

## ⚙️ Requirements

To install dependencies:
Run the first cell in the finalProject.ipynb notebook

Required Python version: 3.11

Main packages:

transformers==4.39.3

scikit-learn

torch

pandas

spacy

nltk


## Data Access
You need credentialed access to MIMIC-III from PhysioNet to download:

NOTEEVENTS.csv

admissions.csv

diagnoses_icd.csv

#To get the sampleData needed for the .ipynb file, make sure to run the opening.py file on the NOTEEVENTS.csv file. THis is the subset of data used to train the model

## Evaluation
To evaluate the trained model and generate classification metrics:
Just run throught the .ipynb file

Outputs:

F1-score, precision, recall

Multiclass AUROC (one-vs-rest)

## Results
Our model achieves the following performance:

Metric	Value
Accuracy	5.0%
Macro F1	5.0%
AUROC (OVR)	~0.49

These results reflect the challenges of low-resource EHR learning with weak supervision and high label imbalance in small samples. See the full paper for analysis and ablation study results.



