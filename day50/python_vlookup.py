import pandas as pd

# 1. Read the CSV files into DataFrames
customers_df = pd.read_csv('customers.csv')
orders_df = pd.read_csv('orders.csv')

print("--- Customers Table ---")
print(customers_df.head())
print("\n--- Orders Table ---")
print(orders_df.head())

# 2. Perform the "VLOOKUP" (Merge/Join)
# We want to add Customer info to the Orders table, matching on 'CustomerID'
# how='left' keeps all orders, even if a customer is missing (similar to VLOOKUP)
merged_df = pd.merge(orders_df, customers_df, on='CustomerID', how='left')

print("\n--- Merged Table (Orders + Customer Info) ---")
print(merged_df)

# Optional: Save the result to a new CSV
merged_df.to_csv('merged_orders.csv', index=False)
print("\nSaved merged data to 'merged_orders.csv'")
