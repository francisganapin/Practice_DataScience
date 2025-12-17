# Sales Analysis Tutorial & Solutions

Here is the step-by-step guide to solving the homework challenges in `sales.md`.

## Exercise 1: Data Manipulation
**Task**: Change `num_orders` to 5000.

**Solution**:
Find the `generate_sales_data` function definition in the notebook and change the default value or the call.
```python
# In the cell calling the function:
df = generate_sales_data(num_orders=5000)

# Check new total revenue
print(f"New Total Revenue: ${df['Total Sales'].sum():,.2f}")
```

## Exercise 2: Category Analysis
**Task**: Highest average price per category.

**Solution**:
```python
# Group by Category and get the mean of Price
avg_price_cat = df.groupby('Category')['Price'].mean().sort_values(ascending=False)
print(avg_price_cat)
```

## Exercise 3: Time Series Deep Dive
**Task**: Weekly Sales Plot.

**Solution**:
```python
# Resample to Weekly ('W')
weekly_sales = df.set_index('Order Date')['Total Sales'].resample('W').sum()

# Plot
plt.figure(figsize=(12, 6))
plt.plot(weekly_sales, marker='o')
plt.title('Weekly Sales Trend')
plt.show()
```

## Exercise 4: Identifying "Whales" (Customer Pareto)
**Task**: Top customers generating revenue.

**Solution**:
```python
# Group by CustomerID
customer_sales = df.groupby('CustomerID')['Total Sales'].sum().sort_values(ascending=False)

# Calculate cumulative percentage
cum_sales = customer_sales.cumsum()
cum_pct = 100 * cum_sales / customer_sales.sum()

# Find how many customers make up 50% of revenue
top_50_pct_count = len(cum_pct[cum_pct <= 50])
print(f"{top_50_pct_count} customers account for 50% of total revenue.")
```

## Exercise 5: RFM Segmentation
**Task**: Find best customers (RFM Score 12).

**Solution**:
```python
# Assuming you have already run the RFM cell
best_customers = rfm[rfm['RFM_Score'] == 12]
print("Best Customers (IDs):", best_customers.index.tolist())
```

## Advanced Challenge: Heatmap
**Task**: Day of Week vs Hour Heatmap.

**Solution**:
```python
# Extract Hour
df['Hour'] = df['Order Date'].dt.hour

# Create Pivot Table
heatmap_data = df.pivot_table(index='DayOfWeek', columns='Hour', values='Total Sales', aggfunc='count')

# Reorder days
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
heatmap_data = heatmap_data.reindex(days)

# Plot
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=False)
plt.title('Orders Heatmap: Day vs Hour')
plt.show()
```
