# generate_data.py
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Create 1000 rows of data
num_rows = 1000

departments = ['Sales', 'IT', 'HR', 'Marketing', 'Operations']
categories = ['Office Supplies', 'Software', 'Travel', 'Payroll', 'Consulting']
types = ['Income', 'Expense', 'income ', 'expNs', 'Income', 'Expense'] # Notice the typos
date_formats = ['%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y']

data = []
for i in range(num_rows):
    # Random Date with different formats
    random_days = random.randint(0, 365)
    random_date = datetime(2023, 1, 1) + timedelta(days=random_days)
    date_str = random_date.strftime(random.choice(date_formats))
    
    # Introduce 5% chance of missing date
    if random.random() < 0.05: date_str = np.nan
        
    category = random.choice(categories)
    # Introduce messy casing
    if random.random() < 0.2: category = category.lower()
    if random.random() < 0.1: category = category.upper()
        
    trans_type = random.choice(types)
    
    # Generate messy amounts with random '$', commas, and negative signs
    amount_val = round(random.uniform(50, 5000), 2)
    if trans_type.lower().startswith('exp'):
        amount = f"-${amount_val:,.2f}" if random.random() > 0.5 else f"-{amount_val}"
    else:
        amount = f"${amount_val:,.2f}" if random.random() > 0.5 else str(amount_val)
        
    # 5% chance of missing amount
    if random.random() < 0.05: amount = np.nan

    data.append([f"TRX-{1000+i}", date_str, random.choice(departments), category, trans_type, amount])

df = pd.DataFrame(data, columns=['Transaction_ID', 'Date', 'Department', 'Category', 'Type', 'Amount'])
# This creates the actual CSV file that data.py is looking for!
df.to_csv("accounting_data.csv", index=False)
print("✅ Successfully generated 'accounting_data.csv' with 1,000 rows!")
