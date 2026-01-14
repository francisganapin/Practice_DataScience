# 🐼 15 Pandas Practice Problems

Use the `employees.csv` dataset to solve these problems!

---

## Getting Started

```python
import pandas as pd

df = pd.read_csv('employees.csv')
```

---

## **Easy Level (1-5)**

### Problem 1: Basic Data Exploration
Display the first 10 rows of the dataset, the shape of the dataframe, and all column names.

---

### Problem 2: Data Types Check
Find out the data types of each column. Convert `hire_date` to datetime format.

---

### Problem 3: Missing Values
Check if there are any missing values in the dataset. Display the count of missing values per column.

---

### Problem 4: Basic Statistics
Calculate the mean, median, min, and max salary from the dataset.

---

### Problem 5: Filtering Rows
Filter and display all employees who:
- Work in the **Engineering** department
- Have a salary greater than **$90,000**

---

## **Medium Level (6-10)**

### Problem 6: Groupby Operations
Calculate the **average salary** and **average performance score** for each department. Sort the results by average salary in descending order.

---

### Problem 7: Value Counts & Percentages
Find how many employees are in each department. Display both the count and the percentage of total employees.

---

### Problem 8: Conditional Column
Create a new column called `salary_tier` based on salary:
- `'Low'` if salary < 60,000
- `'Medium'` if salary between 60,000 and 90,000
- `'High'` if salary > 90,000

---

### Problem 9: Top N Records
Find the **top 5 highest-paid employees** and display their full name, department, job title, and salary.

---

### Problem 10: Multiple Conditions
Find all employees who:
- Are **remote workers** (`is_remote == True`)
- Have **more than 5 years of experience**
- Have a **performance score above 4.0**

---

## **Hard Level (11-15)**

### Problem 11: Date Calculations
Calculate how many years each employee has been with the company (from hire_date to today). Add this as a new column called `tenure_years`. Find the employee with the longest tenure.

---

### Problem 12: Pivot Table
Create a pivot table showing:
- **Rows**: Department
- **Columns**: Gender
- **Values**: Average salary

Which department has the highest gender pay gap?

---

### Problem 13: Correlation Analysis
Calculate the correlation between:
- `salary` and `years_experience`
- `salary` and `performance_score`
- `age` and `salary`

Which factor has the strongest correlation with salary?

---

### Problem 14: Complex Aggregation
For each department, find:
1. Total number of employees
2. Total salary expense
3. Average bonus percentage
4. Number of remote workers
5. Average years of experience

Sort by total salary expense descending.

---

### Problem 15: Ranking & Percentiles
Create a new column `salary_rank` that ranks employees by salary within their department (1 = highest in dept). Also calculate what percentile each employee's salary falls into overall (across the entire company).

---

## 💡 Hints

- Use `pd.to_datetime()` for date conversions
- Use `groupby()` and `agg()` for aggregations
- Use `apply()` with lambda or custom functions for complex transformations
- Use `np.where()` or `pd.cut()` for conditional columns
- Use `rank()` and `quantile()` for ranking problems

---

## 📊 Bonus Challenge

Combine your findings into a short data analysis report answering:
1. Which department has the highest average salary?
2. Is there a correlation between remote work and performance?
3. What's the average bonus percentage by salary tier?

Good luck! 🎯
