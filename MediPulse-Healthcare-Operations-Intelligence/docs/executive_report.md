# MediPulse Executive Report

## Objective

MediPulse analyzes 55,500 healthcare encounters to understand hospital operations, patient demand, billing patterns, length of stay, and clinical test result signals.

## Key Business Questions

- Which conditions and hospitals drive the most volume?
- How do admissions trend over time?
- Which insurers contribute the most billing?
- What patient segments experience longer stays?
- Where are abnormal test results concentrated?
- Which records need billing data quality review?

## Methodology

1. Loaded raw encounter data from `data/raw/healthcare_dataset.csv`.
2. Standardized column names and text casing.
3. Converted admission and discharge fields into date values.
4. Created operational features such as length of stay, admission period, age group, stay category, emergency flag, abnormal result flag, and repeat visit proxy.
5. Flagged negative billing records for audit and set financial reporting values to zero.
6. Generated KPI tables, SQL queries, and visuals for dashboard development.

## Deliverables

- Cleaned dataset: `data/cleaned/healthcare_cleaned.csv`
- KPI summary: `data/cleaned/kpi_summary.csv`
- Condition summary: `data/cleaned/condition_summary.csv`
- Top hospital summary: `data/cleaned/hospital_summary_top25.csv`
- Monthly trend: `data/cleaned/monthly_trend.csv`
- Patient risk scoring: `data/cleaned/patient_risk_scores.csv`
- SQL analytics: `sql/`
- Power BI build guide: `powerbi/dashboard_spec.md`
- Static visuals: `images/`

## Data Quality Notes

The source dataset has no missing values. Negative billing values were present and are treated as data quality issues. Each affected record is marked with `negative_billing_flag`, and the cleaned reporting amount is clipped to zero to prevent negative revenue from distorting portfolio KPIs.

## Recommended Dashboard Narrative

Start with executive KPIs, then guide the viewer through demand patterns, operational load, financial contribution, and clinical test result signals. The strongest portfolio story is that this project connects patient flow, billing, and quality checks rather than stopping at basic descriptive charts.

## Predictive Analytics Bonus

The project includes an interpretable patient complexity score. Because the dataset does not include a labeled outcome such as readmission, mortality, or claim denial, the score is a transparent rules-based baseline rather than a supervised model. It combines age, length of stay, emergency admission, abnormal test results, and repeat visit proxy into low, medium, and high complexity segments.
