"""
SQL Tutorial Database Setup
Run this script to create the sample database for SQL practice.
"""

import sqlite3

# Create connection to database (creates file if it doesn't exist)
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Create Products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock_quantity INTEGER NOT NULL
)
''')

# Create Customers table
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    city TEXT NOT NULL
)
''')

# Create Orders table
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
''')

# Insert sample products
products_data = [
    (1, 'Laptop', 'Electronics', 999.99, 50),
    (2, 'Smartphone', 'Electronics', 699.99, 100),
    (3, 'Headphones', 'Electronics', 149.99, 200),
    (4, 'Coffee Table', 'Furniture', 249.99, 30),
    (5, 'Office Chair', 'Furniture', 199.99, 45),
    (6, 'Bookshelf', 'Furniture', 129.99, 25),
    (7, 'Running Shoes', 'Sports', 89.99, 80),
    (8, 'Basketball', 'Sports', 29.99, 60),
    (9, 'Yoga Mat', 'Sports', 39.99, 100),
    (10, 'Water Bottle', 'Sports', 19.99, 150),
    (11, 'Desk Lamp', 'Electronics', 49.99, 75),
    (12, 'Gaming Mouse', 'Electronics', 79.99, 90),
]

cursor.executemany('INSERT OR REPLACE INTO products VALUES (?, ?, ?, ?, ?)', products_data)

# Insert sample customers
customers_data = [
    (1, 'John', 'Smith', 'john.smith@email.com', 'New York'),
    (2, 'Sarah', 'Johnson', 'sarah.j@email.com', 'Los Angeles'),
    (3, 'Mike', 'Williams', 'mike.w@email.com', 'Chicago'),
    (4, 'Emily', 'Brown', 'emily.b@email.com', 'Houston'),
    (5, 'David', 'Jones', 'david.j@email.com', 'New York'),
    (6, 'Lisa', 'Garcia', 'lisa.g@email.com', 'Los Angeles'),
    (7, 'James', 'Miller', 'james.m@email.com', 'Seattle'),
    (8, 'Anna', 'Davis', 'anna.d@email.com', 'Chicago'),
]

cursor.executemany('INSERT OR REPLACE INTO customers VALUES (?, ?, ?, ?, ?)', customers_data)

# Insert sample orders
orders_data = [
    (1, 1, 1, 1, '2024-01-15'),
    (2, 1, 3, 2, '2024-01-15'),
    (3, 2, 2, 1, '2024-01-16'),
    (4, 3, 5, 1, '2024-01-17'),
    (5, 4, 7, 2, '2024-01-18'),
    (6, 5, 1, 1, '2024-01-19'),
    (7, 6, 9, 3, '2024-01-20'),
    (8, 7, 4, 1, '2024-01-21'),
    (9, 8, 12, 2, '2024-01-22'),
    (10, 1, 10, 4, '2024-01-23'),
    (11, 2, 6, 1, '2024-01-24'),
    (12, 3, 8, 2, '2024-01-25'),
    (13, 4, 11, 1, '2024-01-26'),
    (14, 5, 3, 1, '2024-01-27'),
    (15, 6, 2, 1, '2024-01-28'),
]

cursor.executemany('INSERT OR REPLACE INTO orders VALUES (?, ?, ?, ?, ?)', orders_data)

# Commit and close
conn.commit()
conn.close()

print("✅ Database 'store.db' created successfully!")
print("\nTables created:")
print("  - products (12 records)")
print("  - customers (8 records)")
print("  - orders (15 records)")
