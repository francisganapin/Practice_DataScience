# Real Estate Data Analysis: Boss's Questions & Solutions

## Introduction
As your manager in a real estate analytics firm, I need you to extract actionable insights from our property data. Each question below represents a real business need that will help us make better decisions, optimize our operations, and increase profitability. Understanding **why** we need these insights is just as important as knowing **how** to get them.

---

## Problem 1: What is our average commission per agent?

### Business Question
"I need to know which agents are generating the most commission revenue for our firm. Calculate the total and average commission earned by each agent."

### Solution
```python
import pandas as pd

# Load the data
df = pd.read_csv('real_estate_data.csv')

# Calculate commission for each sale
df['commission_earned'] = df['sale_price'] * df['commission_rate']

# Group by agent and calculate totals
agent_performance = df.groupby(['agent_id', 'agent_name']).agg({
    'commission_earned': ['sum', 'mean', 'count']
}).round(2)

agent_performance.columns = ['Total Commission', 'Avg Commission', 'Properties Sold']
agent_performance = agent_performance.sort_values('Total Commission', ascending=False)

print(agent_performance)
```

### Why This Matters
**Business Impact:** 
- **Compensation Planning:** Helps determine bonuses and incentives for top performers
- **Resource Allocation:** Identifies which agents need more support or training
- **Revenue Forecasting:** Understanding commission patterns helps predict future revenue
- **Performance Management:** Provides objective metrics for performance reviews

**Real-World Application:** In a competitive real estate market, knowing your top performers allows you to retain them with appropriate compensation and learn from their strategies to train other agents.

---

## Problem 2: Which property types have the highest profit margins?

### Business Question
"I want to know which property types (Single Family, Condo, Townhouse) are selling closest to their listing price. This tells us where we have the strongest negotiating position."

### Solution
```python
# Calculate the discount percentage (listing vs sale price)
df['discount_pct'] = ((df['listing_price'] - df['sale_price']) / df['listing_price'] * 100).round(2)

# Group by property type
property_analysis = df.groupby('property_type').agg({
    'discount_pct': 'mean',
    'sale_price': 'mean',
    'property_id': 'count'
}).round(2)

property_analysis.columns = ['Avg Discount %', 'Avg Sale Price', 'Count']
property_analysis = property_analysis.sort_values('Avg Discount %')

print(property_analysis)
```

### Why This Matters
**Business Impact:**
- **Marketing Strategy:** Focus marketing budget on property types with better margins
- **Inventory Decisions:** Guide clients on which property types to invest in
- **Pricing Strategy:** Understand market dynamics for different property types
- **Competitive Positioning:** Know where you have pricing power

**Real-World Application:** If condos consistently sell at 95% of listing price while single-family homes sell at 97%, you might want to specialize in single-family homes or adjust your condo pricing strategy.

---

## Problem 3: How does time on market correlate with sale price discount?

### Business Question
"Are properties that sit on the market longer selling for bigger discounts? I need to understand the relationship between days_on_market and the discount we're giving."

### Solution
```python
import numpy as np

# Calculate discount amount
df['discount_amount'] = df['listing_price'] - df['sale_price']
df['discount_pct'] = ((df['listing_price'] - df['sale_price']) / df['listing_price'] * 100)

# Create time buckets
df['market_time_category'] = pd.cut(df['days_on_market'], 
                                     bins=[0, 30, 45, 60, 100],
                                     labels=['Quick (0-30)', 'Normal (31-45)', 
                                            'Slow (46-60)', 'Very Slow (60+)'])

# Analyze by category
time_analysis = df.groupby('market_time_category').agg({
    'discount_pct': 'mean',
    'discount_amount': 'mean',
    'property_id': 'count'
}).round(2)

print(time_analysis)

# Correlation coefficient
correlation = df['days_on_market'].corr(df['discount_pct'])
print(f"\nCorrelation between days on market and discount: {correlation:.3f}")
```

### Why This Matters
**Business Impact:**
- **Pricing Optimization:** Set realistic initial prices to avoid long market times
- **Client Expectations:** Educate sellers about the cost of overpricing
- **Urgency Creation:** Develop strategies to create buyer urgency
- **Inventory Management:** Identify properties that need price adjustments

**Real-World Application:** If data shows that properties on the market for 60+ days sell at 5% discount vs 2% for properties sold in 30 days, you can quantify the cost of overpricing to clients—potentially saving them tens of thousands of dollars.

---

## Problem 4: What are the top 5 most profitable neighborhoods?

### Business Question
"I need to identify our most lucrative neighborhoods based on total sales volume and average property values. Where should we focus our agent recruitment and marketing efforts?"

