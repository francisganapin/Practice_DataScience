import pandas as pd
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
random.seed(42)

# Configuration
num_records = 200

# Data options
regions = ['NCR', 'Calabarzon', 'Central Luzon', 'Central Visayas', 'Davao Region', 
           'Western Visayas', 'Northern Mindanao', 'Ilocos Region', 'Bicol Region', 'SOCCSKSARGEN']

categories = ['Electronics', 'Fashion', 'Home & Living', 'Beauty', 'Sports', 
              'Groceries', 'Toys', 'Books', 'Automotive', 'Health']

payment_methods = ['Credit Card', 'GCash', 'Maya', 'COD', 'Bank Transfer', 'GrabPay']

shipping_options = ['Standard', 'Express', 'Same Day', 'Economy']

statuses = ['Delivered', 'Processing', 'Shipped', 'Cancelled', 'Returned']

# Generate data
data = []
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

for i in range(num_records):
    # Random date
    random_days = random.randint(0, (end_date - start_date).days)
    order_date = start_date + timedelta(days=random_days)
    
    # Random time of order
    order_hour = random.randint(0, 23)
    order_minute = random.randint(0, 59)
    order_time = f'{order_hour:02d}:{order_minute:02d}'
    
    # Random values
    category = random.choice(categories)
    quantity = random.randint(1, 10)
    
    # === ANOMALY: 10% chance of unusually high quantity ===
    if random.random() < 0.10:
        quantity = random.randint(50, 500)
    
    # Price based on category
    base_prices = {
        'Electronics': (500, 50000),
        'Fashion': (200, 5000),
        'Home & Living': (300, 15000),
        'Beauty': (100, 3000),
        'Sports': (200, 8000),
        'Groceries': (50, 2000),
        'Toys': (100, 3000),
        'Books': (150, 1500),
        'Automotive': (500, 20000),
        'Health': (100, 5000)
    }
    
    unit_price = round(random.uniform(*base_prices[category]), 2)
    total_cost = round(unit_price * quantity, 2)
    shipping_cost = round(random.uniform(50, 300), 2)
    discount = round(random.uniform(0, total_cost * 0.3), 2)
    final_amount = round(total_cost + shipping_cost - discount, 2)
    
    record = {
        'order_id': f'ORD-{i+1001:05d}',
        'order_date': order_date.strftime('%Y-%m-%d'),
        'order_time': order_time,
        'region': random.choice(regions),
        'category': category,
        'product_name': f'{category} Item {random.randint(100, 999)}',
        'quantity': quantity,
        'unit_price': unit_price,
        'total_cost': total_cost,
        'shipping_cost': shipping_cost,
        'discount': discount,
        'final_amount': final_amount,
        'payment_method': random.choice(payment_methods),
        'shipping_type': random.choice(shipping_options),
        'status': random.choice(statuses),
        'customer_rating': random.randint(1, 5)
    }
    data.append(record)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('ecommerce_data.csv', index=False)

print("✅ Dataset created successfully!")
print(f"📊 Total records: {len(df)}")
print(f"📁 File saved: ecommerce_data.csv")
print("\n📋 Column Summary:")
print(df.info())
print("\n📈 Sample Data:")
print(df.head(10))