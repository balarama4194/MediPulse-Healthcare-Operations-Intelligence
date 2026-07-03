-- 1. What are the top-line operational KPIs?
SELECT
    COUNT(*) AS total_admissions,
    COUNT(DISTINCT hospital) AS unique_hospitals,
    COUNT(DISTINCT doctor) AS unique_doctors,
    ROUND(SUM(billing_amount), 2) AS total_billing,
    ROUND(AVG(billing_amount), 2) AS average_billing,
    ROUND(AVG(length_of_stay), 2) AS average_length_of_stay,
    ROUND(AVG(CASE WHEN is_emergency THEN 1.0 ELSE 0.0 END), 4) AS emergency_rate,
    ROUND(AVG(CASE WHEN is_abnormal_result THEN 1.0 ELSE 0.0 END), 4) AS abnormal_test_rate
FROM healthcare_records;

-- 2. Which medical conditions drive the most admissions and billing?
SELECT
    medical_condition,
    COUNT(*) AS admissions,
    ROUND(SUM(billing_amount), 2) AS total_billing,
    ROUND(AVG(billing_amount), 2) AS average_billing,
    ROUND(AVG(length_of_stay), 2) AS average_length_of_stay
FROM healthcare_records
GROUP BY medical_condition
ORDER BY admissions DESC;

-- 3. Which hospitals have the highest volume?
SELECT
    hospital,
    COUNT(*) AS admissions,
    ROUND(SUM(billing_amount), 2) AS total_billing,
    ROUND(AVG(length_of_stay), 2) AS average_length_of_stay,
    ROUND(AVG(CASE WHEN is_emergency THEN 1.0 ELSE 0.0 END), 4) AS emergency_rate
FROM healthcare_records
GROUP BY hospital
ORDER BY admissions DESC, total_billing DESC
LIMIT 25;

-- 4. How do admissions trend over time?
SELECT
    admission_year,
    admission_month,
    COUNT(*) AS admissions,
    ROUND(SUM(billing_amount), 2) AS total_billing,
    ROUND(AVG(length_of_stay), 2) AS average_length_of_stay
FROM healthcare_records
GROUP BY admission_year, admission_month
ORDER BY admission_year, admission_month;

-- 5. Which insurers are associated with the most revenue?
SELECT
    insurance_provider,
    COUNT(*) AS admissions,
    ROUND(SUM(billing_amount), 2) AS total_billing,
    ROUND(AVG(billing_amount), 2) AS average_billing
FROM healthcare_records
GROUP BY insurance_provider
ORDER BY total_billing DESC;

-- 6. Where are abnormal test results concentrated?
SELECT
    medical_condition,
    admission_type,
    COUNT(*) AS admissions,
    SUM(CASE WHEN is_abnormal_result THEN 1 ELSE 0 END) AS abnormal_results,
    ROUND(AVG(CASE WHEN is_abnormal_result THEN 1.0 ELSE 0.0 END), 4) AS abnormal_rate
FROM healthcare_records
GROUP BY medical_condition, admission_type
ORDER BY abnormal_rate DESC, abnormal_results DESC;

-- 7. Which patient segments have longer stays?
SELECT
    age_group,
    medical_condition,
    COUNT(*) AS admissions,
    ROUND(AVG(length_of_stay), 2) AS average_length_of_stay,
    ROUND(AVG(billing_per_day), 2) AS average_billing_per_day
FROM healthcare_records
GROUP BY age_group, medical_condition
ORDER BY average_length_of_stay DESC;

-- 8. What records should be reviewed for billing data quality?
SELECT
    patient_name,
    hospital,
    insurance_provider,
    admission_date,
    billing_amount,
    negative_billing_flag
FROM healthcare_records
WHERE negative_billing_flag = TRUE
ORDER BY admission_date DESC;

