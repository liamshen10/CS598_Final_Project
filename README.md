
# 🧠 Query-Focused EHR Summarization

This repository contains the official implementation of our reproduction of the paper:  
**[Query-Focused Electronic Health Record Summarization for Diagnostic Support](https://arxiv.org/abs/2211.08346)**  
by McInerney et al., EMNLP 2022.

We replicate the core methodology using MIMIC-III data, ClinicalBERT embeddings, and distant supervision via ICD codes to build a query-focused summarization pipeline for clinical decision support.

---

## 📋 Abstract

We investigate the reproducibility of a transformer-based summarization model tailored for radiological diagnosis queries. By leveraging distant supervision from post-discharge ICD codes, we train ClinicalBERT-based classifiers to identify relevant sentences from pre-discharge clinical notes. Our pipeline implements the methodology proposed by McInerney et al., with adaptations for public MIMIC-III data, and explores ablation strategies like alternative pooling techniques. We report performance metrics and identify barriers related to computational constraints, weak labeling, and dataset sparsity.

---

## 📺 Video Presentation

🎥 [Watch our final project video here](https://youtu.be/ruyZwse6_4Y)

---

## 🔗 GitHub Repository

🔗 [liamshen10/CS598_Final_Project](https://github.com/liamshen10/CS598_Final_Project.git)

---

## ⚙️ Requirements

To run the project, open `finalProject.ipynb` in Google Colab or a local Jupyter environment.

**Python Version:** 3.11  
Install dependencies via:

```bash
pip install -r requirements.txt
```

**Core Python Libraries:**
- `transformers==4.39.3`
- `torch`
- `scikit-learn`
- `pandas`
- `spacy`
- `nltk`

---

## 📂 Data Access

This project uses three tables from the [MIMIC-III Clinical Database](https://physionet.org/content/mimiciii/1.4/):

- `NOTEEVENTS.csv`
- `ADMISSIONS.csv`
- `DIAGNOSES_ICD.csv`

### 🔐 Access Instructions:
1. Complete CITI “Data or Specimens Only Research” training via PhysioNet.
2. Request credentialed access through your institution.
3. After downloading the CSVs, run `opening.py` on `NOTEEVENTS.csv` to generate the `simulated_noteevents.csv` subset for training.

---

## 🚀 Running the Model

1. Load the `simulated_noteevents.csv` into the notebook.
2. Follow the notebook cells to:
   - Preprocess and tokenize data
   - Train ClinicalBERT using weak supervision
   - Evaluate predictions using multiclass classification metrics

---

## 📊 Evaluation Metrics

The following metrics are computed using `sklearn.metrics`:

- **Accuracy**
- **Macro-averaged F1 Score**
- **Multiclass AUROC** (One-vs-Rest)
- **Precision / Recall per class**

---

## 📈 Results

| Metric       | Value |
|--------------|-------|
| Accuracy     | 5.0%  |
| Macro F1     | 5.0%  |
| AUROC (OVR)  | ~0.49 |

These results highlight the challenges of weak supervision, label imbalance, and computational limits. See our full report for an ablation analysis and discussion of model limitations.

---

## 🧪 Ablation Study

We tested an alternative pooling strategy using average token pooling (instead of the default `[CLS]` embedding). The change had minimal impact (AUROC ~0.488), suggesting that dataset quality and label sparsity were bigger performance bottlenecks than architecture design.

---

## 👥 Authors

- **Liam Shen** – liams4
- **Abhitej Bokka** – abhitej2

