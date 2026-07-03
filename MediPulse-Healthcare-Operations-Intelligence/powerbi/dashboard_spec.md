# Power BI Dashboard Specification

## Data Source

Use `data/cleaned/healthcare_cleaned.csv` after running:

```powershell
python analysis.py
```

If your system does not expose `python`, run the script with your local Python installation or open it from an IDE.

## Recommended Pages

### 1. Executive Overview

Cards:
- Total Admissions
- Total Billing
- Average Billing
- Average Length of Stay
- Emergency Admission Rate
- Abnormal Test Rate

Visuals:
- Monthly admissions line chart
- Admissions by medical condition bar chart
- Billing by insurance provider bar chart
- Admission type donut chart

Slicers:
- Admission Year
- Medical Condition
- Insurance Provider
- Admission Type

### 2. Operations

Visuals:
- Average length of stay by condition
- Top 25 hospitals by admissions
- Admissions by weekday
- Stay category distribution

### 3. Financial Performance

Visuals:
- Total billing by insurer
- Average billing by condition
- Billing per day by age group
- Billing quality review table filtered by `negative_billing_flag`

### 4. Clinical Signals

Visuals:
- Abnormal test rate by condition
- Abnormal test rate by admission type
- Medication distribution
- Age group by condition matrix

## DAX Measures

```DAX
Total Admissions = COUNTROWS(healthcare_cleaned)

Total Billing = SUM(healthcare_cleaned[billing_amount])

Average Billing = AVERAGE(healthcare_cleaned[billing_amount])

Average Length of Stay = AVERAGE(healthcare_cleaned[length_of_stay])

Emergency Admissions =
CALCULATE(
    COUNTROWS(healthcare_cleaned),
    healthcare_cleaned[is_emergency] = TRUE()
)

Emergency Admission Rate =
DIVIDE([Emergency Admissions], [Total Admissions])

Abnormal Results =
CALCULATE(
    COUNTROWS(healthcare_cleaned),
    healthcare_cleaned[is_abnormal_result] = TRUE()
)

Abnormal Test Rate =
DIVIDE([Abnormal Results], [Total Admissions])

Repeat Visit Proxy Rate =
DIVIDE(
    CALCULATE(
        COUNTROWS(healthcare_cleaned),
        healthcare_cleaned[is_repeat_visit_proxy] = TRUE()
    ),
    [Total Admissions]
)
```

## Design Notes

Use a restrained healthcare operations palette: blue for volume, green for operational health, orange for financial signals, and red only for review flags. Keep slicers at the top or left side of each report page so the dashboard feels consistent.

