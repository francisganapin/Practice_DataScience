# ============================================================================
# SALES DATA ANALYSIS - NUMPY & PANDAS PRACTICE
# ============================================================================
# This file contains exercises to help you learn NumPy, Pandas, and concepts
# that also apply to Excel. Each section has PROBLEMS followed by SOLUTIONS.
# Try to solve the problems yourself before looking at the solutions!
# ============================================================================

import numpy as np
import pandas as pd

# Load the sales data
df = pd.read_csv('sales_data.csv')

# ============================================================================
# SECTION 1: BASIC DATA EXPLORATION (Like opening a file in Excel)
# ============================================================================
print("=" * 60)
print("SECTION 1: BASIC DATA EXPLORATION")
print("=" * 60)

# PROBLEM 1.1: Display the first 5 rows (like scrolling to top in Excel)
# YOUR CODE HERE:


# SOLUTION 1.1:
print("\n--- First 5 rows ---")
print(df.head())

# PROBLEM 1.2: Display the last 5 rows
# YOUR CODE HERE:


# SOLUTION 1.2:
print("\n--- Last 5 rows ---")
print(df.tail())

# PROBLEM 1.3: Get the shape of the data (rows x columns - like checking Excel dimensions)
# YOUR CODE HERE:


# SOLUTION 1.3:
print(f"\n--- Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns ---")

# PROBLEM 1.4: Get column names (like seeing column headers in Excel)
# YOUR CODE HERE:


# SOLUTION 1.4:
print("\n--- Column Names ---")
print(df.columns.tolist())

# PROBLEM 1.5: Get data types for each column
# YOUR CODE HERE:


# SOLUTION 1.5:
print("\n--- Data Types ---")
print(df.dtypes)

# PROBLEM 1.6: Get a statistical summary (like using Excel's Data Analysis ToolPak)
# YOUR CODE HERE:


# SOLUTION 1.6:
print("\n--- Statistical Summary ---")
print(df.describe())


# ============================================================================
# SECTION 2: SELECTING DATA (Like selecting cells/columns in Excel)
# ============================================================================
print("\n" + "=" * 60)
print("SECTION 2: SELECTING DATA")
print("=" * 60)

# PROBLEM 2.1: Select only the 'product_name' column
# YOUR CODE HERE:


# SOLUTION 2.1:
print("\n--- Product Names ---")
print(df['product_name'])

# PROBLEM 2.2: Select multiple columns: product_name, quantity, total_amount
# YOUR CODE HERE:


# SOLUTION 2.2:
print("\n--- Selected Columns ---")
print(df[['product_name', 'quantity', 'total_amount']])

# PROBLEM 2.3: Select rows 5 to 10 (like selecting row range in Excel)
# YOUR CODE HERE:


# SOLUTION 2.3:
print("\n--- Rows 5 to 10 ---")
print(df.iloc[5:11])  # iloc uses 0-based indexing, 11 is exclusive

# PROBLEM 2.4: Select a specific cell (row 3, column 'customer_name')
# YOUR CODE HERE:


# SOLUTION 2.4:
print(f"\n--- Specific Cell (Row 3, customer_name): {df.loc[3, 'customer_name']} ---")


# ============================================================================
# SECTION 3: FILTERING DATA (Like using Excel's Filter feature)
# ============================================================================
print("\n" + "=" * 60)
print("SECTION 3: FILTERING DATA")
print("=" * 60)

# PROBLEM 3.1: Filter all Electronics products
# YOUR CODE HERE:


# SOLUTION 3.1:
print("\n--- Electronics Products ---")
electronics = df[df['category'] == 'Electronics']
print(electronics)

# PROBLEM 3.2: Filter orders where total_amount > 500
# YOUR CODE HERE:


# SOLUTION 3.2:
print("\n--- Orders > $500 ---")
high_value = df[df['total_amount'] > 500]
print(high_value)

# PROBLEM 3.3: Filter orders from the 'North' region with quantity > 5
# YOUR CODE HERE:


# SOLUTION 3.3:
print("\n--- North Region, Quantity > 5 ---")
north_high_qty = df[(df['region'] == 'North') & (df['quantity'] > 5)]
print(north_high_qty)

# PROBLEM 3.4: Filter orders paid with either 'Credit Card' or 'PayPal'
# YOUR CODE HERE:


# SOLUTION 3.4:
print("\n--- Credit Card or PayPal Payments ---")
card_paypal = df[df['payment_method'].isin(['Credit Card', 'PayPal'])]
print(card_paypal.head(10))


# ============================================================================
# SECTION 4: SORTING DATA (Like Excel's Sort feature)
# ============================================================================
print("\n" + "=" * 60)
print("SECTION 4: SORTING DATA")
print("=" * 60)

# PROBLEM 4.1: Sort by total_amount (highest first)
# YOUR CODE HERE:


# SOLUTION 4.1:
print("\n--- Sorted by Total Amount (Descending) ---")
sorted_by_amount = df.sort_values('total_amount', ascending=False)
print(sorted_by_amount.head(10))

