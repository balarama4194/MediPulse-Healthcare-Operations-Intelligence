"""Matplotlib chart builders for MediPulse."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def _save_current_figure(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=160, bbox_inches="tight")
    plt.close()


def plot_admissions_by_condition(df: pd.DataFrame, output_path: Path) -> None:
    """Save a bar chart of admissions by medical condition."""
    counts = df["medical_condition"].value_counts().sort_values()

    plt.figure(figsize=(9, 5))
    counts.plot(kind="barh", color="#2E86AB")
    plt.title("Admissions by Medical Condition")
    plt.xlabel("Admissions")
    plt.ylabel("Medical Condition")
    _save_current_figure(output_path)


def plot_monthly_admissions(trend: pd.DataFrame, output_path: Path) -> None:
    """Save a monthly admissions trend line."""
    plt.figure(figsize=(11, 5))
    plt.plot(trend["admission_date"], trend["admissions"], color="#33658A", linewidth=2)
    plt.title("Monthly Admission Trend")
    plt.xlabel("Admission Month")
    plt.ylabel("Admissions")
    plt.grid(axis="y", alpha=0.25)
    _save_current_figure(output_path)


def plot_billing_by_insurer(df: pd.DataFrame, output_path: Path) -> None:
    """Save total billing by insurance provider."""
    insurer_billing = (
        df.groupby("insurance_provider")["billing_amount"].sum().sort_values()
    )

    plt.figure(figsize=(9, 5))
    insurer_billing.plot(kind="barh", color="#F26419")
    plt.title("Total Billing by Insurance Provider")
    plt.xlabel("Billing Amount")
    plt.ylabel("Insurance Provider")
    _save_current_figure(output_path)


def plot_length_of_stay_distribution(df: pd.DataFrame, output_path: Path) -> None:
    """Save length-of-stay distribution."""
    plt.figure(figsize=(9, 5))
    plt.hist(df["length_of_stay"], bins=30, color="#6A994E", edgecolor="white")
    plt.title("Length of Stay Distribution")
    plt.xlabel("Days")
    plt.ylabel("Patient Records")
    _save_current_figure(output_path)

