"""KPI calculations for healthcare operations reporting."""

import pandas as pd


def build_kpi_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return top-line KPIs in a tidy two-column table."""
    metrics = {
        "total_patients": df.shape[0],
        "unique_hospitals": df["hospital"].nunique(),
        "unique_doctors": df["doctor"].nunique(),
        "total_billing": df["billing_amount"].sum(),
        "average_billing": df["billing_amount"].mean(),
        "median_billing": df["billing_amount"].median(),
        "average_length_of_stay": df["length_of_stay"].mean(),
        "emergency_admission_rate": df["is_emergency"].mean(),
        "abnormal_test_rate": df["is_abnormal_result"].mean(),
        "repeat_visit_proxy_rate": df["is_repeat_visit_proxy"].mean(),
        "negative_billing_records": int(df["negative_billing_flag"].sum()),
    }

    return pd.DataFrame(
        [{"metric": metric, "value": value} for metric, value in metrics.items()]
    )


def condition_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize volume, billing, and stay length by condition."""
    return (
        df.groupby("medical_condition", observed=True)
        .agg(
            patients=("patient_name", "count"),
            total_billing=("billing_amount", "sum"),
            average_billing=("billing_amount", "mean"),
            average_length_of_stay=("length_of_stay", "mean"),
            emergency_rate=("is_emergency", "mean"),
            abnormal_test_rate=("is_abnormal_result", "mean"),
        )
        .reset_index()
        .sort_values("patients", ascending=False)
    )


def hospital_summary(df: pd.DataFrame, top_n: int = 25) -> pd.DataFrame:
    """Summarize the largest hospitals by patient volume."""
    summary = (
        df.groupby("hospital", observed=True)
        .agg(
            patients=("patient_name", "count"),
            total_billing=("billing_amount", "sum"),
            average_billing=("billing_amount", "mean"),
            average_length_of_stay=("length_of_stay", "mean"),
            emergency_rate=("is_emergency", "mean"),
        )
        .reset_index()
        .sort_values(["patients", "total_billing"], ascending=False)
    )

    return summary.head(top_n)


def monthly_trend(df: pd.DataFrame) -> pd.DataFrame:
    """Create a month-level admissions and billing trend."""
    trend = (
        df.set_index("admission_date")
        .resample("MS")
        .agg(
            admissions=("patient_name", "count"),
            total_billing=("billing_amount", "sum"),
            average_length_of_stay=("length_of_stay", "mean"),
            abnormal_test_rate=("is_abnormal_result", "mean"),
        )
        .reset_index()
    )
    trend["admission_month"] = trend["admission_date"].dt.strftime("%Y-%m")

    return trend

