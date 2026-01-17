import pandas as pd
import numpy as np

# Set random seed
np.random.seed(42)

# Employees
employee_ids = ['E0001', 'E0002', 'E0003', 'E0004']
records_per_employee = 25

# Total rows
n = len(employee_ids) * records_per_employee

# Generate repeated Employee_IDs
employee_column = np.repeat(employee_ids, records_per_employee)

# Generate synthetic data
df = pd.DataFrame({
    'Employee_ID': employee_column,  # day number 1-120 for each employee
    'coffee_cups': np.random.randint(6, 15, n),      # 0-7 cups/day
    'hours_worked': np.random.randint(6, 12, n),    # 6-11 hours/day
    'breaks': np.random.randint(0, 5, n),           # 0-4 breaks/day
})

# Performance influenced by hours worked and coffee
df['performance_score'] = np.round(
    3 + 0.3 * (df['hours_worked'] - 6) + 0.1 * df['coffee_cups'] + np.random.normal(0, 0.2, n), 2
)
df['performance_score'] = df['performance_score'].clip(3, 5)

# Salary influenced by performance (simulate variable daily bonus)
df['salary'] = np.round(
    20 + df['performance_score'] * 250 + np.random.normal(0, 50, n), 0
)

print(df.head(10))
print("\nTotal rows:", len(df))

# Optional: save to CSV
df.to_csv("employee_data.csv", index=False)
