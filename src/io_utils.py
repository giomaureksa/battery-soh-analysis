from pathlib import Path
import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    """
    Load CSV file into pandas DataFrame.

    Parameters
    ----------
    path : str or Path
        Path to CSV file

    Returns
    -------
    pd.DataFrame
    """
    return pd.read_csv(path)


def save_csv(df: pd.DataFrame, path: str | Path) -> None:
    """
    Save DataFrame to CSV.

    Parameters
    ----------
    df : pd.DataFrame
    path : str or Path
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
