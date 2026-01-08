# E-Commerce Business Analysis Questions

## Question 1: What is our total revenue for the period?

**Boss Question:** "I need to know our total revenue. How much money did we make from all orders?"

### Solution
```python
import pandas as pd

df = pd.read_csv('ecommerce_data.csv')

# Calculate total revenue (excluding cancelled orders)
total_revenue = df[df['order_status'] != 'Cancelled']['total_amount'].sum()
print(f"Total Revenue: ${total_revenue:,.2f}")
```

**Expected Output:** `Total Revenue: $10,279.79`

### Why We Need This
Understanding total revenue is fundamental to measuring business performance. It helps:
- Track growth over time
- Set realistic targets for sales teams
- Make informed decisions about inventory and marketing budgets
- Report to stakeholders and investors
- Calculate profit margins when combined with cost data

---

## Question 2: Which product category generates the most revenue?

**Boss Question:** "Where is our money coming from? Which category should we focus our marketing efforts on?"

### Solution
```python
import pandas as pd

df = pd.read_csv('ecommerce_data.csv')

# Group by category and sum revenue
category_revenue = df[df['order_status'] != 'Cancelled'].groupby('category')['total_amount'].sum().sort_values(ascending=False)
print(category_revenue)

# Visualize
import matplotlib.pyplot as plt
category_revenue.plot(kind='bar', color='steelblue')
plt.title('Revenue by Product Category')
plt.ylabel('Revenue ($)')
plt.xlabel('Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Why We Need This
Identifying top-performing categories helps:
- Allocate marketing budget effectively
- Optimize inventory management (stock more of what sells)
- Identify cross-selling opportunities
- Make strategic decisions about product expansion
- Understand customer preferences and market trends

---

## Question 3: What is the average order value (AOV)?

**Boss Question:** "What's the typical amount a customer spends per order? Are we maximizing each transaction?"

### Solution
```python
import pandas as pd

df = pd.read_csv('ecommerce_data.csv')

# Calculate average order value
aov = df[df['order_status'] != 'Cancelled']['total_amount'].mean()
print(f"Average Order Value: ${aov:.2f}")
```

**Expected Output:** `Average Order Value: $209.79`

### Why We Need This
Average Order Value (AOV) is a critical metric because:
- It measures customer spending behavior
- Helps set minimum order thresholds for free shipping
- Identifies opportunities for upselling and cross-selling
- Tracks the effectiveness of bundling strategies
- Benchmarks performance against industry standards
- Directly impacts profitability (higher AOV = better margins)

---

## Question 4: Who are our top 5 customers by total spending?

**Boss Question:** "Who are our VIP customers? We need to know who to prioritize for our loyalty program."

### Solution
```python
import pandas as pd

df = pd.read_csv('ecommerce_data.csv')

# Group by customer and sum their total spending
top_customers = df[df['order_status'] != 'Cancelled'].groupby(['customer_id', 'customer_name'])['total_amount'].sum().sort_values(ascending=False).head(5)
print("Top 5 Customers by Spending:")
print(top_customers)
```

### Why We Need This
Identifying top customers is crucial for:
- **80/20 Rule**: Often 20% of customers generate 80% of revenue
- Designing targeted loyalty programs and VIP perks
- Personalizing marketing campaigns
- Reducing churn risk (losing a top customer is costly)
- Allocating customer service resources effectively
- Creating case studies and testimonials

---

## Question 5: What is our order cancellation rate?

**Boss Question:** "How many orders are we losing? This is costing us money and we need to understand why."

### Solution
```python
import pandas as pd

df = pd.read_csv('ecommerce_data.csv')

# Calculate cancellation rate
total_orders = len(df)
cancelled_orders = len(df[df['order_status'] == 'Cancelled'])
cancellation_rate = (cancelled_orders / total_orders) * 100

