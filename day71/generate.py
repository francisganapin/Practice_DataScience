import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# ---------- RAW SOURCES (simulating messy operational data) ----------

# Source 1: Sales transactions (messy)
n_sales = 500
sales_raw = pd.DataFrame({
    'transaction_id': range(1, n_sales + 1),
    'product': np.random.choice(['Laptop', 'laptop', 'LAPTOP', 'Phone', 'phone',
                                  'Tablet', 'tablet', 'Headphones', 'headphones'], n_sales),
    'customer_name': np.random.choice(['Alice Santos', 'Bob Cruz', 'alice santos',
                                        'Charlie Reyes', 'Diana Lopez', None,
                                        'Eve Garcia', 'Frank Torres'], n_sales),
    'customer_city': np.random.choice(['Manila', 'Cebu', 'Davao', 'manila',
                                        'cebu', None], n_sales),
    'quantity': np.random.randint(1, 10, n_sales),
    'unit_price': np.random.choice([999.99, 499.99, 299.99, 79.99, -50.00], n_sales),  # -50 = bad data
    'sale_date': [(datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 365))).strftime('%Y-%m-%d')
                  for _ in range(n_sales)],
    'region': np.random.choice(['Luzon', 'Visayas', 'Mindanao', 'luzon', None], n_sales),
})

# Save raw data
sales_raw.to_csv('raw_sales.csv', index=False)
print(f"Generated {len(sales_raw)} raw sales records -> raw_sales.csv")
print(f"Sample issues: {sales_raw['customer_name'].isna().sum()} null customers, "
      f"{(sales_raw['unit_price'] < 0).sum()} negative prices")