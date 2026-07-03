"""Cleaning and feature engineering logic for MediPulse."""

import numpy as np
import pandas as pd

from src.config import COLUMN_RENAME_MAP


def clean_healthcare_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean raw healthcare records and standardize column names.

    The source file has no missing values, but it contains inconsistent text
    casing and a small number of negative billing amounts. Negative billing is
    retained as an audit flag, then set to zero for financial reporting.
    """
    cleaned = df.copy()
    cleaned.columns = cleaned.columns.str.strip()
    cleaned = cleaned.rename(columns=COLUMN_RENAME_MAP)

    text_columns = cleaned.select_dtypes(include="object").columns
    for column in text_columns:
        cleaned[column] = cleaned[column].astype(str).str.strip()

    proper_case_columns = ["patient_name", "doctor", "hospital"]
    for column in proper_case_columns:
        cleaned[column] = cleaned[column].str.title()

    category_columns = [
        "gender",
        "blood_type",
        "medical_condition",
        "insurance_provider",
        "admission_type",
        "medication",
        "test_results",
    ]
    for column in category_columns:
        cleaned[column] = cleaned[column].str.title()

    cleaned["admission_date"] = pd.to_datetime(cleaned["admission_date"])
    cleaned["discharge_date"] = pd.to_datetime(cleaned["discharge_date"])
    cleaned["billing_amount"] = pd.to_numeric(cleaned["billing_amount"], errors="coerce")
    cleaned["room_number"] = pd.to_numeric(cleaned["room_number"], errors="coerce").astype("Int64")
    cleaned["age"] = pd.to_numeric(cleaned["age"], errors="coerce").astype("Int64")

    cleaned["negative_billing_flag"] = cleaned["billing_amount"] < 0
    cleaned["billing_amount"] = cleaned["billing_amount"].clip(lower=0)

    return cleaned


def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add portfolio-ready operational, financial, and patient features."""
    featured = df.copy()

    featured["length_of_stay"] = (
        featured["discharge_date"] - featured["admission_date"]
    ).dt.days
    featured["length_of_stay"] = featured["length_of_stay"].clip(lower=0)

    featured["admission_year"] = featured["admission_date"].dt.year
    featured["admission_month"] = featured["admission_date"].dt.month
    featured["admission_month_name"] = featured["admission_date"].dt.strftime("%b")
    featured["admission_quarter"] = "Q" + featured["admission_date"].dt.quarter.astype(str)
    featured["admission_weekday"] = featured["admission_date"].dt.day_name()

    featured["age_group"] = pd.cut(
        featured["age"].astype(float),
        bins=[0, 17, 34, 49, 64, 120],
        labels=["0-17", "18-34", "35-49", "50-64", "65+"],
        right=True,
    )

    featured["stay_category"] = pd.cut(
        featured["length_of_stay"],
        bins=[-1, 3, 7, 14, np.inf],
        labels=["Short", "Standard", "Extended", "Long"],
    )

    featured["billing_per_day"] = np.where(
        featured["length_of_stay"] > 0,
        featured["billing_amount"] / featured["length_of_stay"],
        featured["billing_amount"],
    )

    featured["is_emergency"] = featured["admission_type"].eq("Emergency")
    featured["is_abnormal_result"] = featured["test_results"].eq("Abnormal")

    featured["readmission_proxy_key"] = (
        featured["patient_name"].str.lower()
        + "|"
        + featured["medical_condition"].str.lower()
    )
    featured["patient_visit_sequence"] = featured.groupby("readmission_proxy_key")[
        "admission_date"
    ].rank(method="first").astype(int)
    featured["is_repeat_visit_proxy"] = featured["patient_visit_sequence"] > 1

    return featured


def prepare_healthcare_data(df: pd.DataFrame) -> pd.DataFrame:
    """Run the full cleaning and feature engineering pipeline."""
    return add_engineered_features(clean_healthcare_data(df))

