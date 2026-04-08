import pandas as pd
import numpy as np

# 1. Load the Data
file_path = 'student_grades.csv'
df = pd.read_csv(file_path)

print("--- Original Data Info ---")
print(df.info())
print("\n--- First 5 Rows ---")
print(df.head())

# 2. Handle Missing Values
# Replace "missing" and "N/A" strings with actual NaN values
df = df.replace(["missing", "N/A"], np.nan)

# 3. Fix Data Types
# Convert subject columns to numeric, coercing errors to NaN
subject_cols = ['Calculus', 'Physics', 'Programming', 'Ethics']
for col in subject_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Now we can fill missing values (e.g., with 0 or the mean)
# Here we'll fill with 0 for simplicity, assuming missing means no submission
df[subject_cols] = df[subject_cols].fillna(0)

# 4. Clean Text (Sections)
# Standardize section names to uppercase
df['Section'] = df['Section'].str.upper()

# 5. Remove Duplicates
initial_rows = len(df)
df = df.drop_duplicates()
print(f"\nRemoved {initial_rows - len(df)} duplicate rows.")

# 6. Handle Outliers
# Clip grades to be between 0 and 100
df[subject_cols] = df[subject_cols].clip(lower=0, upper=100)

# 7. Analysis (Bonus)
# Calculate Average
df['Average'] = df[subject_cols].mean(axis=1)

# Find Section with highest average
section_avg = df.groupby('Section')['Average'].mean().sort_values(ascending=False)

print("\n--- Cleaned Data Info ---")
print(df.info())
print("\n--- Top 5 Students by Average ---")
print(df.sort_values('Average', ascending=False).head())

print("\n--- Average Grade by Section ---")
print(section_avg)

# 8. Save Cleaned Data
df.to_csv('cleaned_student_grades.csv', index=False)
print("\nSaved cleaned data to 'cleaned_student_grades.csv'")