# PROBLEM 4.2: Sort by date (earliest first), then by total_amount (highest first)
# YOUR CODE HERE:


# SOLUTION 4.2:
print("\n--- Sorted by Date, then Total Amount ---")
multi_sort = df.sort_values(['date', 'total_amount'], ascending=[True, False])
print(multi_sort.head(10))


# ============================================================================
# SECTION 5: AGGREGATION (Like Excel's SUM, AVERAGE, COUNT, MIN, MAX)
# ============================================================================
print("\n" + "=" * 60)
print("SECTION 5: AGGREGATION")
print("=" * 60)

# PROBLEM 5.1: Calculate total sales (SUM of total_amount)
# YOUR CODE HERE:


# SOLUTION 5.1:
total_sales = df['total_amount'].sum()
print(f"\n--- Total Sales: ${total_sales:,.2f} ---")

# PROBLEM 5.2: Calculate average order value
# YOUR CODE HERE:


# SOLUTION 5.2:
avg_order = df['total_amount'].mean()
print(f"--- Average Order Value: ${avg_order:,.2f} ---")

# PROBLEM 5.3: Find the maximum and minimum order amounts
# YOUR CODE HERE:


# SOLUTION 5.3:
max_order = df['total_amount'].max()
min_order = df['total_amount'].min()
print(f"--- Max Order: ${max_order:,.2f}, Min Order: ${min_order:,.2f} ---")

# PROBLEM 5.4: Count total number of orders
# YOUR CODE HERE:


# SOLUTION 5.4:
order_count = df['order_id'].count()
print(f"--- Total Orders: {order_count} ---")

# PROBLEM 5.5: Count unique products sold
# YOUR CODE HERE:


# SOLUTION 5.5:
unique_products = df['product_name'].nunique()
print(f"--- Unique Products Sold: {unique_products} ---")


# ============================================================================
# SECTION 6: GROUPBY (Like Excel Pivot Tables!)
# ============================================================================
print("\n" + "=" * 60)
print("SECTION 6: GROUPBY (Excel Pivot Table Equivalent)")
print("=" * 60)

# PROBLEM 6.1: Total sales by category
# YOUR CODE HERE:


# SOLUTION 6.1:
print("\n--- Total Sales by Category ---")
sales_by_category = df.groupby('category')['total_amount'].sum()
print(sales_by_category)

# PROBLEM 6.2: Total sales by region
# YOUR CODE HERE:


# SOLUTION 6.2:
print("\n--- Total Sales by Region ---")
sales_by_region = df.groupby('region')['total_amount'].sum().sort_values(ascending=False)
print(sales_by_region)

# PROBLEM 6.3: Sales by salesperson (count and total amount)
# YOUR CODE HERE:


# SOLUTION 6.3:
print("\n--- Sales by Salesperson ---")
sales_by_person = df.groupby('salesperson').agg({
    'order_id': 'count',
    'total_amount': 'sum'
}).rename(columns={'order_id': 'num_orders', 'total_amount': 'total_sales'})
print(sales_by_person)

# PROBLEM 6.4: Average order value by region
# YOUR CODE HERE:


# SOLUTION 6.4:
print("\n--- Average Order Value by Region ---")
avg_by_region = df.groupby('region')['total_amount'].mean()
print(avg_by_region)

# PROBLEM 6.5: Sales by Category and Region (like a 2D Pivot Table)
# YOUR CODE HERE:


# SOLUTION 6.5:
print("\n--- Sales by Category and Region ---")
pivot = df.pivot_table(
    values='total_amount',
    index='category',
    columns='region',
    aggfunc='sum',
    fill_value=0
)
print(pivot)


# ============================================================================
# SECTION 7: NUMPY OPERATIONS (Math operations on arrays)
# ============================================================================
print("\n" + "=" * 60)
print("SECTION 7: NUMPY OPERATIONS")
print("=" * 60)

# Convert columns to NumPy arrays for NumPy practice
quantities = df['quantity'].to_numpy()
unit_prices = df['unit_price'].to_numpy()
totals = df['total_amount'].to_numpy()

# PROBLEM 7.1: Calculate mean, median, std of quantities using NumPy
# YOUR CODE HERE:


# SOLUTION 7.1:
print("\n--- Quantity Statistics (NumPy) ---")
print(f"Mean: {np.mean(quantities):.2f}")
print(f"Median: {np.median(quantities):.2f}")
print(f"Std Dev: {np.std(quantities):.2f}")

# PROBLEM 7.2: Find orders where quantity is above average
# YOUR CODE HERE:


# SOLUTION 7.2:
avg_qty = np.mean(quantities)
above_avg_mask = quantities > avg_qty
print(f"\n--- Orders with Above Average Quantity ({avg_qty:.1f}) ---")
print(f"Count: {np.sum(above_avg_mask)}")
print(f"Order IDs: {df.loc[above_avg_mask, 'order_id'].tolist()[:5]}...")  # First 5

# PROBLEM 7.3: Calculate the percentile ranks (25th, 50th, 75th) of total_amount
# YOUR CODE HERE:


