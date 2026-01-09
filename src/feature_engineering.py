import pandas as pd


def compute_delta_time(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute time step per cycle.
    """
    df = df.copy()
    df["delta_t"] = (
        df.groupby(["cell_id", "checkup_num"])["time_s"]
        .diff()
        .fillna(0)
    )
    return df


def integrate_discharge_capacity(df: pd.DataFrame) -> pd.DataFrame:
    """
    Integrate discharge current to capacity (Ah).
    """
    df = df.copy()
    df["dQ_ah"] = df["current_a"].abs() * df["delta_t"] / 3600
    return df


def aggregate_discharge_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate discharge features at cycle level.
    """
    return (
        df.groupby(["cell_id", "checkup_num"], as_index=False)
        .agg(
            discharge_capacity_ah=("dQ_ah", "sum"),
            duration_s=("delta_t", "sum"),
            mean_current_a=("current_a", lambda x: x.abs().mean()),
            min_voltage_v=("voltage_v", "min"),
        )
    )
