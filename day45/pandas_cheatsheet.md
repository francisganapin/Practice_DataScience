# 🐼 Pandas Cheat Sheet

A quick reference for working with the `employees.csv` dataset!

---

## 📥 **Loading & Viewing Data**

```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('employees.csv')

# View data
df.head(10)          # First 10 rows
df.tail(5)           # Last 5 rows
df.sample(5)         # Random 5 rows
df.shape             # (rows, columns)
df.columns           # Column names
df.info()            # Data types & non-null counts
df.describe()        # Statistics for numeric columns
```

---

## 🔍 **Selecting Data**

```python
# Single column
df['salary']
df.salary

# Multiple columns
df[['first_name', 'last_name', 'salary']]

# Rows by index
df.iloc[0]           # First row
df.iloc[0:5]         # First 5 rows
df.iloc[0, 2]        # Row 0, Column 2

# Rows by label
df.loc[0]            # Row with label 0
df.loc[0:5, 'salary':'age']  # Slice rows and columns
```

---

## 🎯 **Filtering Data**

```python
# Single condition
df[df['salary'] > 90000]
df[df['department'] == 'Engineering']

# Multiple conditions (AND)
df[(df['salary'] > 90000) & (df['is_remote'] == True)]

# Multiple conditions (OR)
df[(df['department'] == 'Engineering') | (df['department'] == 'Sales')]

# Using isin()
df[df['department'].isin(['Engineering', 'Sales', 'Marketing'])]

# String contains
df[df['job_title'].str.contains('Manager')]

# Negation
df[~df['is_remote']]  # NOT remote
```

---

## ➕ **Adding & Modifying Columns**

```python
# New column with calculation
df['total_comp'] = df['salary'] * (1 + df['bonus_percentage'] / 100)

# Conditional column with np.where()
df['high_earner'] = np.where(df['salary'] > 90000, 'Yes', 'No')

# Multiple conditions with np.select()
conditions = [
    df['salary'] < 60000,
    df['salary'] <= 90000,
    df['salary'] > 90000
]
choices = ['Low', 'Medium', 'High']
df['salary_tier'] = np.select(conditions, choices)

# Using apply() with lambda
df['full_name'] = df.apply(lambda x: f"{x['first_name']} {x['last_name']}", axis=1)

# Using pd.cut() for binning
df['age_group'] = pd.cut(df['age'], bins=[20, 30, 40, 50, 60], labels=['20s', '30s', '40s', '50s'])
```

---

## 📊 **Groupby & Aggregations**

```python
# Single aggregation
df.groupby('department')['salary'].mean()

# Multiple aggregations
df.groupby('department')['salary'].agg(['mean', 'min', 'max', 'count'])

# Multiple columns
df.groupby('department').agg({
    'salary': ['mean', 'sum'],
    'performance_score': 'mean',
    'employee_id': 'count'
})

# Named aggregations (cleaner output)
df.groupby('department').agg(
    avg_salary=('salary', 'mean'),
    total_salary=('salary', 'sum'),
    employee_count=('employee_id', 'count'),
    avg_performance=('performance_score', 'mean')
).reset_index()

# Groupby multiple columns
df.groupby(['department', 'gender'])['salary'].mean()
```

---

## 📈 **Sorting & Ranking**

```python
# Sort values
df.sort_values('salary', ascending=False)
df.sort_values(['department', 'salary'], ascending=[True, False])

# Top N
df.nlargest(5, 'salary')
df.nsmallest(5, 'salary')

# Ranking
df['salary_rank'] = df['salary'].rank(ascending=False)

# Rank within groups
df['dept_rank'] = df.groupby('department')['salary'].rank(ascending=False)

# Percentile
df['salary_percentile'] = df['salary'].rank(pct=True) * 100
```

---

## 📅 **Date Operations**

```python
# Convert to datetime
df['hire_date'] = pd.to_datetime(df['hire_date'])

# Extract components
df['hire_year'] = df['hire_date'].dt.year
df['hire_month'] = df['hire_date'].dt.month
df['hire_day'] = df['hire_date'].dt.day
df['hire_weekday'] = df['hire_date'].dt.day_name()

# Calculate tenure
from datetime import datetime
df['tenure_years'] = (datetime.now() - df['hire_date']).dt.days / 365

# Filter by date
df[df['hire_date'] > '2020-01-01']
df[df['hire_date'].dt.year == 2019]
```

---

## 📉 **Statistics & Correlation**

```python
# Basic stats
df['salary'].mean()
df['salary'].median()
df['salary'].std()
df['salary'].var()
df['salary'].quantile(0.75)  # 75th percentile

# Value counts
df['department'].value_counts()
df['department'].value_counts(normalize=True)  # Percentages

# Correlation
df['salary'].corr(df['years_experience'])

# Correlation matrix
df[['salary', 'age', 'years_experience', 'performance_score']].corr()
```

---

## 🔄 **Pivot Tables**

```python
# Basic pivot
pd.pivot_table(df, values='salary', index='department', columns='gender', aggfunc='mean')

# Multiple aggregations
pd.pivot_table(df, 
               values='salary', 
               index='department', 
               columns='gender',
               aggfunc=['mean', 'count'],
               margins=True)  # Adds totals
```

---

## 🧹 **Data Cleaning**

```python
# Check for nulls
df.isnull().sum()

# Fill nulls
df['column'].fillna(0)
df['column'].fillna(df['column'].mean())

# Drop nulls
df.dropna()
df.dropna(subset=['salary', 'department'])

# Drop duplicates
df.drop_duplicates()
df.drop_duplicates(subset=['first_name', 'last_name'])

# Replace values
df['gender'].replace({'M': 'Male', 'F': 'Female'})

# Rename columns
df.rename(columns={'old_name': 'new_name'})

# Change data types
df['salary'] = df['salary'].astype(float)
```

---

## 🔗 **Merging & Concatenating**

```python
# Concatenate dataframes (stack rows)
pd.concat([df1, df2])

# Merge (like SQL JOIN)
pd.merge(df1, df2, on='employee_id')
pd.merge(df1, df2, on='employee_id', how='left')   # LEFT JOIN
pd.merge(df1, df2, on='employee_id', how='right')  # RIGHT JOIN
pd.merge(df1, df2, on='employee_id', how='outer')  # FULL OUTER JOIN
```

---

## 💾 **Exporting Data**

```python
# To CSV
df.to_csv('output.csv', index=False)

# To Excel
df.to_excel('output.xlsx', index=False, sheet_name='Employees')

# To JSON
df.to_json('output.json', orient='records')
```

---

## 🎯 **Quick Reference Table**

| Task | Code |
|------|------|
| Load CSV | `pd.read_csv('file.csv')` |
| View shape | `df.shape` |
| Column names | `df.columns.tolist()` |
| Data types | `df.dtypes` |
| Filter rows | `df[df['col'] > value]` |
| Select columns | `df[['col1', 'col2']]` |
| Group & aggregate | `df.groupby('col')['val'].mean()` |
| Sort descending | `df.sort_values('col', ascending=False)` |
| Top 5 | `df.nlargest(5, 'col')` |
| Value counts | `df['col'].value_counts()` |
| Add column | `df['new'] = df['a'] + df['b']` |
| Drop column | `df.drop('col', axis=1)` |
| Rename column | `df.rename(columns={'old': 'new'})` |
| Fill nulls | `df['col'].fillna(0)` |
| Reset index | `df.reset_index(drop=True)` |

---

Good luck with your practice! 🚀
