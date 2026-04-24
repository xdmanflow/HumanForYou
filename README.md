# HumanForYou — Employee Turnover Analysis

> A machine learning project to identify and predict employee attrition at HumanForYou.

---

## Table of Contents

- [Background](#background)
- [Objectives](#objectives)
- [Project Structure](#project-structure)
- [Datasets](#datasets)
- [Methodology](#methodology)
- [Models & Evaluation](#models--evaluation)
- [Key Metrics](#key-metrics)
- [Deliverables](#deliverables)
- [Installation](#installation)
- [Usage](#usage)
- [Ethics & Compliance](#ethics--compliance)
- [Authors](#authors)
- [License](#license)

---

## Background

**HumanForYou** is a pharmaceutical company based in India employing approximately **4,000 people**. The company is currently experiencing an annual employee turnover rate of **15%**, which has a significant impact on:

- Productivity and institutional knowledge retention
- Recruitment and onboarding costs
- Team cohesion and project continuity

This project was initiated to understand the root causes of attrition and equip the HR department with data-driven tools to anticipate and reduce employee departures.

---

## Objectives

1. **Identify** the key factors that contribute to employee attrition
2. **Develop** predictive classification models to flag at-risk employees
3. **Interpret** model decisions using explainability techniques (SHAP)
4. **Recommend** concrete, actionable strategies for HR to reduce turnover

---

## Project Structure

```
HumanForYou/
├── data/                          # Raw data files
│   ├── general_data.csv           # Core HR and demographic data
│   ├── manager_survey_data.csv    # Manager performance assessments
│   ├── employee_survey_data.csv   # Employee satisfaction survey responses
│   └── in_out_time.zip            # Daily arrival and departure times (2015)
│
├── notebooks/                     # Jupyter notebooks
│   └── employee_turnover_analysis.ipynb
│
├── src/                           # Reusable Python modules
│   ├── data_loader.py             # Data ingestion utilities
│   ├── preprocessing.py           # Cleaning, encoding, feature engineering
│   └── model_evaluation.py        # Evaluation metrics and comparison tools
│
├── reports/                       # Project documentation
│   ├── ethics_document.md         # Ethical considerations and data governance
│   └── bibliography.md            # Academic and technical references
│
├── requirements.txt
└── README.md
```

---

## Datasets

### `general_data.csv` — Core HR Data

The primary dataset containing one row per employee with the following feature groups:

| Category | Features |
|----------|----------|
| **Demographics** | Age, Gender, MaritalStatus |
| **Job Information** | JobRole, JobLevel, Department, BusinessTravel |
| **Compensation** | MonthlyIncome, PercentSalaryHike, StockOptionLevel |
| **Experience** | TotalWorkingYears, YearsAtCompany, YearsSinceLastPromotion, NumCompaniesWorked |
| **Target Variable** | `Attrition` (Yes / No) |

---

### `manager_survey_data.csv` — Manager Assessments

Manager-reported evaluations on a 1–4 scale:

| Feature | Description |
|---------|-------------|
| `JobInvolvement` | Employee engagement level as observed by the manager |
| `PerformanceRating` | Manager's rating of the employee's performance |

---

### `employee_survey_data.csv` — Employee Satisfaction Survey

Self-reported satisfaction scores on a 1–4 scale:

| Feature | Description |
|---------|-------------|
| `EnvironmentSatisfaction` | Satisfaction with the physical and social work environment |
| `JobSatisfaction` | Satisfaction with the role and daily tasks |
| `WorkLifeBalance` | Perceived balance between work and personal life |

> ⚠️ **Note:** This dataset contains `NA` values representing missing or unanswered survey responses. These are handled during the preprocessing phase.

---

### `in_out_time.zip` — Working Hours Data

Contains daily check-in and check-out timestamps for each employee throughout **2015**. Used for feature engineering (e.g., average daily hours worked, overtime patterns, absenteeism indicators).

---

## Methodology

The analysis follows a structured data science pipeline:

```
1. Data Loading & Exploration
        ↓
2. Data Preprocessing
   - Missing value imputation
   - Categorical encoding
   - Outlier detection
        ↓
3. Exploratory Data Analysis (EDA)
   - Attrition distribution
   - Correlation analysis
   - Department and role-level breakdowns
        ↓
4. Feature Engineering
   - Derived features from in/out timestamps
   - Overtime flags, average hours, absenteeism rate
        ↓
5. Model Development
   - Multiple classification algorithms trained and compared
        ↓
6. Model Evaluation
   - Cross-validation, confusion matrices, ROC curves
        ↓
7. Model Interpretation
   - SHAP values for global and local explainability
        ↓
8. Recommendations
   - Actionable HR insights based on findings
```

---

## Models & Evaluation

The following classification models were trained and benchmarked:

| Model | Description |
|-------|-------------|
| Logistic Regression | Baseline linear classifier |
| Random Forest | Ensemble of decision trees, robust to overfitting |
| Gradient Boosting | Boosted ensemble for high predictive performance |
| Support Vector Machine | Effective in high-dimensional spaces |
| XGBoost | Optimized gradient boosting for tabular data |

All models were evaluated using stratified cross-validation to account for class imbalance (the dataset is naturally imbalanced since attrition events are the minority class).

---

## Key Metrics

| Metric | Purpose |
|--------|---------|
| **Accuracy** | Overall proportion of correct predictions |
| **Precision** | Of predicted attritions, how many are correct |
| **Recall** | Of actual attritions, how many were caught |
| **F1-Score** | Harmonic mean of precision and recall |
| **ROC-AUC** | Model's ability to discriminate between classes |
| **Feature Importance** | Which features drive the model's decisions |

> Given the business context, **Recall** is prioritized — missing an at-risk employee is more costly than a false positive.

---

## Deliverables

| # | Deliverable | Description |
|---|-------------|-------------|
| 1 | **Jupyter Notebook** | Full analysis pipeline with code, visualizations, and commentary |
| 2 | **Ethics Document** | Data governance, bias considerations, and responsible AI methodology |
| 3 | **Bibliography** | Academic papers and technical references used throughout the project |
| 4 | **Presentation** | 20-minute presentation of findings and recommendations for HR stakeholders |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/humanforyou-turnover.git
cd humanforyou-turnover
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

1. Place all data files in the `data/` directory (see [Datasets](#datasets) for expected filenames)

2. Launch the Jupyter notebook:

```bash
jupyter notebook notebooks/employee_turnover_analysis.ipynb
```

3. Run all cells in order — the notebook is self-contained and annotated at each step.

---

## Ethics & Compliance

This project involves personal employee data and predictive modeling that could influence HR decisions. The following principles were applied throughout:

- **Data minimization** — only features relevant to the analysis were used
- **Fairness** — demographic variables (gender, age, marital status) were monitored for bias in model outputs
- **Transparency** — SHAP values are used to ensure model decisions are explainable and auditable
- **No automated decision-making** — model outputs are intended to **support** HR decisions, not replace human judgment

Full details are documented in [`reports/ethics_document.md`](reports/ethics_document.md).

---

## Authors

This project was developed by:

| Name | Role |
|------|------|
| **Manil Doudou** | Data Analysis & Modeling |
| **Maxime Moysset** | Data Analysis & Modeling |
| **Vanessa Cheptumo** | Data Analysis & Modeling |
| **Allexia Munene** | Data Analysis & Modeling |

---

## License

MIT License

Copyright (c) 2026 Manil Doudou, Maxime Moysset, Vanessa Cheptumo, Allexia Munene

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
