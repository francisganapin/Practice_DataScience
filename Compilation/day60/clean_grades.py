import pandas as pd

# Path to the CSV file
file_path = 'student_grades.csv'

# Load the data
try:
    df = pd.read_csv(file_path)
    print("Data loaded successfully!")
    
    # Display the first few rows
    print("\nFirst 5 rows:")
    print(df.head())
    
    # Display info
    print("\nDataFrame Info:")
    print(df.info())
    
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
