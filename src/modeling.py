from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor


def train_linear_regression(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model


def train_random_forest(X, y, random_state=42):
    model = RandomForestRegressor(
        n_estimators=300,
        max_depth=6,
        random_state=random_state
    )
    model.fit(X, y)
    return model


def train_xgboost(X, y, random_state=42):
    model = XGBRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=4,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=random_state
    )
    model.fit(X, y)
    return model