### Solution
```python
# Analyze neighborhoods
neighborhood_stats = df.groupby('neighborhood').agg({
    'sale_price': ['sum', 'mean', 'count'],
    'commission_rate': 'mean'
}).round(2)

neighborhood_stats.columns = ['Total Sales Volume', 'Avg Sale Price', 'Properties Sold', 'Avg Commission Rate']

# Calculate estimated total commission
neighborhood_stats['Est. Total Commission'] = (
    neighborhood_stats['Total Sales Volume'] * neighborhood_stats['Avg Commission Rate']
).round(2)

# Sort by total sales volume
top_neighborhoods = neighborhood_stats.sort_values('Total Sales Volume', ascending=False).head(5)

print("Top 5 Most Profitable Neighborhoods:")
print(top_neighborhoods)
```

### Why This Matters
**Business Impact:**
- **Geographic Focus:** Concentrate resources in high-value areas
- **Agent Placement:** Assign experienced agents to lucrative neighborhoods
- **Marketing ROI:** Invest advertising budget where it generates most revenue
- **Market Expertise:** Develop specialized knowledge in profitable areas

**Real-World Application:** If West Atherton generates $4.6M in sales while other neighborhoods generate $1M, you'd want to have your best agents there and potentially open a satellite office in that area.

---

## Problem 5: Which property features command premium prices?

### Business Question
"I need to quantify the value of features like pools, garages, and high school ratings. What should we emphasize in our listings to justify higher prices?"

### Solution
```python
# Compare properties with and without key features
features_analysis = pd.DataFrame()

# Pool analysis
features_analysis.loc['Has Pool', 'Avg Sale Price'] = df[df['has_pool'] == 'Yes']['sale_price'].mean()
features_analysis.loc['No Pool', 'Avg Sale Price'] = df[df['has_pool'] == 'No']['sale_price'].mean()
features_analysis.loc['Pool Premium', 'Avg Sale Price'] = (
    features_analysis.loc['Has Pool', 'Avg Sale Price'] - 
    features_analysis.loc['No Pool', 'Avg Sale Price']
)

# Garage analysis
features_analysis.loc['Has Garage', 'Avg Sale Price'] = df[df['has_garage'] == 'Yes']['sale_price'].mean()
features_analysis.loc['No Garage', 'Avg Sale Price'] = df[df['has_garage'] == 'No']['sale_price'].mean()
features_analysis.loc['Garage Premium', 'Avg Sale Price'] = (
    features_analysis.loc['Has Garage', 'Avg Sale Price'] - 
    features_analysis.loc['No Garage', 'Avg Sale Price']
)

# School rating analysis (high vs low)
high_school = df[df['school_rating'] >= 9]['sale_price'].mean()
low_school = df[df['school_rating'] < 7]['sale_price'].mean()
features_analysis.loc['High School Rating (9+)', 'Avg Sale Price'] = high_school
features_analysis.loc['Low School Rating (<7)', 'Avg Sale Price'] = low_school
features_analysis.loc['School Rating Premium', 'Avg Sale Price'] = high_school - low_school

print(features_analysis.round(2))
```

### Why This Matters
**Business Impact:**
- **Listing Optimization:** Know which features to highlight in marketing materials
- **Valuation Accuracy:** Better estimate property values based on features
- **Client Advice:** Guide buyers on which features offer best value
- **Investment Recommendations:** Help sellers decide which improvements to make

**Real-World Application:** If a pool adds $500,000 to average sale price, you can advise sellers that installing a pool for $100,000 could yield a strong ROI. Conversely, if garages only add $50,000, it might not be worth a $75,000 installation.

---

## Problem 6: What is our sales velocity by city?

### Business Question
"I need to understand which cities have the fastest-moving inventory. This helps us predict cash flow and manage agent workload."

### Solution
```python
# Analyze sales velocity by city
city_velocity = df.groupby('city').agg({
    'days_on_market': ['mean', 'median'],
    'sale_price': 'mean',
    'property_id': 'count'
}).round(2)

city_velocity.columns = ['Avg Days on Market', 'Median Days on Market', 'Avg Sale Price', 'Properties Sold']
city_velocity = city_velocity.sort_values('Avg Days on Market')

# Calculate velocity score (lower is better)
city_velocity['Velocity Score'] = (city_velocity['Avg Days on Market'] / 
                                    city_velocity['Avg Days on Market'].max() * 100).round(2)

print("Cities Ranked by Sales Velocity (Fastest First):")
print(city_velocity)
```

