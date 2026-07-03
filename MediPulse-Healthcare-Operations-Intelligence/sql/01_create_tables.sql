-- MediPulse schema for cleaned healthcare operations data.
-- Designed for PostgreSQL, SQL Server, MySQL, or SQLite with minor type edits.

CREATE TABLE healthcare_records (
    patient_name VARCHAR(255),
    age INTEGER,
    gender VARCHAR(20),
    blood_type VARCHAR(5),
    medical_condition VARCHAR(100),
    admission_date DATE,
    doctor VARCHAR(255),
    hospital VARCHAR(255),
    insurance_provider VARCHAR(100),
    billing_amount DECIMAL(12, 2),
    room_number INTEGER,
    admission_type VARCHAR(50),
    discharge_date DATE,
    medication VARCHAR(100),
    test_results VARCHAR(50),
    negative_billing_flag BOOLEAN,
    length_of_stay INTEGER,
    admission_year INTEGER,
    admission_month INTEGER,
    admission_month_name VARCHAR(3),
    admission_quarter VARCHAR(2),
    admission_weekday VARCHAR(20),
    age_group VARCHAR(10),
    stay_category VARCHAR(20),
    billing_per_day DECIMAL(12, 2),
    is_emergency BOOLEAN,
    is_abnormal_result BOOLEAN,
    readmission_proxy_key VARCHAR(600),
    patient_visit_sequence INTEGER,
    is_repeat_visit_proxy BOOLEAN
);

