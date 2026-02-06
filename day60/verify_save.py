import pandas as pd
import os

# 1. Load Data
df = pd.read_csv('student_grades.csv')

# 2. Fix Data
df['Calculus'] = pd.to_numeric(df['Calculus'], errors='coerce')
df.loc[df['Calculus'] < 0, 'Calculus'] = 75

# 3. Save Data
output_file = 'cleaned_student_grades.csv'
if os.path.exists(output_file):
    os.remove(output_file) # Ensure we are creating a new one
    
df.to_csv(output_file, index=False)

# 4. Load Saved Data to Verify
df_saved = pd.read_csv(output_file)
print("Negative values in SAVED file:")
print(df_saved[df_saved['Calculus'] < 0]['Calculus'])

print("\nValues equal to 75 in SAVED file:")
print(df_saved[df_saved['Calculus'] == 75]['Calculus'])
