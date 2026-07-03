"""Backward-compatible entry point for cleaning the healthcare dataset."""

from src.config import CLEANED_DATA_PATH
from src.load_data import load_healthcare_data
from src.data_processing import prepare_healthcare_data


def main() -> None:
    """Clean the raw dataset and save the reporting-ready CSV."""
    cleaned_df = prepare_healthcare_data(load_healthcare_data())
    CLEANED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    cleaned_df.to_csv(CLEANED_DATA_PATH, index=False)
    print(f"Cleaned dataset saved to {CLEANED_DATA_PATH}")


if __name__ == "__main__":
    main()

