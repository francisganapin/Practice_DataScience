import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()
np.random.seed(42)
random.seed(42)

# ============================================================
# CONFIG
# ============================================================
NUM_ORDERS = 500
PRODUCTS = {
    'Classic T-Shirt':    {'price': 450, 'category': 'Apparel'},
    'Hoodie Premium':     {'price': 1200, 'category': 'Apparel'},
    'Phone Case':         {'price': 350, 'category': 'Accessories'},
    'Laptop Sleeve':      {'price': 800, 'category': 'Accessories'},
    'Canvas Tote Bag':    {'price': 550, 'category': 'Bags'},
    'Sticker Pack (10)':  {'price': 150, 'category': 'Stationery'},
    'Coffee Mug':         {'price': 400, 'category': 'Home'},
    'Water Bottle':       {'price': 600, 'category': 'Home'},
}

# ============================================================
# GENERATE NORMAL ORDERS
# ============================================================
orders = []
start_date = datetime(2025, 1, 1)

for i in range(1, NUM_ORDERS + 1):
    product_name = random.choice(list(PRODUCTS.keys()))
    product = PRODUCTS[product_name]
    quantity = random.randint(1, 5)
    unit_price = product['price']
    discount_pct = random.choice([0, 0, 0, 0, 5, 10, 15])  # mostly no discount

    subtotal = unit_price * quantity
    discount_amount = subtotal * (discount_pct / 100)
    total = subtotal - discount_amount

    order_date = start_date + timedelta(
        days=random.randint(0, 364),
        hours=random.randint(8, 22),      # normal business hours
        minutes=random.randint(0, 59)
    )

    orders.append({
        'order_id':        f'SHOP-{i:05d}',
        'customer_name':   fake.name(),
        'customer_email':  fake.email(),
        'product':         product_name,
        'category':        product['category'],
        'quantity':        quantity,
        'unit_price':      unit_price,
        'discount_pct':    discount_pct,
        'discount_amount': round(discount_amount, 2),
        'total':           round(total, 2),
        'order_date':      order_date,
        'order_hour':      order_date.hour,
        'payment_method':  random.choice(['Credit Card', 'GCash', 'PayPal', 'COD']),
        'status':          random.choice(['Completed', 'Completed', 'Completed', 'Pending', 'Shipped']),
        'shipping_city':   fake.city(),
        'is_refunded':     False,
    })

# ============================================================
# INJECT ANOMALIES (the ones you'll detect!)
# ============================================================

# --- ANOMALY 1: Revenue Spikes (abnormally high totals) ---
for i in range(5):
    idx = random.randint(0, len(orders) - 1)
    orders[idx]['quantity'] = random.randint(50, 200)
    orders[idx]['total'] = orders[idx]['unit_price'] * orders[idx]['quantity']
    orders[idx]['discount_pct'] = 0
    orders[idx]['discount_amount'] = 0

# --- ANOMALY 2: Extreme Discounts (coupon abuse) ---
for i in range(8):
    idx = random.randint(0, len(orders) - 1)
    orders[idx]['discount_pct'] = random.choice([80, 85, 90, 95])
    subtotal = orders[idx]['unit_price'] * orders[idx]['quantity']
    orders[idx]['discount_amount'] = round(subtotal * (orders[idx]['discount_pct'] / 100), 2)
    orders[idx]['total'] = round(subtotal - orders[idx]['discount_amount'], 2)

# --- ANOMALY 3: Refund Spikes ---
refund_date = start_date + timedelta(days=random.randint(30, 300))
for i in range(12):
    idx = random.randint(0, len(orders) - 1)
    orders[idx]['is_refunded'] = True
    orders[idx]['status'] = 'Refunded'
    orders[idx]['order_date'] = refund_date + timedelta(minutes=random.randint(0, 120))

# --- ANOMALY 4: Late Night Orders (bot traffic) ---
for i in range(10):
    idx = random.randint(0, len(orders) - 1)
    anomaly_date = orders[idx]['order_date'].replace(
        hour=random.randint(1, 4),
        minute=random.randint(0, 59)
    )
    orders[idx]['order_date'] = anomaly_date
    orders[idx]['order_hour'] = anomaly_date.hour

# --- ANOMALY 5: Duplicate Customer Emails (same person, many orders) ---
fraud_email = "suspicious.buyer@fakeemail.com"
for i in range(7):
    idx = random.randint(0, len(orders) - 1)
    orders[idx]['customer_email'] = fraud_email
    orders[idx]['customer_name'] = "Juan Suspicious"

# ============================================================
# SAVE TO CSV
# ============================================================
df = pd.DataFrame(orders)
df.to_csv('shopify_orders.csv', index=False)
print(f"✅ Generated {len(df)} orders → shopify_orders.csv")
print(f"   Columns: {list(df.columns)}")