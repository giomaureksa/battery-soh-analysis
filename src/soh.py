import pandas as pd


def compute_bol_capacity(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute Beginning-of-Life (BOL) capacity.
    """
    return (
        df.groupby("cell_id", as_index=False)
        .first()[["cell_id", "discharge_capacity_ah"]]
        .rename(columns={"discharge_capacity_ah": "bol_capacity_ah"})
    )


def compute_soh(df: pd.DataFrame, bol_df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute State of Health (SOH).
    """
    df = df.merge(bol_df, on="cell_id", how="left")
    df["soh"] = df["discharge_capacity_ah"] / df["bol_capacity_ah"]
    return df


def compute_soh_delta(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute SOH degradation delta between cycles.
    """
    df = df.copy()
    df["soh_delta"] = (
        df.groupby("cell_id")["soh"]
        .diff()
        .fillna(0)
    )
    return df


def flag_eol(df: pd.DataFrame, threshold: float = 0.8) -> pd.DataFrame:
    """
    Flag End-of-Life (EOL) condition.
    """
    df = df.copy()
    df["below_eol"] = df["soh"] < threshold
    return df
