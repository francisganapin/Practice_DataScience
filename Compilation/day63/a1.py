import sqlite3
from datetime import date
# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect('date_practice.db')
cursor = conn.cursor()
# 1. Clean up old tables
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS customers")
# 2. Create Tables
cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    join_date TEXT      -- Format: YYYY-MM-DD
)
""")
cursor.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,      -- Format: YYYY-MM-DD
    delivery_date TEXT,   -- Format: YYYY-MM-DD
    amount REAL,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
)
""")
# 3. Insert specific dummy data
customers_data = [
    (1, 'Alice',   '2023-01-15'),  
    (2, 'Bob',     '2023-06-20'),  
    (3, 'Charlie', '2023-10-01'),  
    (4, 'David',   '2022-12-01'),  
    (5, 'Eve',     '2024-01-01')    
]
orders_data = [
    (101, 1, '2023-02-01', '2023-02-05', 150.00),   
    (102, 2, '2023-07-15', '2023-07-20', 200.50), 
    (103, 3, '2023-10-01', '2023-10-02', 50.00),  
    (104, 3, '2023-11-05', '2023-11-10', 300.00),
    (105, 4, '2023-01-05', '2023-01-10', 500.00), 
    (106, 1, date.today().isoformat(), None, 120.00)
]

cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", customers_data)
cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", orders_data)
conn.commit()
print("✅ Database created with 5 customers and 6 orders!")
conn.close()