"""Simple predictive analytics features for portfolio storytelling."""

import numpy as np
import pandas as pd


def build_patient_risk_scores(df: pd.DataFrame) -> pd.DataFrame:
    """Create a transparent patient complexity risk score.

    This is an interpretable baseline rather than a trained model. It is useful
    for dashboard segmentation when a labeled outcome is not available.
    """
    scored = df.copy()

    age_component = np.select(
        [
            scored["age"] >= 75,
            scored["age"] >= 65,
            scored["age"] >= 50,
            scored["age"] < 18,
        ],
        [25, 18, 10, 8],
        default=4,
    )
    stay_component = np.select(
        [
            scored["length_of_stay"] >= 15,
            scored["length_of_stay"] >= 8,
            scored["length_of_stay"] >= 4,
        ],
        [25, 15, 8],
        default=2,
    )
    admission_component = np.where(scored["is_emergency"], 20, 5)
    test_component = np.where(scored["is_abnormal_result"], 20, 4)
    repeat_visit_component = np.where(scored["is_repeat_visit_proxy"], 10, 0)

    scored["patient_complexity_score"] = (
        age_component
        + stay_component
        + admission_component
        + test_component
        + repeat_visit_component
    ).clip(0, 100)

    scored["patient_complexity_segment"] = pd.cut(
        scored["patient_complexity_score"],
        bins=[-1, 35, 65, 100],
        labels=["Low", "Medium", "High"],
    )

    return scored[
        [
            "patient_name",
            "age",
            "age_group",
            "medical_condition",
            "admission_type",
            "length_of_stay",
            "test_results",
            "is_repeat_visit_proxy",
            "patient_complexity_score",
            "patient_complexity_segment",
        ]
    ].sort_values("patient_complexity_score", ascending=False)

