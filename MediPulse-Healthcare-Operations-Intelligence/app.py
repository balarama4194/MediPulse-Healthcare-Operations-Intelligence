"""Lightweight command-line summary for the MediPulse project."""

from src.kpis import build_kpi_summary
from src.load_data import load_healthcare_data
from src.data_processing import prepare_healthcare_data


def main() -> None:
    """Print a quick portfolio summary without generating files."""
    healthcare_df = prepare_healthcare_data(load_healthcare_data())
    kpis = build_kpi_summary(healthcare_df)

    print("\nMediPulse - Healthcare Operations Intelligence\n")
    for _, row in kpis.iterrows():
        metric = row["metric"].replace("_", " ").title()
        value = row["value"]
        if row["metric"].endswith("_records") or row["metric"] in {
            "total_patients",
            "unique_hospitals",
            "unique_doctors",
        }:
            print(f"{metric}: {value:,.0f}")
        elif "billing" in row["metric"]:
            print(f"{metric}: ${value:,.2f}")
        elif "rate" in row["metric"]:
            print(f"{metric}: {value:.2%}")
        else:
            print(f"{metric}: {value:,.2f}" if isinstance(value, float) else f"{metric}: {value}")


if __name__ == "__main__":
    main()
