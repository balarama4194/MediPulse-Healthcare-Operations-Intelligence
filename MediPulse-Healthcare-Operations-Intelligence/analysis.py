"""Run the MediPulse healthcare operations analytics pipeline."""

from src.config import CLEANED_DATA_PATH, DATA_CLEANED_DIR, IMAGES_DIR, KPI_OUTPUT_PATH
from src.kpis import build_kpi_summary, condition_summary, hospital_summary, monthly_trend
from src.load_data import load_healthcare_data
from src.data_processing import prepare_healthcare_data
from src.predictive import build_patient_risk_scores
try:
    from src.visualization import (
        plot_admissions_by_condition,
        plot_billing_by_insurer,
        plot_length_of_stay_distribution,
        plot_monthly_admissions,
    )
except ModuleNotFoundError as exc:
    if exc.name != "matplotlib":
        raise
    plot_admissions_by_condition = None
    plot_billing_by_insurer = None
    plot_length_of_stay_distribution = None
    plot_monthly_admissions = None


def main() -> None:
    """Create cleaned data, KPI tables, and static charts."""
    DATA_CLEANED_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    raw_df = load_healthcare_data()
    healthcare_df = prepare_healthcare_data(raw_df)

    healthcare_df.to_csv(CLEANED_DATA_PATH, index=False)

    kpi_summary = build_kpi_summary(healthcare_df)
    conditions = condition_summary(healthcare_df)
    hospitals = hospital_summary(healthcare_df)
    trend = monthly_trend(healthcare_df)
    risk_scores = build_patient_risk_scores(healthcare_df)

    kpi_summary.to_csv(KPI_OUTPUT_PATH, index=False)
    conditions.to_csv(DATA_CLEANED_DIR / "condition_summary.csv", index=False)
    hospitals.to_csv(DATA_CLEANED_DIR / "hospital_summary_top25.csv", index=False)
    trend.to_csv(DATA_CLEANED_DIR / "monthly_trend.csv", index=False)
    risk_scores.to_csv(DATA_CLEANED_DIR / "patient_risk_scores.csv", index=False)

    if plot_admissions_by_condition is not None:
        plot_admissions_by_condition(
            healthcare_df, IMAGES_DIR / "admissions_by_condition.png"
        )
        plot_monthly_admissions(trend, IMAGES_DIR / "monthly_admission_trend.png")
        plot_billing_by_insurer(healthcare_df, IMAGES_DIR / "billing_by_insurer.png")
        plot_length_of_stay_distribution(
            healthcare_df, IMAGES_DIR / "length_of_stay_distribution.png"
        )
    else:
        print("Matplotlib is not installed; skipped chart generation.")

    print("MediPulse analytics pipeline completed.")
    print(f"Cleaned data: {CLEANED_DATA_PATH}")
    print(f"KPI summary: {KPI_OUTPUT_PATH}")
    print(f"Images: {IMAGES_DIR}")


if __name__ == "__main__":
    main()