### Why This Matters
**Business Impact:**
- **Cash Flow Forecasting:** Predict when commissions will be received
- **Inventory Management:** Know which markets move quickly
- **Agent Productivity:** Faster markets mean more transactions per agent
- **Market Timing:** Understand seasonal or geographic patterns

**Real-World Application:** If properties in San Francisco sell in 30 days on average while Antioch takes 50 days, you can set different expectations with clients and plan your business operations accordingly. Fast markets might need more agents; slow markets might need better pricing strategies.

---

## Problem 7: How do property taxes correlate with sale prices across different cities?

### Business Question
"I need to understand the property tax burden in different markets. Are buyers in high-tax areas getting better value, or are they paying a premium?"

### Solution
```python
# Calculate tax as percentage of sale price
df['tax_percentage'] = (df['property_tax'] / df['sale_price'] * 100).round(3)

# Analyze by city
tax_analysis = df.groupby('city').agg({
    'property_tax': 'mean',
    'sale_price': 'mean',
    'tax_percentage': 'mean',
    'property_id': 'count'
}).round(2)

tax_analysis.columns = ['Avg Property Tax', 'Avg Sale Price', 'Tax as % of Price', 'Count']
tax_analysis = tax_analysis.sort_values('Tax as % of Price', ascending=False)

print("Property Tax Analysis by City:")
print(tax_analysis)

# Overall correlation
correlation = df['property_tax'].corr(df['sale_price'])
print(f"\nCorrelation between property tax and sale price: {correlation:.3f}")
```

### Why This Matters
**Business Impact:**
- **Total Cost of Ownership:** Help buyers understand true costs beyond purchase price
- **Comparative Analysis:** Show buyers value across different cities
- **Investment Decisions:** High taxes might indicate better services/schools
- **Negotiation Points:** Use tax burden in price negotiations

**Real-World Application:** A buyer comparing a $1.5M home in Palo Alto with $34,200/year taxes vs a $1.5M home in Oakland with $18,000/year taxes needs to understand that over 10 years, the Palo Alto home costs an additional $162,000 in taxes—essentially making it a $1.66M purchase.

---

## Problem 8: What is the ROI on recent renovations?

### Business Question
"I need to know if recently renovated properties are commanding higher prices. Should we advise sellers to renovate before listing?"

### Solution
```python
# Calculate years since renovation
df['years_since_renovation'] = 2024 - df['last_renovation_year']

# Create renovation categories
df['renovation_category'] = pd.cut(df['years_since_renovation'],
                                    bins=[-1, 3, 6, 10, 50],
                                    labels=['Recent (0-3 yrs)', 'Moderate (4-6 yrs)',
                                           'Older (7-10 yrs)', 'Very Old (10+ yrs)'])

# Analyze by renovation age
renovation_analysis = df.groupby('renovation_category').agg({
    'sale_price': 'mean',
    'discount_pct': 'mean',
    'days_on_market': 'mean',
    'property_id': 'count'
}).round(2)

renovation_analysis.columns = ['Avg Sale Price', 'Avg Discount %', 'Avg Days on Market', 'Count']

print("Impact of Renovation Timing:")
print(renovation_analysis)

# Price premium for recent renovations
recent_reno = df[df['years_since_renovation'] <= 3]['sale_price'].mean()
old_reno = df[df['years_since_renovation'] > 6]['sale_price'].mean()
premium = recent_reno - old_reno

print(f"\nPrice Premium for Recent Renovations: ${premium:,.2f}")
print(f"Percentage Premium: {(premium/old_reno*100):.2f}%")
```

### Why This Matters
**Business Impact:**
- **Seller Guidance:** Advise whether renovation investment is worthwhile
- **Pricing Strategy:** Justify higher prices for renovated properties
- **Market Positioning:** Differentiate renovated vs non-renovated listings
- **ROI Calculation:** Help sellers make data-driven renovation decisions

**Real-World Application:** If recently renovated homes sell for $200,000 more on average and typical renovations cost $75,000, you can confidently advise sellers that renovation offers a strong ROI. Plus, renovated homes might sell faster, reducing carrying costs.

---

## Problem 9: Which agents are most efficient (fastest sales)?

### Business Question
"I need to identify our most efficient agents—those who close deals quickly. Fast closings mean happier clients and more transactions per year."

