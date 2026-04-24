"""
Quick script to run the employee turnover analysis and see results.
This script executes the key parts of the notebook to test the models.
"""

import sys
import os
sys.path.append('src')

# Import necessary libraries
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

from data_loader import (
    load_general_data, load_manager_survey, load_employee_survey,
    load_working_hours_data, merge_all_data
)
from preprocessing import (
    handle_missing_values, encode_categorical_variables,
    create_features, prepare_features_for_modeling, scale_features
)
from model_evaluation import (
    evaluate_model, plot_confusion_matrix, plot_roc_curve,
    compare_models, print_classification_report
)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from imblearn.over_sampling import SMOTE
import xgboost as xgb
import lightgbm as lgb

print("="*60)
print("HUMANFORYOU EMPLOYEE TURNOVER ANALYSIS")
print("="*60)

# Step 1: Load data
print("\n[1/7] Loading data...")
try:
    general_df = load_general_data('data/general_data.csv')
    manager_df = load_manager_survey('data/manager_survey_data.csv')
    employee_df = load_employee_survey('data/employee_survey_data.csv')
    
    # Load working hours
    in_time_df, out_time_df = load_working_hours_data(
        zip_path='data/in_out_time.zip',
        in_time_path='data/in_time.csv',
        out_time_path='data/out_time.csv'
    )
    
    has_working_hours = (in_time_df is not None and out_time_df is not None)
    print(f"[OK] Data loaded successfully! Working hours: {has_working_hours}")
except Exception as e:
    print(f"[ERROR] Error loading data: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Step 2: Merge data
print("\n[2/7] Merging data...")
try:
    if has_working_hours:
        df = merge_all_data(general_df, manager_df, employee_df, in_time_df, out_time_df)
    else:
        df = merge_all_data(general_df, manager_df, employee_df)
    print(f"[OK] Merged dataset: {df.shape}")
except Exception as e:
    print(f"[ERROR] Error merging data: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Step 3: Preprocessing
print("\n[3/7] Preprocessing data...")
try:
    df_clean = handle_missing_values(df, strategy='median')
    df_features = create_features(df_clean)
    df_encoded, encoders = encode_categorical_variables(df_features, target_col='Attrition')
    X, y = prepare_features_for_modeling(df_encoded, target_col='Attrition')
    print(f"[OK] Preprocessing complete! Features: {X.shape[1]}, Samples: {X.shape[0]}")
    print(f"  Attrition rate: {(y == 1).sum() / len(y) * 100:.2f}%")
except Exception as e:
    print(f"[ERROR] Error in preprocessing: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Step 4: Train-test split
print("\n[4/7] Splitting data...")
try:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Handle class imbalance
    smote = SMOTE(random_state=42)
    X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)
    
    # Scale features
    X_train_scaled, X_test_scaled, scaler = scale_features(
        pd.DataFrame(X_train_balanced, columns=X.columns),
        pd.DataFrame(X_test, columns=X.columns)
    )
    X_train_unscaled = X_train_balanced
    X_test_unscaled = X_test.values
    
    print(f"[OK] Data split complete!")
    print(f"  Training: {X_train_balanced.shape[0]} samples")
    print(f"  Test: {X_test.shape[0]} samples")
except Exception as e:
    print(f"[ERROR] Error in data splitting: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Step 5: Train models
print("\n[5/7] Training models...")
models = {
    'Logistic Regression': (LogisticRegression(random_state=42, max_iter=1000), True),
    'Random Forest': (RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1), False),
    'Gradient Boosting': (GradientBoostingClassifier(random_state=42), False),
    'XGBoost': (xgb.XGBClassifier(random_state=42, eval_metric='logloss'), False),
    'LightGBM': (lgb.LGBMClassifier(random_state=42, verbose=-1), False),
    'SVM': (SVC(probability=True, random_state=42), True),
    'KNN': (KNeighborsClassifier(n_neighbors=5), True)
}

results = []
trained_models = {}

for name, (model, use_scaled) in models.items():
    try:
        print(f"  Training {name}...", end=' ')
        X_train_model = X_train_scaled if use_scaled else X_train_unscaled
        X_test_model = X_test_scaled if use_scaled else X_test_unscaled
        
        model.fit(X_train_model, y_train_balanced)
        trained_models[name] = model
        
        y_pred = model.predict(X_test_model)
        y_pred_proba = model.predict_proba(X_test_model)[:, 1]
        
        metrics = evaluate_model(y_test, y_pred, y_pred_proba, model_name=name)
        results.append(metrics)
        
        print(f"[OK] (AUC: {metrics['ROC-AUC']:.4f})")
    except Exception as e:
        print(f"[ERROR] Error: {e}")

# Step 6: Compare results
print("\n[6/7] Model Comparison Results:")
print("="*60)
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('ROC-AUC', ascending=False)

print("\n" + results_df.to_string(index=False))
print("\n" + "="*60)

# Step 7: Best model details
print("\n[7/7] Best Model Analysis:")
best_model_name = results_df.iloc[0]['Model']
best_model = trained_models[best_model_name]
use_scaled = best_model_name in ['Logistic Regression', 'SVM', 'KNN']
X_test_model = X_test_scaled if use_scaled else X_test_unscaled

y_pred_best = best_model.predict(X_test_model)
y_pred_proba_best = best_model.predict_proba(X_test_model)[:, 1]

print(f"\nBest Model: {best_model_name}")
print_classification_report(y_test, y_pred_best, model_name=best_model_name)

# Feature importance
if hasattr(best_model, 'feature_importances_'):
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': best_model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    print("\nTop 10 Most Important Features:")
    print(feature_importance.head(10).to_string(index=False))

print("\n" + "="*60)
print("ANALYSIS COMPLETE!")
print("="*60)
print(f"\nBest Model: {best_model_name}")
print(f"ROC-AUC: {results_df.iloc[0]['ROC-AUC']:.4f}")
print(f"Accuracy: {results_df.iloc[0]['Accuracy']:.4f}")
print(f"F1-Score: {results_df.iloc[0]['F1-Score']:.4f}")

