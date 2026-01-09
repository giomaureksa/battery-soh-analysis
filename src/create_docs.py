"""
create_docs.py

This script initializes the documentation structure for a
research-grade / industry-grade machine learning repository.

IMPORTANT:
- This script does NOT generate results
- This script does NOT touch datasets
- This script only creates narrative documentation files

Author: Gio Maureksa Nugraha
"""

from pathlib import Path

# Base documentation directory
DOCS_DIR = Path("../docs")

# Documentation files to be created
DOC_FILES = {
    "project_overview.md": """
# Project Overview

This project focuses on battery State of Health (SOH) estimation
using machine learning techniques.

The repository intentionally does NOT include datasets or trained
models due to data usage and redistribution policies.

All experiments are reproducible by following the instructions
provided in this documentation.
""",

    "methodology.md": """
# Methodology

This document describes the overall methodology used in this project,
including data preprocessing, feature engineering, and model training.

The focus is on reproducibility and transparency rather than
result sharing.
""",

    "model_information.md": """
# Trained Models Information

## Model Files
All trained models are saved in pickle format for easy deployment.

### Linear Regression Model
- **File**: linear_regression_model.pkl
- **Type**: sklearn.linear_model.LinearRegression
- **Parameters**: fit_intercept=True
- **Performance**: R-squared = 0.9214

### Random Forest Model
- **File**: random_forest_model.pkl
- **Type**: sklearn.ensemble.RandomForestRegressor
- **Parameters**: n_estimators=300, max_depth=5
- **Performance**: R-squared = 0.9572

### XGBoost Model
- **File**: xgboost_model.pkl
- **Type**: xgboost.XGBRegressor
- **Parameters**: n_estimators=300, max_depth=3, learning_rate=0.05
- **Performance**: R-squared = 0.9999

## Model Usage

```python
import pickle
import numpy as np

# Load model
with open('xgboost_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Make prediction
checkup_number = 15
prediction = model.predict(np.array([[checkup_number]]))
print(f"Predicted SOH: {prediction[0]:.4f}")
```
""",

    "evaluation_strategy.md": """
# Evaluation Strategy

Model performance is evaluated using standard regression metrics such as:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)

Exact numerical results are not published to comply with dataset
usage policies.
""",

    "ethical_and_data_usage.md": """
# Ethical and Data Usage Considerations

The dataset used in this project is sourced from IEEE DataPort.

To respect data usage policies and ethical research practices:
- Raw data is not redistributed
- Processed data is not published
- Derived datasets are excluded

Users are expected to obtain the dataset directly from the original source.
""",

    "limitations.md": """
# Limitations

This project focuses on methodological demonstration rather than
benchmark dominance.

Results may vary depending on:
- Dataset version
- Feature extraction choices
- Hyperparameter configurations
"""
}

def create_docs():
    """Create documentation directory and markdown files."""
    DOCS_DIR.mkdir(exist_ok=True)

    for filename, content in DOC_FILES.items():
        file_path = DOCS_DIR / filename
        file_path.write_text(content.strip(), encoding="utf-8")

    print("Documentation structure successfully created.")

if __name__ == "__main__":
    create_docs()
