import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

# --- Config ---
num_records = 200
cities = ["Manila", "Cebu", "Davao", "Makati", "Quezon City", "Taguig"]
property_types = ["Condo", "House & Lot", "Townhouse", "Vacant Lot", "Commercial"]
agents = ["Agent_A", "Agent_B", "Agent_C", "Agent_D", "Agent_E", "Agent_F"]

# --- Generate normal transactions ---
data = []
for i in range(1, num_records + 1):
    txn_id = f"TXN-{i:04d}"
    date = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 364))
    city = random.choice(cities)
    prop_type = random.choice(property_types)
    agent = random.choice(agents)
    
    # Normal price ranges per type (in PHP)
    price_ranges = {
        "Condo": (2_000_000, 8_000_000),
        "House & Lot": (3_000_000, 15_000_000),
        "Townhouse": (2_500_000, 10_000_000),
        "Vacant Lot": (500_000, 5_000_000),
        "Commercial": (5_000_000, 30_000_000),
    }
    
    low, high = price_ranges[prop_type]
    listed_price = round(random.uniform(low, high), 2)
    
    # Normal: sold price is 85%-100% of listed price
    sold_price = round(listed_price * random.uniform(0.85, 1.0), 2)
    
    # Normal: appraisal is close to listed price (90%-110%)
    appraised_value = round(listed_price * random.uniform(0.90, 1.10), 2)
    
    # Days on market
    days_on_market = random.randint(30, 180)
    
    # Buyer-seller same city? (normal = mostly yes)
    buyer_city = city if random.random() > 0.3 else random.choice(cities)
    
    # Number of transactions by this buyer in this year
    buyer_txn_count = random.choices([1, 2, 3], weights=[70, 20, 10])[0]
    
    data.append({
        "txn_id": txn_id,
        "date": date.strftime("%Y-%m-%d"),
        "city": city,
        "property_type": prop_type,
        "agent": agent,
        "listed_price": listed_price,
        "sold_price": sold_price,
        "appraised_value": appraised_value,
        "days_on_market": days_on_market,
        "buyer_city": buyer_city,
        "buyer_txn_count": buyer_txn_count,
    })

df = pd.DataFrame(data)

# --- Inject Fraud (rows 180-200) ---
fraud_indices = list(range(179, 200))  # last ~20 rows

for idx in fraud_indices:
    fraud_type = random.choice(["price_flip", "undervalue", "rapid", "volume"])
    
    if fraud_type == "price_flip":
        # Sold WAY above listed price (flipping fraud)
        df.at[idx, "sold_price"] = round(df.at[idx, "listed_price"] * random.uniform(1.5, 3.0), 2)
    
    elif fraud_type == "undervalue":
        # Sold way below appraised value (money laundering indicator)
        df.at[idx, "sold_price"] = round(df.at[idx, "appraised_value"] * random.uniform(0.3, 0.5), 2)
    
    elif fraud_type == "rapid":
        # Suspiciously fast sale
        df.at[idx, "days_on_market"] = random.randint(0, 3)
    
    elif fraud_type == "volume":
        # Buyer doing too many transactions
        df.at[idx, "buyer_txn_count"] = random.randint(8, 20)

# Save to Excel
df.to_excel("real_estate_transactions.xlsx", index=False, sheet_name="Transactions")
print("✅ Dataset saved: real_estate_transactions.xlsx")
print(f"Total records: {len(df)}")
print(f"Fraud records injected: {len(fraud_indices)}")