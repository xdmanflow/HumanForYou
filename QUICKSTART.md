# Quick Start Guide
## HumanForYou Employee Turnover Analysis

This guide will help you get started with the project quickly.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Jupyter Notebook (will be installed via requirements)

## Setup Steps

### 1. Clone or Navigate to Project Directory

```bash
cd "C:\Users\manil\Desktop\Studies\AI\Project of AI"
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Place Data Files

Place the following files in the `data/` directory:
- `general_data.csv`
- `manager_survey_data.csv`
- `employee_survey_data.csv`
- `in_out_time.zip`

### 5. Launch Jupyter Notebook

```bash
jupyter notebook
```

### 6. Open the Analysis Notebook

Navigate to `notebooks/employee_turnover_analysis.ipynb` and run all cells.

## Project Structure

```
.
├── data/                          # Data files (place CSV and ZIP here)
├── notebooks/                     # Jupyter notebooks
│   └── employee_turnover_analysis.ipynb
├── src/                          # Python modules
│   ├── data_loader.py
│   ├── preprocessing.py
│   └── model_evaluation.py
├── reports/                      # Reports and documents
│   ├── ethics_document.md
│   ├── bibliography.md
│   └── presentation_outline.md
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── QUICKSTART.md                 # This file
```

## Running the Analysis

1. **Open Jupyter Notebook**: `notebooks/employee_turnover_analysis.ipynb`
2. **Run All Cells**: Use "Cell" → "Run All" or execute cells sequentially
3. **Review Results**: Check outputs, visualizations, and model performance
4. **Review Reports**: Check `reports/` folder for ethics and bibliography documents

## Troubleshooting

### Import Errors
- Ensure virtual environment is activated
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check that you're running from the project root directory

### Data Loading Errors
- Verify data files are in the `data/` directory
- Check file names match exactly (case-sensitive)
- Ensure CSV files are properly formatted

### Memory Issues
- Reduce sample size in SHAP analysis (already set to 100 samples)
- Use smaller parameter grids in hyperparameter tuning
- Process data in chunks if dataset is very large

### Model Training Takes Too Long
- Reduce number of models tested initially
- Use smaller parameter grids
- Reduce cross-validation folds (from 5 to 3)

## Next Steps

1. **Review the Notebook**: Understand each section
2. **Read Ethics Document**: `reports/ethics_document.md`
3. **Review Bibliography**: `reports/bibliography.md`
4. **Prepare Presentation**: Use `reports/presentation_outline.md` as guide
5. **Customize Analysis**: Modify code as needed for your specific requirements

## Getting Help

- Review the README.md for detailed documentation
- Check code comments in Python modules
- Review the Jupyter notebook markdown cells for explanations
- Consult the bibliography for theoretical foundations

## Notes

- The notebook is designed to be run sequentially
- Some cells may take several minutes to execute (model training)
- Results will vary slightly due to random seeds (set to 42 for reproducibility)
- Working hours data processing may take time depending on dataset size

---

