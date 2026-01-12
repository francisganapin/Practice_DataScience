# 🏠 Real Estate Data Analytics - Complete Solutions Guide

**Dataset:** `real_estate_data.csv` (30 properties)

---

## 📦 Initial Setup

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('real_estate_data.csv')
```

---

# 📊 BEGINNER LEVEL (Problems 1-5)

---

## Problem 1: Basic Exploration

### Task
Load the dataset and answer:
- How many properties are in the dataset?
- What are the column names and their data types?
- Are there any missing values?

### Solution

```python
# Number of properties
print(f"Total Properties: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}")

# Column names and data types
print("\n=== Column Info ===")
print(df.dtypes)

# Alternative: More detailed info
print("\n=== Detailed Info ===")
df.info()

# Missing values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# Quick statistics
print("\n=== Summary Statistics ===")
print(df.describe())
```

### Expected Output
```
Total Properties: 30
Total Columns: 26
Missing Values: 0 (no missing data in this dataset)
```

---

## Problem 2: Property Type Distribution

### Task
Find the count and percentage of each property type.

### Solution

```python
# Count of each property type
type_counts = df['property_type'].value_counts()
print("=== Property Type Counts ===")
print(type_counts)

# Percentage
type_pct = df['property_type'].value_counts(normalize=True) * 100
print("\n=== Property Type Percentage ===")
print(type_pct.round(2))

# Combined view
type_summary = pd.DataFrame({
    'Count': type_counts,
    'Percentage': type_pct.round(2)
})
print("\n=== Summary ===")
print(type_summary)

# Visualization
plt.figure(figsize=(8, 6))
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Property Type Distribution')
plt.show()
```

### Expected Output
```
Property Type      Count    Percentage
Single Family      14       46.67%
Condo              10       33.33%
Townhouse          6        20.00%
```

---

## Problem 3: Average Prices by City

### Task
Calculate the average listing price and average sold price for each city.

### Solution

```python
# Group by city and calculate means
city_prices = df.groupby('city')[['listing_price', 'sold_price']].mean()
city_prices = city_prices.sort_values('sold_price', ascending=False)

print("=== Average Prices by City ===")
print(city_prices.round(2))

# Highest average sold price
highest_city = city_prices['sold_price'].idxmax()
highest_price = city_prices['sold_price'].max()
print(f"\n🏆 Highest Avg Sold Price: {highest_city} (${highest_price:,.2f})")

# Visualization
city_prices.plot(kind='bar', figsize=(12, 6))
plt.title('Average Listing vs Sold Price by City')
plt.ylabel('Price ($)')
plt.xlabel('City')
plt.xticks(rotation=45)
plt.legend(['Listing Price', 'Sold Price'])
plt.tight_layout()
plt.show()
```

---

## Problem 4: Price Per Square Foot

### Task
Create a `price_per_sqft` column and find the top 5 properties.

### Solution

```python
# Create price per sqft column
df['price_per_sqft'] = df['sold_price'] / df['sqft']

# Top 5 highest price per sqft
top5 = df.nlargest(5, 'price_per_sqft')[['property_id', 'address', 'city', 
                                           'sqft', 'sold_price', 'price_per_sqft']]
print("=== Top 5 Highest Price Per Sqft ===")
print(top5.round(2))

# Statistics
print(f"\nAverage Price/Sqft: ${df['price_per_sqft'].mean():.2f}")
print(f"Median Price/Sqft: ${df['price_per_sqft'].median():.2f}")
print(f"Min Price/Sqft: ${df['price_per_sqft'].min():.2f}")
print(f"Max Price/Sqft: ${df['price_per_sqft'].max():.2f}")
```

---

## Problem 5: Pool Properties Analysis

### Task
Compare properties with pools vs without pools.

### Solution

```python
# Count of properties with/without pool
pool_counts = df['has_pool'].value_counts()
print("=== Pool Distribution ===")
print(f"With Pool: {pool_counts.get(1, 0)}")
print(f"Without Pool: {pool_counts.get(0, 0)}")

# Average sold price comparison
pool_prices = df.groupby('has_pool')['sold_price'].mean()
print("\n=== Average Sold Price ===")
print(f"With Pool: ${pool_prices[1]:,.2f}")
print(f"Without Pool: ${pool_prices[0]:,.2f}")

