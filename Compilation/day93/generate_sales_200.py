import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

num_rows = 200
sources = ['LinkedIn', 'Cold Email', 'Referral', 'Webinar', 'Cold Call', 'Organic Search']
statuses = ['New Lead', 'Contacted', 'Qualified', 'Proposal Sent', 'Closed Won', 'Closed Lost']
companies = [f"Company_{i}" for i in range(1, 51)]  # 50 unique companies

data = {
    'Date_Acquired': [(datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365))).strftime('%Y-%m-%d') for _ in range(num_rows)],
    'Company': [np.random.choice(companies) for _ in range(num_rows)],
    'Source': [np.random.choice(sources, p=[0.3, 0.25, 0.1, 0.15, 0.1, 0.1]) for _ in range(num_rows)],
    'Status': [np.random.choice(statuses, p=[0.2, 0.2, 0.2, 0.15, 0.15, 0.1]) for _ in range(num_rows)],
    'Acquisition_Cost': np.round(np.random.uniform(10, 150, num_rows), 2),
    'Expected_Revenue': np.round(np.random.uniform(1000, 20000, num_rows), -2) # Round to nearest 100
}

df = pd.DataFrame(data)

# Sort by date
df = df.sort_values(by='Date_Acquired')

# Save to CSV
df.to_csv('sales_acquisition_200.csv', index=False)
print("Data generated successfully.")
