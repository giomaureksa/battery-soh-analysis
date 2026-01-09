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