import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('student_grades.csv')

# Convert to numeric
df['Calculus'] = pd.to_numeric(df['Calculus'], errors='coerce')

# Check for negative values BEFORE
print("Negative values BEFORE:")
print(df[df['Calculus'] < 0]['Calculus'])

# Apply fix
df.loc[df['Calculus'] < 0, 'Calculus'] = 75

# Check for negative values AFTER
print("\nNegative values AFTER:")
print(df[df['Calculus'] < 0]['Calculus'])

# Verify if they are 75 now
print("\nDid they become 75?")
print(df[df['Calculus'] == 75]['Calculus'])