# Price difference
price_diff = pool_prices[1] - pool_prices[0]
pct_diff = (price_diff / pool_prices[0]) * 100
print(f"\n💰 Price Difference: ${price_diff:,.2f}")
print(f"📈 Percentage Difference: {pct_diff:.2f}%")

# More detailed comparison
pool_analysis = df.groupby('has_pool').agg({
    'sold_price': ['mean', 'median', 'count'],
    'sqft': 'mean',
    'price_per_sqft': 'mean'
})
print("\n=== Detailed Pool Analysis ===")
print(pool_analysis.round(2))
```

---

# 📈 INTERMEDIATE LEVEL (Problems 6-10)

---

## Problem 6: Agent Performance Analysis

### Task
For each agent, calculate total sales, volume, and average days on market.

### Solution

```python
# Agent performance metrics
agent_performance = df.groupby(['agent_id', 'agent_name']).agg({
    'property_id': 'count',
    'sold_price': 'sum',
    'days_on_market': 'mean'
}).rename(columns={
    'property_id': 'properties_sold',
    'sold_price': 'total_volume',
    'days_on_market': 'avg_days_on_market'
})

# Sort by total volume
agent_performance = agent_performance.sort_values('total_volume', ascending=False)

print("=== Agent Performance Ranking ===")
print(agent_performance.round(2))

# Top performer
top_agent = agent_performance.index[0][1]
top_volume = agent_performance['total_volume'].iloc[0]
print(f"\n🏆 Top Agent: {top_agent}")
print(f"   Total Volume: ${top_volume:,.2f}")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Total volume chart
agent_performance['total_volume'].head(10).plot(kind='barh', ax=axes[0])
axes[0].set_title('Top Agents by Sales Volume')
axes[0].set_xlabel('Total Volume ($)')

# Average days on market
agent_performance['avg_days_on_market'].head(10).plot(kind='barh', ax=axes[1])
axes[1].set_title('Average Days on Market by Agent')
axes[1].set_xlabel('Days')

plt.tight_layout()
plt.show()
```

---

## Problem 7: Price Negotiation Analysis

### Task
Analyze the difference between listing and sold prices.

### Solution

```python
# Create price difference columns
df['price_difference'] = df['listing_price'] - df['sold_price']
df['price_diff_pct'] = (df['price_difference'] / df['listing_price']) * 100

# Statistics
print("=== Price Negotiation Statistics ===")
print(f"Average Discount: ${df['price_difference'].mean():,.2f}")
print(f"Average Discount %: {df['price_diff_pct'].mean():.2f}%")

# By property type
negotiation_by_type = df.groupby('property_type').agg({
    'price_difference': 'mean',
    'price_diff_pct': 'mean'
}).round(2)

print("\n=== Negotiation by Property Type ===")
print(negotiation_by_type)

# Highest negotiation
most_negotiated = negotiation_by_type['price_diff_pct'].idxmax()
print(f"\n🏷️ Most Negotiated Type: {most_negotiated}")

# Properties sold ABOVE listing price
above_listing = df[df['sold_price'] > df['listing_price']]
print(f"\n=== Properties Sold Above Listing ===")
print(f"Count: {len(above_listing)}")
if len(above_listing) > 0:
    print(above_listing[['property_id', 'address', 'city', 'listing_price', 
                         'sold_price', 'price_difference']])

# Visualization
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='property_type', y='price_diff_pct')
plt.title('Price Negotiation % by Property Type')
plt.ylabel('Discount %')
plt.xlabel('Property Type')
plt.axhline(y=0, color='r', linestyle='--', alpha=0.5)
plt.show()
```

---

## Problem 8: Market Speed by State

### Task
Analyze how quickly properties sell in different states.

### Solution

```python
# Days on market by state
state_speed = df.groupby('state')['days_on_market'].agg(['mean', 'median', 'min', 'max', 'count'])
state_speed = state_speed.sort_values('mean')

print("=== Days on Market by State ===")
print(state_speed.round(2))

# Fastest and slowest markets
fastest = state_speed['mean'].idxmin()
slowest = state_speed['mean'].idxmax()
print(f"\n🏃 Fastest Market: {fastest} ({state_speed.loc[fastest, 'mean']:.1f} days avg)")
print(f"🐢 Slowest Market: {slowest} ({state_speed.loc[slowest, 'mean']:.1f} days avg)")

