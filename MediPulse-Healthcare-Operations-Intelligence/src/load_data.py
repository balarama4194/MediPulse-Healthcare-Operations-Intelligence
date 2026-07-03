"""Data loading utilities for the MediPulse project."""

from pathlib import Path

import pandas as pd

from src.config import RAW_DATA_PATH


def load_healthcare_data(path: str | Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Load the raw healthcare dataset.

    Args:
        path: CSV file location.

    Returns:
        Raw healthcare records as a pandas DataFrame.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    return pd.read_csv(path)