print(f"Total Orders: {total_orders}")
print(f"Cancelled Orders: {cancelled_orders}")
print(f"Cancellation Rate: {cancellation_rate:.2f}%")
```

**Expected Output:** `Cancellation Rate: 2.00%`

### Why We Need This
Monitoring cancellation rates helps:
- Identify operational problems (stock issues, payment failures)
- Measure customer satisfaction
- Calculate actual vs. projected revenue
- Improve checkout process and user experience
- Detect fraud patterns
- Set realistic sales forecasts
- **Financial Impact**: Even a 2% cancellation rate can mean thousands in lost revenue

---

## Question 6: What is the average shipping cost and how does it impact profit margins?

**Boss Question:** "Shipping is eating into our profits. What are we actually spending on average, and which orders are most expensive to ship?"

### Solution
```python
import pandas as pd

df = pd.read_csv('ecommerce_data.csv')

# Calculate average shipping cost
avg_shipping = df[df['order_status'] != 'Cancelled']['shipping_cost'].mean()
total_shipping = df[df['order_status'] != 'Cancelled']['shipping_cost'].sum()

# Calculate shipping as percentage of revenue
shipping_percentage = (total_shipping / df[df['order_status'] != 'Cancelled']['total_amount'].sum()) * 100

print(f"Average Shipping Cost: ${avg_shipping:.2f}")
print(f"Total Shipping Cost: ${total_shipping:.2f}")
print(f"Shipping as % of Revenue: {shipping_percentage:.2f}%")

# Find categories with highest shipping costs
category_shipping = df[df['order_status'] != 'Cancelled'].groupby('category')['shipping_cost'].mean().sort_values(ascending=False)
print("\nAverage Shipping Cost by Category:")
print(category_shipping)
```

### Why We Need This
Understanding shipping costs is vital because:
- Shipping directly impacts profit margins
- Helps set competitive yet profitable shipping rates
- Identifies opportunities for negotiating better carrier rates
- Informs decisions about free shipping thresholds
- Reveals which products/categories are most expensive to ship
- Helps optimize warehouse locations and fulfillment strategies
- **Example**: If shipping is 15% of revenue, reducing it by 3% can significantly boost profits

---

## Question 7: Which payment method is most popular?

**Boss Question:** "Are customers using the payment methods we're promoting? Should we add or remove any options?"

### Solution
```python
import pandas as pd

df = pd.read_csv('ecommerce_data.csv')

# Count orders by payment method
payment_methods = df[df['order_status'] != 'Cancelled']['payment_method'].value_counts()
payment_percentage = (payment_methods / payment_methods.sum()) * 100

print("Orders by Payment Method:")
for method, count in payment_methods.items():
    print(f"{method}: {count} orders ({payment_percentage[method]:.1f}%)")

# Visualize
import matplotlib.pyplot as plt
payment_methods.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Payment Method Distribution')
plt.ylabel('')
plt.show()
```

### Why We Need This
Analyzing payment methods helps:
- Reduce transaction fees (some methods cost more than others)
- Improve checkout conversion (customers abandon if preferred method unavailable)
- Identify security concerns (certain methods have higher fraud rates)
- Negotiate better rates with payment processors
- Target demographics (younger users prefer digital wallets, older prefer cards)
- Comply with regional preferences (PayPal popular in some countries)
- **Business Impact**: Adding a popular payment method can increase conversions by 10-30%

---

## Question 8: What is the average delivery time?

**Boss Question:** "How fast are we getting products to customers? Speed matters for customer satisfaction."

### Solution
```python
import pandas as pd

df = pd.read_csv('ecommerce_data.csv')

# Convert date columns to datetime
df['order_date'] = pd.to_datetime(df['order_date'])
df['delivery_date'] = pd.to_datetime(df['delivery_date'])

# Calculate delivery time in days
df['delivery_days'] = (df['delivery_date'] - df['order_date']).dt.days

# Calculate average delivery time for delivered orders
avg_delivery = df[df['order_status'] == 'Delivered']['delivery_days'].mean()
print(f"Average Delivery Time: {avg_delivery:.1f} days")

