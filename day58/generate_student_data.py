import pandas as pd
import numpy as np
import random
import os

# Set seed for reproducibility
np.random.seed(101)

# Generate 200 students
n_students = 200

# Student IDs
student_ids = range(1001, 1001 + n_students)

# Study Hours (Normal distribution, mean=10, std=5)
# Clip to ensure no negative hours or unrealistic high numbers
study_hours = np.random.normal(10, 5, n_students)
study_hours = np.clip(study_hours, 0, 40).round(1)

# Attendance Rate (Skewed towards high attendance)
attendance = np.random.normal(85, 15, n_students)
attendance = np.clip(attendance, 50, 100).round(1)

# Part Time Job (0 = No, 1 = Yes)
has_job = np.random.choice(['No', 'Yes'], n_students, p=[0.7, 0.3])

# Calculate Scores based on study hours and attendance + noise
# Base score 50
# + 1.5 per study hour
# + 0.2 per attendance point
# - 5 if has job
math_score = 40 + (study_hours * 1.5) + ((attendance - 50) * 0.5) + np.random.normal(0, 10, n_students)
math_score = np.clip(math_score, 0, 100).astype(int)

science_score = 45 + (study_hours * 1.2) + ((attendance - 50) * 0.4) + np.random.normal(0, 12, n_students)
science_score = np.clip(science_score, 0, 100).astype(int)

# English is less dependent on study hours, more random
english_score = np.random.normal(75, 15, n_students)
english_score = np.clip(english_score, 0, 100).astype(int)

# Create DataFrame
df = pd.DataFrame({
    'Student_ID': student_ids,
    'Study_Hours': study_hours,
    'Attendance_Pct': attendance,
    'Has_Part_Time_Job': has_job,
    'Math_Score': math_score,
    'Science_Score': science_score,
    'English_Score': english_score
})

# Introduce some "dirty" data for the lesson
# 1. Missing values in Study_Hours
df.loc[random.sample(range(n_students), 5), 'Study_Hours'] = np.nan

# 2. An impossible score (Data Entry Error)
df.loc[0, 'Math_Score'] = 150  # Impossible score

# Save to CSV
output_path = 'student_performance.csv'
df.to_csv(output_path, index=False)

print(f"Student data generated at: {os.path.abspath(output_path)}")
