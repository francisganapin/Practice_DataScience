import sqlite3
import random
from datetime import datetime, timedelta
def create_connection():
    try:
        conn = sqlite3.connect('analytics.db')
        return conn
    except sqlite3.Error as e:
        print(e)
    return None
def setup_database():
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        # 1. Create Tables
        # Customers Table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT,
            country TEXT,
            signup_date DATE
        );
        ''')
        # Products Table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            category TEXT,
            price REAL
        );
        ''')
        # Orders Table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            order_date DATE,
            total_amount REAL,
            FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
        );
        ''')
        # Reviews Table (Good for Left Joins - not every product has a review)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            review_id INTEGER PRIMARY KEY,
            product_id INTEGER,
            rating INTEGER,
            comment TEXT,
            FOREIGN KEY (product_id) REFERENCES products (product_id)
        );
        ''')
        # Marketing Channels (Good for Analytics)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS marketing_channels (
            channel_id INTEGER PRIMARY KEY,
            channel_name TEXT
        );
        ''')
        
        # Attribution (Linking customers to channels)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_attribution (
            attribution_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            channel_id INTEGER,
            FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
            FOREIGN KEY (channel_id) REFERENCES marketing_channels (channel_id)
        );
        ''')
        # 2. Insert Mock Data
        
        # Marketing Channels
        channels = [('Organic Search',), ('Social Media',), ('Email',), ('Paid Ads',), ('Referral',)]
        cursor.executemany("INSERT INTO marketing_channels (channel_name) VALUES (?)", channels)
        
        # Products
        products = [
            ('Laptop Pro', 'Electronics', 1200.00),
            ('Smartphone X', 'Electronics', 800.00),
            ('Wireless Mouse', 'Accessories', 25.50),
            ('Mechanical Keyboard', 'Accessories', 150.00),
            ('Noise Cancelling Headphones', 'Electronics', 250.00),
            ('Coffee Mug', 'Home', 12.00),
            ('Office Chair', 'Furniture', 300.00),
            ('Desk Lamp', 'Home', 45.00),
            ('Gaming Monitor', 'Electronics', 400.00),
            ('USB-C Cable', 'Accessories', 15.00)
        ]
        cursor.executemany("INSERT INTO products (product_name, category, price) VALUES (?, ?, ?)", products)
        # Customers
        customers = [
            ('John', 'Doe', 'john@example.com', 'USA', '2023-01-15'),
            ('Jane', 'Smith', 'jane@test.com', 'UK', '2023-02-10'),
            ('Michael', 'Johnson', 'mike@demo.com', 'USA', '2023-03-05'),
            ('Emily', 'Davis', 'emily@sample.net', 'Canada', '2023-03-20'),
            ('David', 'Wilson', 'david@example.com', 'UK', '2023-04-01'),
            ('Sarah', 'Brown', 'sarah@test.com', 'Australia', '2023-05-12'),
            ('Robert', 'Miller', 'rob@demo.com', 'USA', '2023-06-15'),
            ('Jessica', 'Taylor', None, 'Canada', '2023-07-01'), # Null email
            ('Alice', 'Wonder', 'alice@wonder.com', 'Germany', '2023-08-20'), # New customer, maybe no orders
            ('Bob', 'Builder', 'bob@build.com', 'USA', '2023-09-10')
        ]
        cursor.executemany("INSERT INTO customers (first_name, last_name, email, country, signup_date) VALUES (?, ?, ?, ?, ?)", customers)
        # Orders (Random generation for complexity)
        # We leave some customers without orders to test LEFT JOIN
        orders = []
        for i in range(1, 20): # 19 orders
            cust_id = random.choice([1, 2, 3, 4, 5, 6, 7]) # Customers 8, 9, 10 have no orders
            order_date = (datetime(2023, 1, 1) + timedelta(days=random.randint(0, 300))).strftime('%Y-%m-%d')
            amount = round(random.uniform(20.0, 1500.0), 2)
            orders.append((cust_id, order_date, amount))
        
        cursor.executemany("INSERT INTO orders (customer_id, order_date, total_amount) VALUES (?, ?, ?)", orders)
        # Reviews
        reviews = [
            (1, 5, 'Great laptop!'),
            (1, 4, 'Good but expensive'),
            (3, 5, 'Works perfectly'),
            (6, 2, 'Arrived broken'),
            (7, 4, 'Comfortable chair')
        ]
        cursor.executemany("INSERT INTO reviews (product_id, rating, comment) VALUES (?, ?, ?)", reviews)
        # Customer Attribution
        attributions = [
            (1, 1), # John - Organic
            (2, 2), # Jane - Social
            (3, 3), # Michael - Email
            (4, 1), # Emily - Organic
            (5, 4), # David - Paid Ads
            (6, 5), # Sarah - Referral
            (7, 2), # Robert - Social
            (8, 3), # Jessica - Email
            (9, 1), # Alice - Organic
            (10, 4) # Bob - Paid Ads
        ]
        cursor.executemany("INSERT INTO customer_attribution (customer_id, channel_id) VALUES (?, ?)", attributions)
        conn.commit()
        print("Database 'analytics.db' created and seeded successfully!")
        conn.close()
    else:
        print("Error! cannot create the database connection.")
if __name__ == '__main__':
    setup_database()

