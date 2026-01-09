import numpy as np
import pandas as pd


def validate_schema(df: pd.DataFrame, required_cols: set) -> None:
    """
    Validate required columns exist.
    """
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def sort_timeseries(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sort data by cell, checkup, and time.
    """
    return (
        df.sort_values(["cell_id", "checkup_num", "time_s"])
        .reset_index(drop=True)
    )


def assign_test_phase(df: pd.DataFrame) -> pd.DataFrame:
    """
    Assign charge/discharge phase based on current sign.
    """
    df = df.copy()
    df["test_phase"] = np.where(df["current_a"] < 0, "discharge", "charge")
    return df