# SOLUTION 7.3:
print("\n--- Total Amount Percentiles ---")
p25 = np.percentile(totals, 25)
p50 = np.percentile(totals, 50)
p75 = np.percentile(totals, 75)
print(f"25th Percentile: ${p25:,.2f}")
print(f"50th Percentile (Median): ${p50:,.2f}")
print(f"75th Percentile: ${p75:,.2f}")

# PROBLEM 7.4: Create a new array that calculates revenue per unit
# YOUR CODE HERE:


# SOLUTION 7.4:
revenue_per_unit = totals / quantities
print("\n--- Average Revenue Per Unit (First 10) ---")
for i in range(10):
    print(f"Order {df.iloc[i]['order_id']}: ${revenue_per_unit[i]:.2f}/unit")


# ============================================================================
# SECTION 8: CREATING NEW COLUMNS (Like adding formulas in Excel)
# ============================================================================
print("\n" + "=" * 60)
print("SECTION 8: CREATING NEW COLUMNS")
print("=" * 60)

# PROBLEM 8.1: Create a column for discount amount
# YOUR CODE HERE:


# SOLUTION 8.1:
df['discount_amount'] = df['total_amount'] * df['discount_percent'] / 100
print("\n--- Discount Amount Column Added ---")
print(df[['product_name', 'total_amount', 'discount_percent', 'discount_amount']].head())

# PROBLEM 8.2: Create a column for net amount (after discount)
# YOUR CODE HERE:


# SOLUTION 8.2:
df['net_amount'] = df['total_amount'] - df['discount_amount']
print("\n--- Net Amount Column Added ---")
print(df[['product_name', 'total_amount', 'discount_amount', 'net_amount']].head())

# PROBLEM 8.3: Create a column categorizing orders as 'Low', 'Medium', 'High' value
# Low: < 400, Medium: 400-800, High: > 800
# YOUR CODE HERE:


# SOLUTION 8.3:
def categorize_order(amount):
    if amount < 400:
        return 'Low'
    elif amount <= 800:
        return 'Medium'
    else:
        return 'High'

df['value_category'] = df['total_amount'].apply(categorize_order)
print("\n--- Value Categories ---")
print(df['value_category'].value_counts())


# ============================================================================
# SECTION 9: DATE OPERATIONS (Like Excel date functions)
# ============================================================================
print("\n" + "=" * 60)
print("SECTION 9: DATE OPERATIONS")
print("=" * 60)

# PROBLEM 9.1: Convert date column to datetime type
# YOUR CODE HERE:


# SOLUTION 9.1:
df['date'] = pd.to_datetime(df['date'])
print(f"\n--- Date column type: {df['date'].dtype} ---")

# PROBLEM 9.2: Extract month and day of week from date
# YOUR CODE HERE:


# SOLUTION 9.2:
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.day_name()
print("\n--- Month and Day of Week ---")
print(df[['date', 'month', 'day_of_week']].head(10))

# PROBLEM 9.3: Total sales by month
# YOUR CODE HERE:


# SOLUTION 9.3:
print("\n--- Total Sales by Month ---")
monthly_sales = df.groupby('month')['total_amount'].sum()
print(monthly_sales)


# ============================================================================
# SECTION 10: EXPORT DATA (Like Save As in Excel)
# ============================================================================
print("\n" + "=" * 60)
print("SECTION 10: EXPORT DATA")
print("=" * 60)

# PROBLEM 10.1: Export the enhanced dataframe to a new CSV
# YOUR CODE HERE:


# SOLUTION 10.1:
df.to_csv('sales_data_enhanced.csv', index=False)
print("\n--- Exported to sales_data_enhanced.csv ---")

# PROBLEM 10.2: Export to Excel format
# YOUR CODE HERE:


# SOLUTION 10.2:
# Note: This requires openpyxl: pip install openpyxl
try:
    df.to_excel('sales_report.xlsx', index=False, sheet_name='Sales Data')
    print("--- Exported to sales_report.xlsx ---")
except ImportError:
    print("--- Install openpyxl to export to Excel: pip install openpyxl ---")


# ============================================================================
# BONUS CHALLENGES
# ============================================================================
print("\n" + "=" * 60)
print("BONUS CHALLENGES")
print("=" * 60)

# BONUS 1: Find the top 3 best-selling products by quantity
print("\n--- Top 3 Products by Quantity ---")
top_products = df.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(3)
print(top_products)

# BONUS 2: Calculate the sales performance rating for each salesperson
# Rating = (Individual Sales / Total Sales) * 100
print("\n--- Salesperson Performance ---")
total_sales = df['total_amount'].sum()
performance = df.groupby('salesperson')['total_amount'].sum() / total_sales * 100
print(performance.round(2))

# BONUS 3: Find the most popular payment method by region
print("\n--- Most Popular Payment Method by Region ---")
payment_by_region = df.groupby(['region', 'payment_method']).size().unstack(fill_value=0)
print(payment_by_region)

print("\n" + "=" * 60)
print("PRACTICE COMPLETE!")
print("=" * 60)
