"""
Employee SQL Tutorial Database Setup
Run this script to create the employee database for SQL practice.
"""

import sqlite3

# Create connection to database
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Create Departments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL,
    location TEXT NOT NULL
)
''')

# Create Employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    hire_date TEXT NOT NULL,
    salary REAL NOT NULL,
    department_id INTEGER,
    job_title TEXT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
)
''')

# Create Projects table
cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT,
    budget REAL NOT NULL
)
''')

# Create Employee_Projects table (many-to-many relationship)
cursor.execute('''
CREATE TABLE IF NOT EXISTS employee_projects (
    employee_id INTEGER,
    project_id INTEGER,
    role TEXT NOT NULL,
    hours_worked INTEGER DEFAULT 0,
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
)
''')

# Insert departments
departments_data = [
    (1, 'Engineering', 'Building A'),
    (2, 'Marketing', 'Building B'),
    (3, 'Human Resources', 'Building A'),
    (4, 'Finance', 'Building C'),
    (5, 'Sales', 'Building B'),
]

cursor.executemany('INSERT OR REPLACE INTO departments VALUES (?, ?, ?)', departments_data)

# Insert employees
employees_data = [
    (1, 'John', 'Smith', 'john.smith@company.com', '2020-01-15', 75000, 1, 'Software Engineer'),
    (2, 'Sarah', 'Johnson', 'sarah.j@company.com', '2019-03-20', 85000, 1, 'Senior Engineer'),
    (3, 'Mike', 'Williams', 'mike.w@company.com', '2021-06-01', 65000, 2, 'Marketing Specialist'),
    (4, 'Emily', 'Brown', 'emily.b@company.com', '2018-09-10', 95000, 1, 'Tech Lead'),
    (5, 'David', 'Jones', 'david.j@company.com', '2022-02-14', 55000, 5, 'Sales Representative'),
    (6, 'Lisa', 'Garcia', 'lisa.g@company.com', '2020-07-22', 70000, 2, 'Marketing Manager'),
    (7, 'James', 'Miller', 'james.m@company.com', '2019-11-05', 60000, 3, 'HR Specialist'),
    (8, 'Anna', 'Davis', 'anna.d@company.com', '2021-04-18', 80000, 4, 'Financial Analyst'),
    (9, 'Robert', 'Wilson', 'robert.w@company.com', '2017-08-30', 110000, 1, 'Engineering Manager'),
    (10, 'Jennifer', 'Taylor', 'jennifer.t@company.com', '2022-01-10', 52000, 5, 'Sales Associate'),
    (11, 'Michael', 'Anderson', 'michael.a@company.com', '2020-05-25', 72000, 4, 'Accountant'),
    (12, 'Jessica', 'Thomas', 'jessica.t@company.com', '2018-12-01', 88000, 3, 'HR Manager'),
    (13, 'William', 'Jackson', 'william.j@company.com', '2023-03-15', 58000, 1, 'Junior Developer'),
    (14, 'Ashley', 'White', 'ashley.w@company.com', '2021-09-08', 67000, 2, 'Content Creator'),
    (15, 'Christopher', 'Harris', 'chris.h@company.com', '2019-06-12', 78000, 5, 'Sales Manager'),
]

cursor.executemany('INSERT OR REPLACE INTO employees VALUES (?, ?, ?, ?, ?, ?, ?, ?)', employees_data)

# Insert projects
projects_data = [
    (1, 'Website Redesign', '2024-01-01', '2024-06-30', 150000),
    (2, 'Mobile App Development', '2024-02-15', '2024-12-31', 300000),
    (3, 'Marketing Campaign Q1', '2024-01-01', '2024-03-31', 50000),
    (4, 'HR System Upgrade', '2024-03-01', '2024-09-30', 80000),
    (5, 'Sales Training Program', '2024-04-01', None, 25000),
]

cursor.executemany('INSERT OR REPLACE INTO projects VALUES (?, ?, ?, ?, ?)', projects_data)

# Insert employee-project assignments
employee_projects_data = [
    (1, 1, 'Developer', 120),
    (2, 1, 'Lead Developer', 200),
    (4, 1, 'Project Manager', 80),
    (1, 2, 'Developer', 150),
    (2, 2, 'Lead Developer', 180),
    (9, 2, 'Technical Advisor', 40),
    (13, 2, 'Junior Developer', 200),
    (3, 3, 'Content Creator', 100),
    (6, 3, 'Campaign Manager', 120),
    (14, 3, 'Designer', 80),
    (7, 4, 'Requirements Analyst', 60),
    (12, 4, 'Project Lead', 100),
    (5, 5, 'Trainer', 40),
    (10, 5, 'Participant', 20),
    (15, 5, 'Program Lead', 50),
]

cursor.executemany('INSERT OR REPLACE INTO employee_projects VALUES (?, ?, ?, ?)', employee_projects_data)

# Commit and close
conn.commit()
conn.close()

print("✅ Database 'employee.db' created successfully!")
print("\nTables created:")
print("  - departments (5 records)")
print("  - employees (15 records)")
print("  - projects (5 records)")
print("  - employee_projects (15 records)")
