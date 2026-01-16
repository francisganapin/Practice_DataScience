import csv
import random
from datetime import datetime, timedelta

departments = ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance', 'IT', 'Operations']
first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Robert', 'Jessica', 'William', 'Ashley', 'James', 'Mary', 'Christopher', 'Jennifer', 'Matthew', 'Lisa', 'Joshua', 'Linda', 'Daniel', 'Elizabeth']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin']

def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

start_date = datetime(2015, 1, 1)
end_date = datetime(2023, 12, 31)

header = ['EmployeeID', 'FirstName', 'LastName', 'Department', 'Salary', 'JoiningDate', 'Age', 'PerformanceScore', 'City']
data = []

for i in range(1, 101):
    emp_id = 1000 + i
    f_name = random.choice(first_names)
    l_name = random.choice(last_names)
    dept = random.choice(departments)
    salary = random.randint(40000, 150000)
    join_date = random_date(start_date, end_date).strftime('%Y-%m-%d')
    age = random.randint(22, 60)
    perf_score = random.randint(1, 5)
    city = random.choice(['Makati', 'Pasig', 'Taguig', 'Quezon', 'Muntinlupa', 'Mandaluyong','Manila','Navotas',])
    
    data.append([emp_id, f_name, l_name, dept, salary, join_date, age, perf_score, city])

with open('employees2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print("employees2.csv created successfully.")