# Breakdown by category
category_delivery = df[df['order_status'] == 'Delivered'].groupby('category')['delivery_days'].mean().sort_values()
print("\nAverage Delivery Time by Category:")
print(category_delivery)
```

### Why We Need This
Delivery time analysis is critical because:
- **Customer Satisfaction**: Fast delivery = happy customers = repeat business
- Competitive advantage (Amazon Prime set 2-day standard)
- Identifies bottlenecks in fulfillment process
- Helps set realistic delivery promises
- Reveals which products/categories take longer
- Impacts return rates (longer wait = higher returns)
- **Statistics**: 25% of customers abandon carts due to slow delivery times

---

## Question 9: Which states/cities generate the most revenue?

**Boss Question:** "Where are our best customers located? We need to know where to focus our regional marketing."

### Solution
```python
import pandas as pd

df = pd.read_csv('ecommerce_data.csv')

# Top 5 states by revenue
state_revenue = df[df['order_status'] != 'Cancelled'].groupby('state')['total_amount'].sum().sort_values(ascending=False).head(5)
print("Top 5 States by Revenue:")
print(state_revenue)

# Top 5 cities by revenue
city_revenue = df[df['order_status'] != 'Cancelled'].groupby('city')['total_amount'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Cities by Revenue:")
print(city_revenue)
```

### Why We Need This
Geographic analysis helps:
- Target local advertising and promotions
- Optimize warehouse and distribution center locations
- Identify expansion opportunities
- Understand regional preferences
- Plan inventory based on regional demand
- Negotiate better shipping rates in high-volume areas
- Tailor marketing messages to local culture
- **Strategic Value**: Opening a warehouse in a high-revenue state can reduce shipping costs by 20-40%

---

## Question 10: What is the return rate and which products are returned most?

**Boss Question:** "Returns are killing our profits. How bad is it, and what products are causing the problem?"

### Solution
```python
import pandas as pd

df = pd.read_csv('ecommerce_data.csv')

# Calculate return rate
total_delivered = len(df[df['order_status'] == 'Delivered'])
total_returns = len(df[(df['order_status'] == 'Delivered') & (df['return_status'] == 'Yes')])
return_rate = (total_returns / total_delivered) * 100

print(f"Total Delivered Orders: {total_delivered}")
print(f"Returned Orders: {total_returns}")
print(f"Return Rate: {return_rate:.2f}%")

# Products with returns
returned_products = df[(df['order_status'] == 'Delivered') & (df['return_status'] == 'Yes')][['product_name', 'category', 'total_amount']]
print("\nReturned Products:")
print(returned_products)

# Return rate by category
category_returns = df[df['order_status'] == 'Delivered'].groupby('category')['return_status'].apply(lambda x: (x == 'Yes').sum() / len(x) * 100)
print("\nReturn Rate by Category:")
print(category_returns)
```

### Why We Need This
Return rate analysis is crucial because:
- **Financial Impact**: Returns cost 2-3x the original shipping cost
- Identifies quality issues with specific products
- Reveals problems with product descriptions (expectations vs. reality)
- Helps improve sizing guides and product photos
- Impacts inventory management (returned items may not be resellable)
- Affects customer lifetime value (high returners are less profitable)
- Industry benchmark: 5-10% is normal, >15% is concerning
- **Action**: High return rates may require supplier changes or product discontinuation

---

## Question 11: What is the revenue contribution by customer segment?

**Boss Question:** "Are Premium customers really worth the extra effort? Show me the numbers."

### Solution
```python
import pandas as pd

df = pd.read_csv('ecommerce_data.csv')

# Revenue by customer segment
segment_revenue = df[df['order_status'] != 'Cancelled'].groupby('customer_segment')['total_amount'].agg(['sum', 'mean', 'count'])
segment_revenue.columns = ['Total Revenue', 'Avg Order Value', 'Order Count']
segment_revenue['Revenue %'] = (segment_revenue['Total Revenue'] / segment_revenue['Total Revenue'].sum()) * 100

print("Revenue by Customer Segment:")
print(segment_revenue)

# Visualize
import matplotlib.pyplot as plt
segment_revenue['Total Revenue'].plot(kind='bar', color=['gold', 'silver'])
plt.title('Revenue by Customer Segment')
plt.ylabel('Total Revenue ($)')
plt.xlabel('Customer Segment')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
```

### Why We Need This
Customer segmentation analysis helps:
- Validate the value of premium/loyalty programs
- Allocate customer service resources appropriately
- Design targeted marketing campaigns
- Set appropriate discount strategies for each segment
- Identify opportunities to upgrade regular customers to premium
- Measure ROI of premium customer perks
- **Business Decision**: If premium customers generate 70% of revenue, they deserve priority support and exclusive offers

---

## Question 12: What is the discount impact on revenue?

**Boss Question:** "We're giving away too many discounts. How much revenue are we losing, and is it worth it?"

### Solution
```python
import pandas as pd
import numpy as np

df = pd.read_csv('ecommerce_data.csv')

# Calculate discount amount
df['discount_amount'] = df['total_amount'] * (df['discount_percent'] / 100)
df['revenue_before_discount'] = df['total_amount'] + df['discount_amount']

# Total discount given
total_discount = df[df['order_status'] != 'Cancelled']['discount_amount'].sum()
total_revenue = df[df['order_status'] != 'Cancelled']['total_amount'].sum()
discount_percentage = (total_discount / (total_revenue + total_discount)) * 100

print(f"Total Discounts Given: ${total_discount:,.2f}")
print(f"Discount as % of Potential Revenue: {discount_percentage:.2f}%")

# Orders with vs without discounts
orders_with_discount = len(df[(df['order_status'] != 'Cancelled') & (df['discount_percent'] > 0)])
orders_without_discount = len(df[(df['order_status'] != 'Cancelled') & (df['discount_percent'] == 0)])

print(f"\nOrders with Discount: {orders_with_discount}")
print(f"Orders without Discount: {orders_without_discount}")

# Average order value with vs without discount
avg_with_discount = df[(df['order_status'] != 'Cancelled') & (df['discount_percent'] > 0)]['total_amount'].mean()
avg_without_discount = df[(df['order_status'] != 'Cancelled') & (df['discount_percent'] == 0)]['total_amount'].mean()

print(f"\nAvg Order Value (with discount): ${avg_with_discount:.2f}")
print(f"Avg Order Value (without discount): ${avg_without_discount:.2f}")
```

### Why We Need This
Discount analysis is essential because:
- Measures the true cost of promotional campaigns
- Determines if discounts actually drive higher order values
- Identifies if we're training customers to wait for sales
- Helps optimize discount strategies (% vs. $ off, minimum thresholds)
- Reveals margin erosion
- Compares discount effectiveness across segments
- **Critical Insight**: If discounted orders have lower AOV, the strategy may be counterproductive
- **Profitability**: Every 1% discount reduction can significantly boost profit margins

---

## Question 13: What is the monthly revenue trend?

**Boss Question:** "Are we growing or declining? I need to see the trend over time."

### Solution
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ecommerce_data.csv')

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Extract month and year
df['month'] = df['order_date'].dt.to_period('M')

# Calculate monthly revenue
monthly_revenue = df[df['order_status'] != 'Cancelled'].groupby('month')['total_amount'].sum()

print("Monthly Revenue:")
print(monthly_revenue)

# Visualize trend
monthly_revenue.plot(kind='line', marker='o', color='green', linewidth=2)
plt.title('Monthly Revenue Trend')
plt.ylabel('Revenue ($)')
plt.xlabel('Month')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Calculate growth rate
monthly_revenue_values = monthly_revenue.values
growth_rates = [(monthly_revenue_values[i] - monthly_revenue_values[i-1]) / monthly_revenue_values[i-1] * 100 
                for i in range(1, len(monthly_revenue_values))]
print(f"\nAverage Monthly Growth Rate: {sum(growth_rates)/len(growth_rates):.2f}%")
```

### Why We Need This
Trend analysis is vital for:
- **Strategic Planning**: Identifying growth or decline patterns
- Forecasting future revenue
- Detecting seasonality (holiday spikes, summer slumps)
- Measuring impact of marketing campaigns
- Setting realistic targets for sales teams
- Identifying when to scale operations (hiring, inventory)
- Investor reporting and fundraising
- **Early Warning**: Declining trends allow proactive intervention
- **Opportunity**: Growth trends justify expansion investments

---

## Question 14: Which products have the highest quantity sold?

**Boss Question:** "What are our best-sellers by volume? We need to make sure we never run out of stock on these."

### Solution
```python
import pandas as pd

df = pd.read_csv('ecommerce_data.csv')

# Total quantity sold by product
product_quantity = df[df['order_status'] != 'Cancelled'].groupby(['product_name', 'category'])['quantity'].sum().sort_values(ascending=False).head(10)

print("Top 10 Products by Quantity Sold:")
print(product_quantity)

# Visualize
import matplotlib.pyplot as plt
product_quantity.plot(kind='barh', color='coral')
plt.title('Top 10 Products by Quantity Sold')
plt.xlabel('Quantity Sold')
plt.ylabel('Product')
plt.tight_layout()
plt.show()
```

### Why We Need This
Volume analysis helps:
- **Inventory Management**: Prevent stockouts on popular items
- Identify products to feature in marketing
- Negotiate better supplier rates (bulk discounts)
- Optimize warehouse space allocation
- Plan production schedules (for manufactured goods)
- Identify bundling opportunities
- **Customer Satisfaction**: Stockouts = lost sales + frustrated customers
- **Revenue Protection**: Top sellers often generate 40-60% of total revenue

---

## Question 15: What is the customer lifetime value (CLV) for repeat customers?

**Boss Question:** "How valuable are repeat customers? Should we invest more in retention programs?"

### Solution
```python
import pandas as pd

df = pd.read_csv('ecommerce_data.csv')

# Identify repeat customers (more than 1 order)
customer_orders = df[df['order_status'] != 'Cancelled'].groupby('customer_id').agg({
    'order_id': 'count',
    'total_amount': 'sum'
}).rename(columns={'order_id': 'order_count', 'total_amount': 'total_spent'})

# Separate repeat vs one-time customers
repeat_customers = customer_orders[customer_orders['order_count'] > 1]
onetime_customers = customer_orders[customer_orders['order_count'] == 1]

print(f"Total Customers: {len(customer_orders)}")
print(f"Repeat Customers: {len(repeat_customers)} ({len(repeat_customers)/len(customer_orders)*100:.1f}%)")
print(f"One-time Customers: {len(onetime_customers)} ({len(onetime_customers)/len(customer_orders)*100:.1f}%)")

print(f"\nAverage Lifetime Value (Repeat Customers): ${repeat_customers['total_spent'].mean():.2f}")
print(f"Average Lifetime Value (One-time Customers): ${onetime_customers['total_spent'].mean():.2f}")

print(f"\nTotal Revenue from Repeat Customers: ${repeat_customers['total_spent'].sum():,.2f}")
print(f"Total Revenue from One-time Customers: ${onetime_customers['total_spent'].sum():,.2f}")

# Show top repeat customers
print("\nTop 5 Repeat Customers:")
print(repeat_customers.sort_values('total_spent', ascending=False).head())
```

### Why We Need This
Customer Lifetime Value (CLV) analysis is critical because:
- **Retention ROI**: Acquiring new customers costs 5-25x more than retaining existing ones
- Justifies investment in loyalty programs
- Identifies most valuable customer relationships
- Helps set customer acquisition cost (CAC) budgets
- Reveals the importance of customer service quality
- Guides email marketing and retargeting strategies
- **Profitability**: Repeat customers typically have 60-70% higher conversion rates
- **Strategic Focus**: If repeat customers generate majority of revenue, retention > acquisition
- **Benchmarking**: Industry standard is 20-30% repeat customer rate

---

## Summary

These 15 questions cover the essential metrics every e-commerce business needs to monitor:

1. **Revenue Metrics**: Total revenue, AOV, monthly trends
2. **Customer Insights**: Top customers, segments, CLV, repeat rates
3. **Product Performance**: Category revenue, best-sellers, returns
4. **Operational Efficiency**: Delivery time, shipping costs, cancellation rate
5. **Marketing Effectiveness**: Discount impact, geographic distribution, payment preferences

**Key Takeaway**: Data-driven decisions lead to better business outcomes. Regular analysis of these metrics helps identify opportunities, prevent problems, and maximize profitability.
