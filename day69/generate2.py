import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

# --- Config ---
num_students = 200
grade_levels = [7, 8, 9, 10, 11, 12]
sections = ["A", "B", "C", "D"]
subjects = ["Math", "Science", "English", "Filipino", "MAPEH"]
first_names = ["Juan", "Maria", "Pedro", "Ana", "Jose", "Rosa", "Carlos", "Elena",
               "Miguel", "Sofia", "Diego", "Isabella", "Marco", "Liza", "Rafael"]
last_names = ["Santos", "Reyes", "Cruz", "Garcia", "Torres", "Flores", "Rivera",
              "Ramos", "Lopez", "Gonzales", "Dela Cruz", "Villanueva", "Mendoza"]

# --- Generate Students ---
students = []
for i in range(1, num_students + 1):
    student_id = f"STU-{i:04d}"
    first = random.choice(first_names)
    last = random.choice(last_names)
    full_name = f"{first} {last}"
    grade = random.choice(grade_levels)
    section = random.choice(sections)

    # Normal age based on grade level (Grade 7 = ~12yo, Grade 12 = ~17yo)
    normal_age = grade + 5  # approximate
    birthdate = datetime(2025 - normal_age, random.randint(1, 12), random.randint(1, 28))

    # Normal grades (65-95 range)
    avg_grade = round(random.uniform(65, 95), 1)
    final_grade = round(avg_grade + random.uniform(-5, 5), 1)
    final_grade = min(max(final_grade, 60), 100)  # clamp to 60-100

    # Attendance (normal: 75%-98%)
    total_days = 200
    days_present = random.randint(150, 196)
    attendance_rate = round((days_present / total_days) * 100, 1)

    # Tuition (normal: ₱15,000 - ₱50,000)
    tuition_fee = round(random.uniform(15000, 50000), 2)
    amount_paid = round(tuition_fee * random.uniform(0.7, 1.0), 2)
    has_scholarship = random.choices([True, False], weights=[15, 85])[0]

    # Parent/Guardian
    has_guardian = True

    students.append({
        "student_id": student_id,
        "full_name": full_name,
        "birthdate": birthdate.strftime("%Y-%m-%d"),
        "age": normal_age,
        "grade_level": grade,
        "section": section,
        "avg_quarterly_grade": avg_grade,
        "final_grade": final_grade,
        "days_present": days_present,
        "total_days": total_days,
        "attendance_rate": attendance_rate,
        "tuition_fee": tuition_fee,
        "amount_paid": amount_paid,
        "has_scholarship": has_scholarship,
        "has_guardian": has_guardian,
    })

df = pd.DataFrame(students)

# ============================================
# 🚨 INJECT FRAUD (rows 180-200)
# ============================================
fraud_indices = list(range(179, 200))

for idx in fraud_indices:
    fraud_type = random.choice([
        "ghost", "duplicate", "grade_manip",
        "attendance_fraud", "financial", "age_anomaly"
    ])

    if fraud_type == "ghost":
        # Ghost student: has NO grades, NO attendance, but is enrolled
        df.at[idx, "avg_quarterly_grade"] = 0
        df.at[idx, "final_grade"] = 0
        df.at[idx, "days_present"] = 0
        df.at[idx, "attendance_rate"] = 0
        df.at[idx, "has_guardian"] = False

    elif fraud_type == "duplicate":
        # Copy data from another student (duplicate enrollment)
        source = random.randint(0, 150)
        df.at[idx, "full_name"] = df.at[source, "full_name"]
        df.at[idx, "birthdate"] = df.at[source, "birthdate"]
        # But keep different student_id (this is the fraud indicator!)

    elif fraud_type == "grade_manip":
        # Low quarterly average but suspiciously high final grade
        df.at[idx, "avg_quarterly_grade"] = round(random.uniform(50, 65), 1)
        df.at[idx, "final_grade"] = round(random.uniform(88, 99), 1)

    elif fraud_type == "attendance_fraud":
        # Perfect attendance but zero grades (impossible in reality)
        df.at[idx, "days_present"] = 200
        df.at[idx, "attendance_rate"] = 100.0
        df.at[idx, "avg_quarterly_grade"] = 0
        df.at[idx, "final_grade"] = 0

    elif fraud_type == "financial":
        # Paid ₱0 tuition with NO scholarship
        df.at[idx, "amount_paid"] = 0
        df.at[idx, "has_scholarship"] = False

    elif fraud_type == "age_anomaly":
        # Age doesn't match grade level at all
        df.at[idx, "age"] = random.choice([5, 6, 25, 30, 35])
        weird_year = 2025 - df.at[idx, "age"]
        df.at[idx, "birthdate"] = f"{weird_year}-06-15"

# --- Save both CSV and Excel ---
df.to_csv("school_students.csv", index=False)
df.to_excel("school_students.xlsx", index=False, sheet_name="Students")
print("✅ school_students.csv saved")
print("✅ school_students.xlsx saved")
print(f"Total students: {len(df)}")
print(f"Fraud injected: {len(fraud_indices)} rows (rows 180-200)")