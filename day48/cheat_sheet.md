# Pandas Data Analysis Cheat Sheet

## 1. Loading Data
```python
import pandas as pd

# Load CSV file
df = pd.read_csv('employees.csv')

# Display first n rows
df.head()
df.head(10)

# Display info (columns, types, non-null counts)
df.info()

# Basic statistics
df.describe()
```

## 2. Selecting and Filtering
```python
# Select a single column
df['Salary']

# Select multiple columns
df[['FirstName', 'LastName', 'Department']]

# Filter by condition
df[df['Department'] == 'Engineering']

# Multiple conditions (AND: &, OR: |)
df[(df['Salary'] > 100000) & (df['City'] == 'New York')]

# Filter by string contains
df[df['LastName'].str.contains('son')]
```

## 3. Sorting
```python
# Sort by values
df.sort_values(by='Salary', ascending=False)

# Sort by multiple columns
df.sort_values(by=['Department', 'Salary'], ascending=[True, False])
```

## 4. Grouping and Aggregation
```python
# Group by a column and calculate mean
df.groupby('Department')['Salary'].mean()

# Group by multiple columns
df.groupby(['Department', 'City'])['Age'].mean()

# Multiple aggregations
df.groupby('Department').agg({
    'Salary': 'mean',
    'Age': 'max',
    'EmployeeID': 'count'
})
```

## 5. Date Handling
```python
# Convert to datetime
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])

# Extract year/month
df['Year'] = df['JoiningDate'].dt.year
df['Month'] = df['JoiningDate'].dt.month

# Filter by date
df[df['JoiningDate'] > '2020-01-01']
```

## 6. Creating New Columns
```python
# Simple calculation
df['MonthlySalary'] = df['Salary'] / 12

# Conditional column (using numpy)
import numpy as np
df['HighEarner'] = np.where(df['Salary'] > 100000, 'Yes', 'No')
```

## 7. Handling Missing Data
```python
# Check for nulls
df.isnull().sum()

# Drop rows with nulls
df.dropna()

# Fill nulls
df.fillna(0)
```
