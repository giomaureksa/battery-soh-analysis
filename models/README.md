# Trained Models

This directory contains trained SOH prediction models produced in Notebook 3.

## Models

- **linear_regression_soh.pkl**
  - Baseline linear model for SOH estimation
  - Used for interpretability and reference

- **random_forest_soh.pkl**
  - Nonlinear ensemble model
  - Improves accuracy over linear baseline

- **xgboost_soh.pkl**
  - Gradient boosting model
  - Achieved highest performance (R² ≈ 0.999)

## Notes
- Models are trained on discharge-cycle-level features
- Intended for research and comparison purposes only
- Not suitable for direct deployment in BMS systems
