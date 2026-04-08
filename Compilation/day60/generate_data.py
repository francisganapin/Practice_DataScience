import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Number of rows
n_rows = 200

# Generate Student IDs
student_ids = [f"2023-{str(i).zfill(4)}" for i in range(1, n_rows + 1)]

# Generate Names
first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "Chris", "Jessica", "Daniel", "Ashley", "James", "Mary", "Robert", "Patricia", "William", "Jennifer", "Joseph", "Linda", "Charles", "Elizabeth"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]

names = []
for _ in range(n_rows):
    names.append(f"{random.choice(first_names)} {random.choice(last_names)}")

# Generate Sections (with inconsistencies)
sections = np.random.choice(['A', 'B', 'C', 'D'], n_rows)
# Introduce inconsistencies
for i in range(0, n_rows, 20):
    sections[i] = sections[i].lower() # 'a', 'b', etc.

# Generate Grades (College Subjects)
def generate_grades(n, mean=85, std=10):
    grades = np.random.normal(mean, std, n)
    grades = np.round(grades).astype(object)
    return grades

calculus = generate_grades(n_rows)
physics = generate_grades(n_rows)
programming = generate_grades(n_rows)
ethics = generate_grades(n_rows)

# Introduce Anomalies

# 1. Missing Values
for col in [calculus, physics, programming, ethics]:
    # Set 5% to NaN
    mask = np.random.choice([True, False], size=n_rows, p=[0.05, 0.95])
    col[mask] = np.nan
    
    # Set 2% to "missing" or "N/A"
    mask_str = np.random.choice([True, False], size=n_rows, p=[0.02, 0.98])
    col[mask_str] = np.random.choice(["missing", "N/A"], size=mask_str.sum())

# 2. Outliers
# Set some grades to > 100 or < 0
outlier_indices = np.random.choice(n_rows, 5, replace=False)
calculus[outlier_indices] = [150, -10, 500, 105, -5]

# Create DataFrame
df = pd.DataFrame({
    'Student_ID': student_ids,
    'Name': names,
    'Section': sections,
    'Calculus': calculus,
    'Physics': physics,
    'Programming': programming,
    'Ethics': ethics
})

# 3. Duplicates
# Duplicate last 5 rows
df = pd.concat([df, df.tail(5)], ignore_index=True)

# Save to CSV
output_file = 'student_grades.csv'
df.to_csv(output_file, index=False)

print(f"Generated {len(df)} rows of data in '{output_file}'")
print(df.head())
print(df.tail())
