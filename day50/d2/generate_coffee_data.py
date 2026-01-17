import csv
import random
from datetime import datetime, timedelta

def generate_coffee_data():
    locations = ["Makati", "Manila", "Caloocan"]
    
    products = {
        "Coffee": [
            ("Espresso", 120), ("Americano", 130), ("Cappuccino", 150), 
            ("Latte", 160), ("Caramel Macchiato", 170), ("Mocha", 170)
        ],
        "Tea": [
            ("Green Tea", 110), ("Black Tea", 110), ("Chamomile Tea", 120), 
            ("Matcha Latte", 180), ("Iced Lemon Tea", 130)
        ],
        "Bakery": [
            ("Croissant", 90), ("Bagel", 80), ("Blueberry Muffin", 95), 
            ("Chocolate Cookie", 70), ("Cinnamon Roll", 100)
        ],
        "Smoothies": [
            ("Mango Smoothie", 160), ("Strawberry Banana", 170), 
            ("Green Detox", 180), ("Chocolate Shake", 160)
        ]
    }
    
    data = []
    start_date = datetime.now() - timedelta(days=30)
    
    for i in range(1, 501):
        transaction_id = f"TRX-{i:04d}"
        
        # Random date and time
        random_days = random.randint(0, 30)
        date = start_date + timedelta(days=random_days)
        date_str = date.strftime("%Y-%m-%d")
        
        # Random time between 7 AM and 10 PM
        hour = random.randint(7, 21)
        minute = random.randint(0, 59)
        time_str = f"{hour:02d}:{minute:02d}"
        
        location = random.choice(locations)
        
        category = random.choice(list(products.keys()))
        product_name, price = random.choice(products[category])
        
        quantity = random.randint(1, 5)
        total_amount = price * quantity
        
        data.append([
            transaction_id, date_str, time_str, location, 
            category, product_name, price, quantity, total_amount
        ])

    headers = [
        "Transaction ID", "Date", "Time", "Location", 
        "Product Category", "Product Name", "Price", "Quantity", "Total Amount"
    ]

    with open('coffee_shop_sales.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

    print("Successfully generated coffee_shop_sales.csv with 500 entries.")

if __name__ == "__main__":
    generate_coffee_data()