### Solution
```python
# Analyze agent efficiency
agent_efficiency = df.groupby(['agent_id', 'agent_name']).agg({
    'days_on_market': ['mean', 'median'],
    'sale_price': 'mean',
    'property_id': 'count',
    'commission_earned': 'sum'
}).round(2)

agent_efficiency.columns = ['Avg Days on Market', 'Median Days on Market', 
                           'Avg Sale Price', 'Properties Sold', 'Total Commission']

# Calculate efficiency score (properties sold / avg days on market)
agent_efficiency['Efficiency Score'] = (
    agent_efficiency['Properties Sold'] / agent_efficiency['Avg Days on Market'] * 100
).round(2)

agent_efficiency = agent_efficiency.sort_values('Efficiency Score', ascending=False)

print("Agent Efficiency Rankings:")
print(agent_efficiency)
```

### Why This Matters
**Business Impact:**
- **Best Practices Sharing:** Learn from efficient agents and train others
- **Client Satisfaction:** Faster sales mean happier sellers
- **Revenue Velocity:** More transactions per agent means more revenue
- **Agent Capacity:** Efficient agents can handle more listings

**Real-World Application:** If Agent A sells properties in 25 days on average while Agent B takes 55 days, Agent A can handle twice as many listings per year. If both agents sell 10 properties, Agent A generates revenue in 250 days while Agent B needs 550 days—Agent A could potentially sell 20+ properties in the same timeframe.

---

## Problem 10: What is the optimal pricing strategy by property size?

### Business Question
"I need to understand the price per square foot across different property sizes. Are larger properties more or less expensive per square foot? This helps us price new listings competitively."

### Solution
```python
# Calculate price per square foot
df['price_per_sqft'] = (df['sale_price'] / df['square_feet']).round(2)

# Create size categories
df['size_category'] = pd.cut(df['square_feet'],
                              bins=[0, 1200, 1800, 2500, 5000],
                              labels=['Small (<1200)', 'Medium (1200-1800)',
                                     'Large (1800-2500)', 'Very Large (2500+)'])

# Analyze by size category
size_analysis = df.groupby('size_category').agg({
    'price_per_sqft': 'mean',
    'sale_price': 'mean',
    'square_feet': 'mean',
    'days_on_market': 'mean',
    'property_id': 'count'
}).round(2)

size_analysis.columns = ['Avg Price/SqFt', 'Avg Sale Price', 'Avg Square Feet', 
                         'Avg Days on Market', 'Count']

print("Pricing Analysis by Property Size:")
print(size_analysis)

# Additional: Price per sqft by property type and size
detailed_analysis = df.groupby(['property_type', 'size_category'])['price_per_sqft'].mean().round(2)
print("\nPrice per SqFt by Type and Size:")
print(detailed_analysis.unstack())
```

### Why This Matters
**Business Impact:**
- **Competitive Pricing:** Price new listings based on market data
- **Value Communication:** Show buyers whether they're getting good value
- **Market Segmentation:** Understand different buyer segments (small vs large)
- **Listing Strategy:** Know which size properties are easiest to sell

**Real-World Application:** If small condos sell for $750/sqft while large single-family homes sell for $650/sqft, you can explain to buyers that smaller properties command a premium per square foot due to affordability and location. This helps set realistic expectations and justify pricing.

---

## Summary: Why These Questions Matter

### Strategic Decision Making
Each of these 10 questions addresses a specific business need:
1. **Revenue Management** (Problems 1, 4, 9) - Optimize income and resource allocation
2. **Pricing Strategy** (Problems 2, 3, 10) - Set competitive, profitable prices
3. **Market Intelligence** (Problems 5, 6, 7) - Understand market dynamics
4. **Client Advisory** (Problems 5, 8) - Provide data-driven recommendations

### Skills You're Developing

By solving these problems, you're learning to:

- **Data Aggregation:** Group and summarize data meaningfully
- **Feature Engineering:** Create new calculated fields (commission_earned, discount_pct, price_per_sqft)
- **Statistical Analysis:** Calculate correlations, averages, and distributions
- **Business Translation:** Convert data insights into actionable business decisions
- **Pandas Proficiency:** Master groupby, agg, sorting, and filtering operations
- **Critical Thinking:** Understand not just "how" to analyze, but "why" it matters

### Real-World Impact

In a real estate business, these analyses directly impact:
- **Profitability:** Better pricing and agent management increase margins
- **Client Satisfaction:** Data-driven advice builds trust and delivers results
- **Competitive Advantage:** Market intelligence helps you outperform competitors
- **Operational Efficiency:** Understanding patterns optimizes resource allocation

### Next Steps

After mastering these problems, you should be able to:
1. Identify business questions from raw data
2. Design appropriate analyses to answer those questions
3. Communicate findings to non-technical stakeholders
4. Make data-driven recommendations with confidence

Remember: **Data analysis is not just about writing code—it's about solving real business problems and creating value.**