# Visualization
plt.figure(figsize=(12, 6))
state_speed[['mean', 'median']].plot(kind='bar')
plt.title('Average Days on Market by State')
plt.ylabel('Days')
plt.xlabel('State')
plt.legend(['Mean', 'Median'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

## Problem 9: Correlation Analysis

### Task
Calculate correlations and create a heatmap.

### Solution

```python
# Select numeric columns for correlation
numeric_cols = ['sqft', 'bedrooms', 'bathrooms', 'year_built', 
                'school_rating', 'walkability_score', 'sold_price', 
                'days_on_market', 'crime_rate']

# Correlation matrix
corr_matrix = df[numeric_cols].corr()

print("=== Correlation with Sold Price ===")
price_corr = corr_matrix['sold_price'].sort_values(ascending=False)
print(price_corr.round(3))

# Strongest correlation
strongest = price_corr.drop('sold_price').abs().idxmax()
strongest_val = price_corr[strongest]
print(f"\n🔗 Strongest Correlation: {strongest} ({strongest_val:.3f})")

# Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
            fmt='.2f', square=True, linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.tight_layout()
plt.show()

# Scatter plot of strongest correlation
plt.figure(figsize=(10, 6))
plt.scatter(df[strongest], df['sold_price'], alpha=0.6)
plt.xlabel(strongest)
plt.ylabel('Sold Price')
plt.title(f'Sold Price vs {strongest}')
plt.tight_layout()
plt.show()
```

---

## Problem 10: Time-Based Analysis

### Task
Analyze listings by month and identify seasonal patterns.

### Solution

```python
# Convert to datetime
df['listing_date'] = pd.to_datetime(df['listing_date'])
df['sold_date'] = pd.to_datetime(df['sold_date'])

# Extract month
df['listing_month'] = df['listing_date'].dt.month
df['listing_month_name'] = df['listing_date'].dt.month_name()

# Listings by month
monthly_listings = df.groupby('listing_month').agg({
    'property_id': 'count',
    'sold_price': 'mean',
    'days_on_market': 'mean'
}).rename(columns={'property_id': 'count'})

print("=== Monthly Analysis ===")
print(monthly_listings.round(2))

# Most active month
busiest_month = monthly_listings['count'].idxmax()
print(f"\n📅 Busiest Listing Month: {busiest_month}")

# Average sale price by month
print("\n=== Seasonal Price Pattern ===")
for month in sorted(df['listing_month'].unique()):
    avg_price = df[df['listing_month'] == month]['sold_price'].mean()
    count = len(df[df['listing_month'] == month])
    print(f"Month {month}: ${avg_price:,.2f} (n={count})")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

monthly_listings['count'].plot(kind='bar', ax=axes[0], color='steelblue')
axes[0].set_title('Number of Listings by Month')
axes[0].set_xlabel('Month')
axes[0].set_ylabel('Count')

monthly_listings['sold_price'].plot(kind='line', marker='o', ax=axes[1], color='green')
axes[1].set_title('Average Sold Price by Listing Month')
axes[1].set_xlabel('Month')
axes[1].set_ylabel('Average Price ($)')

plt.tight_layout()
plt.show()
```

---

# 🚀 ADVANCED LEVEL (Problems 11-15)

---

## Problem 11: Market Segmentation

### Task
Create price segments and analyze each segment's characteristics.

### Solution

```python
# Create price segments
bins = [0, 400000, 600000, 800000, float('inf')]
labels = ['Budget', 'Mid-Range', 'Premium', 'Luxury']

df['price_segment'] = pd.cut(df['sold_price'], bins=bins, labels=labels)

# Segment analysis
segment_analysis = df.groupby('price_segment').agg({
    'property_id': 'count',
    'sqft': 'mean',
    'days_on_market': 'mean',
    'sold_price': 'mean',
    'bedrooms': 'mean',
    'bathrooms': 'mean'
}).rename(columns={'property_id': 'count'})

print("=== Market Segment Analysis ===")
print(segment_analysis.round(2))

# Most common property type per segment
print("\n=== Most Common Property Type by Segment ===")
for segment in labels:
    segment_data = df[df['price_segment'] == segment]
    if len(segment_data) > 0:
        most_common = segment_data['property_type'].mode()[0]
        count = len(segment_data)
        print(f"{segment}: {most_common} (n={count})")

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Count by segment
segment_analysis['count'].plot(kind='bar', ax=axes[0,0], color='steelblue')
axes[0,0].set_title('Properties by Segment')
axes[0,0].set_ylabel('Count')

# Avg sqft by segment
segment_analysis['sqft'].plot(kind='bar', ax=axes[0,1], color='green')
axes[0,1].set_title('Average Sqft by Segment')
axes[0,1].set_ylabel('Sqft')

# Days on market by segment
segment_analysis['days_on_market'].plot(kind='bar', ax=axes[1,0], color='orange')
axes[1,0].set_title('Avg Days on Market by Segment')
axes[1,0].set_ylabel('Days')

# Price distribution
df.boxplot(column='sold_price', by='price_segment', ax=axes[1,1])
axes[1,1].set_title('Price Distribution by Segment')
axes[1,1].set_ylabel('Price ($)')

plt.tight_layout()
plt.show()
```

---

## Problem 12: ROI & Investment Analysis

### Task
Calculate estimated original price, appreciation, and ROI by neighborhood.

### Solution

```python
# Current year
current_year = 2024
appreciation_rate = 1.03  # 3% annual

# Calculate years since built
df['years_since_built'] = current_year - df['year_built']

# Estimated original purchase price
# Formula: original = sold_price / (1.03 ^ years)
df['estimated_original_price'] = df['sold_price'] / (appreciation_rate ** df['years_since_built'])

# Total appreciation
df['total_appreciation'] = df['sold_price'] - df['estimated_original_price']

# ROI percentage
df['roi_pct'] = (df['total_appreciation'] / df['estimated_original_price']) * 100

# View property-level results
print("=== Property ROI Analysis (Sample) ===")
print(df[['property_id', 'neighborhood', 'year_built', 'sold_price', 
          'estimated_original_price', 'total_appreciation', 'roi_pct']].head(10).round(2))

# Neighborhood analysis
neighborhood_roi = df.groupby('neighborhood').agg({
    'roi_pct': 'mean',
    'total_appreciation': 'mean',
    'sold_price': 'mean',
    'property_id': 'count'
}).rename(columns={'property_id': 'count'})

neighborhood_roi = neighborhood_roi.sort_values('roi_pct', ascending=False)

print("\n=== Neighborhood ROI Ranking ===")
print(neighborhood_roi.round(2))

# Best neighborhood
best_neighborhood = neighborhood_roi['roi_pct'].idxmax()
best_roi = neighborhood_roi['roi_pct'].max()
print(f"\n🏆 Best Neighborhood for ROI: {best_neighborhood}")
print(f"   Average ROI: {best_roi:.2f}%")

# Visualization
plt.figure(figsize=(12, 8))
neighborhood_roi['roi_pct'].plot(kind='barh')
plt.xlabel('Average ROI (%)')
plt.ylabel('Neighborhood')
plt.title('Average ROI by Neighborhood')
plt.tight_layout()
plt.show()
```

---

## Problem 13: Predictive Feature Importance

### Task
Build a linear regression model to predict sold price.

### Solution

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# Define features and target
features = ['sqft', 'bedrooms', 'bathrooms', 'year_built', 'school_rating', 'walkability_score']
X = df[features]
y = df['sold_price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model performance
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"\n=== Model Performance ===")
print(f"R² Score: {r2:.4f}")
print(f"RMSE: ${rmse:,.2f}")

# Feature coefficients
print(f"\n=== Feature Coefficients ===")
print(f"Intercept: ${model.intercept_:,.2f}\n")

coef_df = pd.DataFrame({
    'Feature': features,
    'Coefficient': model.coef_,
    'Abs_Coefficient': np.abs(model.coef_)
}).sort_values('Abs_Coefficient', ascending=False)

print(coef_df[['Feature', 'Coefficient']].to_string(index=False))

# Most important feature
print(f"\n🏆 Most Important Feature: {coef_df.iloc[0]['Feature']}")

# Predict new property
new_property = pd.DataFrame({
    'sqft': [2000],
    'bedrooms': [3],
    'bathrooms': [2],
    'year_built': [2010],
    'school_rating': [8],
    'walkability_score': [75]
})

predicted_price = model.predict(new_property)[0]

print(f"\n=== Price Prediction ===")
print(f"Property: 2000 sqft, 3 bed, 2 bath, built 2010, school 8, walkability 75")
print(f"💰 Predicted Price: ${predicted_price:,.2f}")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Actual vs Predicted
axes[0].scatter(y_test, y_pred, alpha=0.7)
axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
axes[0].set_xlabel('Actual Price')
axes[0].set_ylabel('Predicted Price')
axes[0].set_title(f'Actual vs Predicted (R² = {r2:.3f})')

# Feature importance
axes[1].barh(coef_df['Feature'], coef_df['Coefficient'])
axes[1].set_xlabel('Coefficient')
axes[1].set_title('Feature Importance')

plt.tight_layout()
plt.show()
```

---

## Problem 14: Anomaly Detection

### Task
Identify outliers using Z-scores and IQR methods.

### Solution

```python
from scipy import stats

# Ensure price_per_sqft exists
if 'price_per_sqft' not in df.columns:
    df['price_per_sqft'] = df['sold_price'] / df['sqft']

# === Method 1: Z-Score for Price per Sqft ===
mean_ppsf = df['price_per_sqft'].mean()
std_ppsf = df['price_per_sqft'].std()

df['ppsf_zscore'] = (df['price_per_sqft'] - mean_ppsf) / std_ppsf
outliers_zscore = df[np.abs(df['ppsf_zscore']) > 2]

print("=== Z-Score Outliers (Price/Sqft > 2 std) ===")
print(f"Count: {len(outliers_zscore)}")
if len(outliers_zscore) > 0:
    print(outliers_zscore[['property_id', 'address', 'city', 'price_per_sqft', 'ppsf_zscore']])

# === Method 2: IQR for Days on Market ===
Q1 = df['days_on_market'].quantile(0.25)
Q3 = df['days_on_market'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR

outliers_dom = df[df['days_on_market'] > upper_bound]

print(f"\n=== IQR Outliers (Days on Market > {upper_bound:.0f}) ===")
print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"Upper Bound: {upper_bound:.0f}")
print(f"Count: {len(outliers_dom)}")
if len(outliers_dom) > 0:
    print(outliers_dom[['property_id', 'address', 'city', 'days_on_market']])

# === Method 3: Sold Above Listing (>5%) ===
df['above_listing_pct'] = ((df['sold_price'] - df['listing_price']) / df['listing_price']) * 100
outliers_above = df[df['above_listing_pct'] > 5]

print(f"\n=== Properties Sold >5% Above Listing ===")
print(f"Count: {len(outliers_above)}")
if len(outliers_above) > 0:
    print(outliers_above[['property_id', 'address', 'city', 'listing_price', 
                          'sold_price', 'above_listing_pct']])

# Summary
print("\n=== Anomaly Summary ===")
print(f"Price/Sqft Outliers (Z-score): {len(outliers_zscore)}")
print(f"Days on Market Outliers (IQR): {len(outliers_dom)}")
print(f"Above Listing >5%: {len(outliers_above)}")

# Visualization
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Price per sqft boxplot
axes[0].boxplot(df['price_per_sqft'])
axes[0].set_title('Price per Sqft Distribution')
axes[0].set_ylabel('$/Sqft')

# Days on market boxplot  
axes[1].boxplot(df['days_on_market'])
axes[1].set_title('Days on Market Distribution')
axes[1].set_ylabel('Days')

# Above/below listing histogram
axes[2].hist(df['above_listing_pct'], bins=15, edgecolor='black')
axes[2].axvline(x=0, color='r', linestyle='--')
axes[2].axvline(x=5, color='g', linestyle='--')
axes[2].set_title('Sold Price vs Listing %')
axes[2].set_xlabel('% Difference')

plt.tight_layout()
plt.show()
```

---

## Problem 15: Comprehensive Market Report

### Task
Create a complete market analysis with multiple visualizations.

### Solution

```python
# ==========================================
# COMPREHENSIVE REAL ESTATE MARKET REPORT
# ==========================================

print("=" * 60)
print("       REAL ESTATE MARKET ANALYSIS REPORT")
print("=" * 60)

# === 1. EXECUTIVE SUMMARY ===
print("\n📊 EXECUTIVE SUMMARY")
print("-" * 40)
total_properties = len(df)
total_volume = df['sold_price'].sum()
avg_price = df['sold_price'].mean()
median_price = df['sold_price'].median()
avg_dom = df['days_on_market'].mean()

print(f"Total Properties Analyzed: {total_properties}")
print(f"Total Sales Volume: ${total_volume:,.2f}")
print(f"Average Sold Price: ${avg_price:,.2f}")
print(f"Median Sold Price: ${median_price:,.2f}")
print(f"Average Days on Market: {avg_dom:.1f}")

# === 2. GEOGRAPHIC ANALYSIS ===
print("\n🌎 GEOGRAPHIC ANALYSIS")
print("-" * 40)

# Best performing cities
city_perf = df.groupby('city').agg({
    'sold_price': 'mean',
    'days_on_market': 'mean',
    'property_id': 'count'
}).rename(columns={'property_id': 'count'})

best_city = city_perf['sold_price'].idxmax()
worst_city = city_perf['sold_price'].idxmin()
fastest_city = city_perf['days_on_market'].idxmin()

print(f"Highest Avg Price: {best_city} (${city_perf.loc[best_city, 'sold_price']:,.2f})")
print(f"Lowest Avg Price: {worst_city} (${city_perf.loc[worst_city, 'sold_price']:,.2f})")
print(f"Fastest Sales: {fastest_city} ({city_perf.loc[fastest_city, 'days_on_market']:.1f} days)")

# Best performing states
state_perf = df.groupby('state').agg({
    'sold_price': ['sum', 'mean'],
    'days_on_market': 'mean'
})
print(f"\nStates by Total Volume:")
print(state_perf['sold_price']['sum'].sort_values(ascending=False))

# === 3. AGENT LEADERBOARD ===
print("\n👔 AGENT LEADERBOARD")
print("-" * 40)

agent_stats = df.groupby('agent_name').agg({
    'sold_price': 'sum',
    'days_on_market': 'mean',
    'property_id': 'count'
}).rename(columns={'property_id': 'sales_count', 'sold_price': 'total_volume'})

# Top 3 by volume
top3_volume = agent_stats.nlargest(3, 'total_volume')
print("Top 3 by Sales Volume:")
for i, (agent, row) in enumerate(top3_volume.iterrows(), 1):
    print(f"  {i}. {agent}: ${row['total_volume']:,.2f} ({row['sales_count']} sales)")

# Top 3 by efficiency (lowest days on market)
top3_speed = agent_stats.nsmallest(3, 'days_on_market')
print("\nTop 3 by Speed (Lowest Days on Market):")
for i, (agent, row) in enumerate(top3_speed.iterrows(), 1):
    print(f"  {i}. {agent}: {row['days_on_market']:.1f} days avg")

# === 4. PROPERTY TYPE INSIGHTS ===
print("\n🏠 PROPERTY TYPE INSIGHTS")
print("-" * 40)

type_analysis = df.groupby('property_type').agg({
    'sold_price': ['mean', 'median'],
    'sqft': 'mean',
    'days_on_market': 'mean',
    'property_id': 'count'
})
print(type_analysis.round(2))

# === 5. RECOMMENDATIONS ===
print("\n💡 INVESTMENT RECOMMENDATIONS")
print("-" * 40)

# Best value neighborhoods (low price per sqft, good school rating)
if 'price_per_sqft' not in df.columns:
    df['price_per_sqft'] = df['sold_price'] / df['sqft']

value_analysis = df.groupby('neighborhood').agg({
    'price_per_sqft': 'mean',
    'school_rating': 'mean',
    'days_on_market': 'mean'
})

# Score (high school rating, low price per sqft, low DOM)
value_analysis['value_score'] = (
    value_analysis['school_rating'] / value_analysis['school_rating'].max() * 0.4 +
    (1 - value_analysis['price_per_sqft'] / value_analysis['price_per_sqft'].max()) * 0.4 +
    (1 - value_analysis['days_on_market'] / value_analysis['days_on_market'].max()) * 0.2
)

best_value = value_analysis.nlargest(3, 'value_score')
print("Top 3 Best Value Neighborhoods:")
for i, (hood, row) in enumerate(best_value.iterrows(), 1):
    print(f"  {i}. {hood} (Score: {row['value_score']:.2f})")
    print(f"     - Avg $/Sqft: ${row['price_per_sqft']:.2f}")
    print(f"     - School Rating: {row['school_rating']:.1f}")

# === 6. VISUALIZATIONS ===
print("\n📈 GENERATING VISUALIZATIONS...")

fig = plt.figure(figsize=(16, 12))

# 1. Price Distribution
ax1 = fig.add_subplot(2, 3, 1)
ax1.hist(df['sold_price'], bins=15, edgecolor='black', color='steelblue')
ax1.axvline(avg_price, color='red', linestyle='--', label=f'Mean: ${avg_price/1000:.0f}K')
ax1.axvline(median_price, color='green', linestyle='--', label=f'Median: ${median_price/1000:.0f}K')
ax1.set_title('Price Distribution')
ax1.set_xlabel('Sold Price ($)')
ax1.set_ylabel('Count')
ax1.legend()

# 2. Price by Property Type (Boxplot)
ax2 = fig.add_subplot(2, 3, 2)
df.boxplot(column='sold_price', by='property_type', ax=ax2)
ax2.set_title('Price by Property Type')
ax2.set_xlabel('Property Type')
ax2.set_ylabel('Sold Price ($)')
plt.suptitle('')  # Remove automatic title

# 3. Sqft vs Price (Scatter)
ax3 = fig.add_subplot(2, 3, 3)
scatter = ax3.scatter(df['sqft'], df['sold_price'], 
                       c=df['property_type'].astype('category').cat.codes, 
                       alpha=0.7, cmap='viridis')
ax3.set_title('Sqft vs Sold Price')
ax3.set_xlabel('Square Feet')
ax3.set_ylabel('Sold Price ($)')

# 4. Average Price by City
ax4 = fig.add_subplot(2, 3, 4)
city_perf['sold_price'].sort_values().plot(kind='barh', ax=ax4, color='teal')
ax4.set_title('Average Price by City')
ax4.set_xlabel('Average Sold Price ($)')

# 5. Days on Market Distribution
ax5 = fig.add_subplot(2, 3, 5)
ax5.hist(df['days_on_market'], bins=12, edgecolor='black', color='coral')
ax5.axvline(avg_dom, color='red', linestyle='--', label=f'Avg: {avg_dom:.0f} days')
ax5.set_title('Days on Market Distribution')
ax5.set_xlabel('Days')
ax5.set_ylabel('Count')
ax5.legend()

# 6. Top Agents by Volume
ax6 = fig.add_subplot(2, 3, 6)
agent_stats.nlargest(5, 'total_volume')['total_volume'].plot(kind='bar', ax=ax6, color='purple')
ax6.set_title('Top 5 Agents by Volume')
ax6.set_ylabel('Total Sales Volume ($)')
ax6.set_xticklabels(ax6.get_xticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.savefig('market_report_charts.png', dpi=150, bbox_inches='tight')
plt.show()

print("\n✅ Report Complete!")
print("📊 Charts saved to: market_report_charts.png")
```

---

# 🎯 Quick Reference Table

| Problem | Key Skills | Difficulty |
|---------|-----------|------------|
| 1 | `shape`, `info()`, `isnull()` | ⭐ |
| 2 | `value_counts()`, percentages | ⭐ |
| 3 | `groupby()`, `mean()` | ⭐ |
| 4 | Creating columns, `nlargest()` | ⭐ |
| 5 | Boolean filtering, comparison | ⭐ |
| 6 | `groupby()` + `agg()` | ⭐⭐ |
| 7 | Feature engineering, filtering | ⭐⭐ |
| 8 | `median()`, bar charts | ⭐⭐ |
| 9 | `corr()`, heatmap | ⭐⭐ |
| 10 | `pd.to_datetime()`, `dt.month` | ⭐⭐ |
| 11 | `pd.cut()`, multi-level analysis | ⭐⭐⭐ |
| 12 | Financial formulas, ROI | ⭐⭐⭐ |
| 13 | sklearn, LinearRegression | ⭐⭐⭐ |
| 14 | Z-scores, IQR, outliers | ⭐⭐⭐ |
| 15 | Full report, multiple viz | ⭐⭐⭐ |

---

**Happy Learning! 🚀**
