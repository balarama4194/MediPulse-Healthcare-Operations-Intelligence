# MediPulse Presentation Script

## 30-Second Summary

MediPulse is a healthcare operations analytics project built on 55,500 patient encounters. I cleaned and transformed the raw data using Python, created operational and financial KPIs, wrote SQL queries for business analysis, and designed a Power BI dashboard to track admissions, billing, length of stay, emergency demand, abnormal test results, and billing data quality.

## Problem Statement

Healthcare teams need a clear view of patient flow, operational load, billing patterns, and clinical result signals. Raw encounter data is difficult to use directly, so this project turns it into structured reporting data and dashboard-ready insights.

## My Approach

1. Loaded the raw healthcare dataset from CSV.
2. Cleaned text casing, standardized column names, and converted date fields.
3. Engineered features such as length of stay, admission period, age group, stay category, billing per day, emergency flag, abnormal test flag, and repeat visit proxy.
4. Flagged negative billing values as data quality issues and clipped them to zero for reporting.
5. Generated KPI tables, SQL analytics, visual charts, and Power BI dashboard guidance.
6. Added an interpretable patient complexity score as a predictive analytics bonus.

## Key Insights To Mention

- The dataset contains 55,500 patient encounters.
- Total cleaned billing is approximately $1.42B.
- Average billing is approximately $25.5K per encounter.
- Average length of stay is 15.51 days.
- Emergency admissions represent 32.92% of encounters.
- Abnormal test results appear in 33.56% of encounters.
- 108 records had negative billing values and were flagged for review.

## Dashboard Walkthrough

### Executive Overview

Start with total admissions, billing, average billing, average stay, emergency rate, and abnormal test rate. This gives leaders a quick operational snapshot.

### Operations

Show length of stay by condition, top hospitals by volume, admissions by weekday, and stay category distribution. This page is useful for capacity planning.

### Financial Performance

Show billing by insurer, average billing by condition, billing per day, and billing quality flags. This page connects operations with revenue performance.

### Clinical Signals

Show abnormal test rate by condition and admission type, medication distribution, and age group patterns. This page helps identify patient segments that may need closer review.

## Closing Statement

This project demonstrates the full data analyst workflow: data cleaning, feature engineering, KPI design, SQL analysis, dashboard planning, quality checks, and executive communication. It is designed to be understandable for business users while still showing strong technical execution.

