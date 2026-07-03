"""Project paths and shared constants."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_RAW_DIR = PROJECT_ROOT / "data" / "raw"
DATA_CLEANED_DIR = PROJECT_ROOT / "data" / "cleaned"
DATA_EXTERNAL_DIR = PROJECT_ROOT / "data" / "external"
IMAGES_DIR = PROJECT_ROOT / "images"
DOCS_DIR = PROJECT_ROOT / "docs"
SQL_DIR = PROJECT_ROOT / "sql"
POWERBI_DIR = PROJECT_ROOT / "powerbi"

RAW_DATA_PATH = DATA_RAW_DIR / "healthcare_dataset.csv"
CLEANED_DATA_PATH = DATA_CLEANED_DIR / "healthcare_cleaned.csv"
KPI_OUTPUT_PATH = DATA_CLEANED_DIR / "kpi_summary.csv"

DATE_COLUMNS = ["Date of Admission", "Discharge Date"]

COLUMN_RENAME_MAP = {
    "Name": "patient_name",
    "Age": "age",
    "Gender": "gender",
    "Blood Type": "blood_type",
    "Medical Condition": "medical_condition",
    "Date of Admission": "admission_date",
    "Doctor": "doctor",
    "Hospital": "hospital",
    "Insurance Provider": "insurance_provider",
    "Billing Amount": "billing_amount",
    "Room Number": "room_number",
    "Admission Type": "admission_type",
    "Discharge Date": "discharge_date",
    "Medication": "medication",
    "Test Results": "test_results",
}

