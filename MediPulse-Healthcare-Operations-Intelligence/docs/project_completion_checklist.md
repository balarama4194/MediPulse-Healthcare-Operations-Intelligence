# MediPulse Project Completion Checklist

Use this checklist before publishing the project to GitHub or sharing it in a portfolio.

## Python Pipeline

- [x] Raw dataset is stored in `data/raw/healthcare_dataset.csv`.
- [x] Reusable source modules are stored in `src/`.
- [x] `analysis.py` runs the full data pipeline.
- [x] Cleaned dataset is generated in `data/cleaned/`.
- [x] KPI tables are generated in `data/cleaned/`.
- [x] Static chart images are generated in `images/`.
- [x] Patient complexity scoring bonus output is generated.

## SQL

- [x] Table creation script exists in `sql/01_create_tables.sql`.
- [x] Business question queries exist in `sql/02_business_questions.sql`.
- [x] Queries cover KPIs, conditions, hospitals, monthly trends, insurers, clinical signals, and billing quality review.

## Power BI

- [x] Cleaned CSV is ready for import.
- [x] Dashboard specification exists in `powerbi/dashboard_spec.md`.
- [x] Step-by-step Power BI PDF guide exists in `output/pdf/`.
- [ ] Power BI `.pbix` file saved in `powerbi/`.
- [ ] Dashboard screenshots exported to `images/`.
- [ ] README updated with dashboard screenshots after Power BI build.

## Documentation

- [x] README explains the project, KPIs, outputs, and how to run it.
- [x] Executive report exists in `docs/executive_report.md`.
- [x] Presentation script exists in `docs/presentation_script.md`.

## Final Portfolio Steps

1. Build the Power BI dashboard using the PDF guide.
2. Save the file as `powerbi/MediPulse_Healthcare_Operations_Dashboard.pbix`.
3. Export screenshots from Power BI.
4. Add dashboard screenshots to the README under the Power BI section.
5. Publish the repository to GitHub.

