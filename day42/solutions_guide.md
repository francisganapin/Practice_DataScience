# fReal Estate Data Analysis - Solutions Guide

This guide provides detailed solutions for all 15 medium-level problems in the real estate dataset analysis.

## Why Practice These Problems?

These 15 problems are designed to build **real-world data analysis skills** that are essential for:

1. **Business Intelligence**: Understanding how to extract meaningful insights from data
2. **Decision Making**: Learning to analyze trends and patterns that drive business decisions
3. **Data Manipulation**: Mastering pandas operations that you'll use daily as a data analyst
4. **Statistical Thinking**: Developing intuition about data relationships and correlations
5. **Visualization**: Creating compelling visual stories from raw data

Each problem simulates actual tasks you'd encounter working with real estate data, customer analytics, sales reporting, or any business domain. The skills are **transferable** - once you master grouping, filtering, and aggregating real estate data, you can apply the same techniques to e-commerce, finance, healthcare, or any other field.

**Key Learning Outcomes:**

- Data aggregation and grouping
- Statistical analysis and correlation
- Feature engineering and derived metrics
- Time series analysis
- Outlier detection
- Multi-criteria filtering
- Data visualization
- Predictive modeling basics

---

## Problem 1: Price Analysis by Property Type

### Why This Matters

Understanding pricing patterns across different property types is crucial for:

- **Market Segmentation**: Identifying which property types are most valuable
- **Investment Strategy**: Knowing where to allocate resources
- **Pricing Strategy**: Understanding typical discount rates for negotiations
- **Portfolio Analysis**: Comparing performance across property categories

This is one of the most common business questions: "How do different segments perform?"

### Approach

1. Group data by property type
2. Calculate average listing price, sale price, and discount percentage
3. Sort by average sale price

### Solution

```python
# Calculate discount percentage
df['discount_pct'] = ((df['listing_price'] - df['sale_price']) / df['listing_price'] * 100)

# Group by property type and calculate averages
price_analysis = df.groupby('property_type').agg({
    'listing_price': 'mean',
    'sale_price': 'mean',
    'discount_pct': 'mean'
}).round(2)

# Sort by average sale price
price_analysis = price_analysis.sort_values('sale_price', ascending=False)

print(price_analysis)
```

### Key Concepts

- `groupby()` for aggregation
- `agg()` with multiple functions
- Percentage calculations
- `sort_values()` for ordering

---

## Problem 2: Top Performing Agents

### Why This Matters

Agent performance analysis is essential for:

- **Resource Allocation**: Identifying top performers to reward or learn from
- **Training Needs**: Understanding which agents need support
- **Commission Planning**: Calculating compensation accurately
- **Business Forecasting**: Predicting future revenue based on agent performance

This teaches you how to create **performance dashboards** - a critical skill in any analytics role.

### Approach

1. Calculate commission for each transaction
2. Group by agent and aggregate metrics
3. Select top 5 by total sales volume

### Solution

```python
# Calculate commission earned
df['commission_earned'] = df['sale_price'] * df['commission_rate']

# Group by agent
agent_performance = df.groupby(['agent_id', 'agent_name']).agg({
    'property_id': 'count',
    'sale_price': 'sum',
    'days_on_market': 'mean',
    'commission_earned': 'sum'
}).rename(columns={
    'property_id': 'properties_sold',
    'sale_price': 'total_sales_volume',
    'days_on_market': 'avg_days_on_market'
}).round(2)

# Sort and get top 5
top_agents = agent_performance.sort_values('total_sales_volume', ascending=False).head(5)

print(top_agents)
```

### Key Concepts

- Multiple aggregations on different columns
- `rename()` for clearer column names
- `head()` to get top N records

---

## Problem 3: Price per Square Foot Analysis

### Approach

1. Calculate price per square foot
2. Group by city and find averages
3. Create visualization for top 10 cities

### Solution

```python
# Calculate price per square foot
df['price_per_sqft'] = df['sale_price'] / df['square_feet']

# City analysis
city_price_sqft = df.groupby('city')['price_per_sqft'].mean().sort_values(ascending=False)

print(f"Highest: {city_price_sqft.index[0]} - ${city_price_sqft.iloc[0]:.2f}/sqft")
print(f"Lowest: {city_price_sqft.index[-1]} - ${city_price_sqft.iloc[-1]:.2f}/sqft")

# Visualization
top_10_cities = city_price_sqft.head(10)

plt.figure(figsize=(12, 6))
top_10_cities.plot(kind='bar', color='steelblue')
plt.title('Top 10 Cities by Average Price per Square Foot', fontsize=14, fontweight='bold')
plt.xlabel('City', fontsize=12)
plt.ylabel('Price per Sq Ft ($)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

### Key Concepts

- Derived columns for calculations
- `iloc[]` for positional indexing
- Bar chart creation with matplotlib
- Plot customization (labels, rotation, grid)

---

## Problem 4: Correlation Analysis

### Why This Matters

Correlation analysis helps you:

- **Identify Key Drivers**: Understand what factors most influence price
- **Feature Selection**: Choose the best variables for predictive models
- **Avoid Multicollinearity**: Detect redundant features
- **Generate Insights**: Discover unexpected relationships in data

This is a **fundamental statistical skill** used in every data science project to understand variable relationships.

### Approach

1. Select relevant numerical columns
2. Calculate correlation matrix
3. Create heatmap visualization

### Solution

```python
# Select features for correlation
features = ['sale_price', 'square_feet', 'bedrooms', 'bathrooms', 
            'year_built', 'school_rating', 'walkability_score']

correlation_matrix = df[features].corr()

# Find strongest correlation with sale_price
correlations_with_price = correlation_matrix['sale_price'].drop('sale_price').sort_values(ascending=False)
print("Correlations with Sale Price:")
print(correlations_with_price)
print(f"\nStrongest correlation: {correlations_with_price.index[0]} ({correlations_with_price.iloc[0]:.3f})")

# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, square=True, linewidths=1)
plt.title('Correlation Heatmap - Property Features vs Sale Price', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### Key Concepts

- `corr()` for correlation matrix
- `drop()` to exclude a column
- Seaborn heatmap with annotations
- Color mapping with diverging colormap

---

## Problem 5: Days on Market Segmentation

### Approach

1. Create categorical bins using `pd.cut()` or conditional logic
2. Group by category and calculate statistics
3. Calculate percentages

### Solution

```python
# Create market_speed category
def categorize_speed(days):
    if days <= 25:
        return 'Fast'
    elif days <= 50:
        return 'Medium'
    else:
        return 'Slow'

df['market_speed'] = df['days_on_market'].apply(categorize_speed)

# Alternative using pd.cut
# df['market_speed'] = pd.cut(df['days_on_market'], 
#                              bins=[0, 25, 50, float('inf')],
#                              labels=['Fast', 'Medium', 'Slow'])

# Statistics by category
speed_stats = df.groupby('market_speed').agg({
    'sale_price': 'mean',
    'property_id': 'count'
}).rename(columns={'property_id': 'count'})

# Calculate percentages
speed_stats['percentage'] = (speed_stats['count'] / len(df) * 100).round(2)

print(speed_stats)
print(f"\nPercentage of 'Fast' sales: {speed_stats.loc['Fast', 'percentage']:.2f}%")
```

### Key Concepts

- `apply()` with custom functions
- `pd.cut()` for binning continuous data
- Percentage calculations
- `.loc[]` for label-based indexing

---

## Problem 6: Premium Features Impact

### Approach

1. Filter data by feature presence
2. Calculate average prices for each group
3. Compute price differences and premiums

### Solution

```python
# Pool analysis
pool_yes = df[df['has_pool'] == 'Yes']['sale_price'].mean()
pool_no = df[df['has_pool'] == 'No']['sale_price'].mean()
pool_diff = pool_yes - pool_no
pool_premium = (pool_diff / pool_no * 100)

print("POOL ANALYSIS:")
print(f"With Pool: ${pool_yes:,.2f}")
print(f"Without Pool: ${pool_no:,.2f}")
print(f"Difference: ${pool_diff:,.2f}")
print(f"Premium: {pool_premium:.2f}%\n")

# Garage analysis
garage_yes = df[df['has_garage'] == 'Yes']['sale_price'].mean()
garage_no = df[df['has_garage'] == 'No']['sale_price'].mean()
garage_diff = garage_yes - garage_no
garage_premium = (garage_diff / garage_no * 100)

print("GARAGE ANALYSIS:")
print(f"With Garage: ${garage_yes:,.2f}")
print(f"Without Garage: ${garage_no:,.2f}")
print(f"Difference: ${garage_diff:,.2f}")
print(f"Premium: {garage_premium:.2f}%\n")

# Comparison
if pool_premium > garage_premium:
    print(f"Pool adds more value: {pool_premium:.2f}% vs {garage_premium:.2f}%")
else:
    print(f"Garage adds more value: {garage_premium:.2f}% vs {pool_premium:.2f}%")
```

### Key Concepts

- Boolean filtering
- Comparative analysis
- Percentage premium calculations
- String formatting with thousands separator

---

## Problem 7: Neighborhood Quality Score

### Why This Matters

Creating composite scores is crucial for:

- **Multi-Factor Decision Making**: Combining multiple criteria into one metric
- **Ranking Systems**: Creating fair comparison across different dimensions
- **Feature Engineering**: Building new meaningful variables for ML models
- **Business Metrics**: Developing KPIs that capture complex concepts

This teaches **normalization** and **weighted scoring** - essential for creating custom metrics in any business domain.

### Approach

1. Normalize crime_rate to 0-10 scale (inverted)
2. Calculate weighted composite score
3. Group by neighborhood and rank

### Solution

```python
# Normalize crime_rate to 0-10 scale (inverted - lower crime is better)
max_crime = df['crime_rate'].max()
min_crime = df['crime_rate'].min()
df['crime_score'] = 10 - ((df['crime_rate'] - min_crime) / (max_crime - min_crime) * 10)

# Calculate neighborhood quality score
df['neighborhood_quality_score'] = (
    df['school_rating'] * 0.4 +
    (df['walkability_score'] / 10) * 0.3 +  # Normalize to 0-10
    df['crime_score'] * 0.3
)

# Top 5 neighborhoods
top_neighborhoods = df.groupby('neighborhood')['neighborhood_quality_score'].mean().sort_values(ascending=False).head(5)

print("Top 5 Neighborhoods by Quality Score:")
for i, (neighborhood, score) in enumerate(top_neighborhoods.items(), 1):
    print(f"{i}. {neighborhood}: {score:.2f}")
```

### Key Concepts

- Min-max normalization
- Weighted scoring formulas
- Score inversion for inverse relationships
- `items()` for iterating over Series

---

## Problem 8: Property Age Analysis

### Approach

1. Calculate property age
2. Create age groups using `pd.cut()`
3. Analyze relationship with price
4. Visualize the trend

### Solution

```python
# Calculate property age
current_year = 2024
df['property_age'] = current_year - df['year_built']

# Create age groups
df['age_group'] = pd.cut(df['property_age'], 
                         bins=[0, 10, 20, 30, 40, 100],
                         labels=['0-10 years', '11-20 years', '21-30 years', 
                                '31-40 years', '40+ years'])

# Average sale price by age group
age_price = df.groupby('age_group', observed=True)['sale_price'].mean().sort_index()

print("Average Sale Price by Property Age:")
print(age_price)

# Visualization
plt.figure(figsize=(10, 6))
age_price.plot(kind='bar', color='coral')
plt.title('Average Sale Price by Property Age Group', fontsize=14, fontweight='bold')
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Average Sale Price ($)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, v in enumerate(age_price):
    plt.text(i, v, f'${v/1000:.0f}K', ha='center', va='bottom')

plt.tight_layout()
plt.show()
```

### Key Concepts

- Date calculations
- `pd.cut()` with custom bins and labels
- `observed=True` to avoid empty categories
- Adding text labels to bar charts

---

## Problem 9: Renovation Impact

### Approach

1. Handle null values in renovation year
2. Calculate years since renovation
3. Compare renovated vs non-renovated properties
4. Analyze recent renovations

### Solution

```python
# Identify renovated properties
df['is_renovated'] = df['last_renovation_year'].notna()

# Calculate years since renovation for renovated properties
df['years_since_renovation'] = current_year - df['last_renovation_year']

# Compare renovated vs non-renovated
renovated_avg = df[df['is_renovated']]['sale_price'].mean()
not_renovated_avg = df[~df['is_renovated']]['sale_price'].mean()
renovation_premium = ((renovated_avg - not_renovated_avg) / not_renovated_avg * 100)

print("RENOVATION IMPACT:")
print(f"Renovated properties: ${renovated_avg:,.2f}")
print(f"Non-renovated properties: ${not_renovated_avg:,.2f}")
print(f"Premium: {renovation_premium:.2f}%\n")

# Recent renovations (within last 5 years)
recent_reno = df[df['years_since_renovation'] <= 5]['sale_price'].mean()
older_reno = df[df['years_since_renovation'] > 5]['sale_price'].mean()

print("RECENT RENOVATION IMPACT:")
print(f"Recent renovation (≤5 years): ${recent_reno:,.2f}")
print(f"Older renovation (>5 years): ${older_reno:,.2f}")
print(f"Recent renovation premium: {((recent_reno - older_reno) / older_reno * 100):.2f}%")
```

### Key Concepts

- `notna()` for null checking
- Boolean negation with `~`
- Chained filtering conditions
- Handling missing data

---

## Problem 10: Commission Analysis

### Approach

1. Calculate total commission per agent
2. Find statistics on commission rates
3. Create scatter plot

### Solution

```python
# Total commission by agent (already calculated in Problem 2)
df['commission_earned'] = df['sale_price'] * df['commission_rate']

agent_commission = df.groupby('agent_name')['commission_earned'].sum().sort_values(ascending=False)

print(f"Agent with highest commission: {agent_commission.index[0]} - ${agent_commission.iloc[0]:,.2f}\n")

# Average commission rate
avg_commission_rate = df['commission_rate'].mean()
print(f"Average commission rate: {avg_commission_rate:.3f} ({avg_commission_rate*100:.1f}%)\n")

# Most common commission rate
most_common_rate = df['commission_rate'].mode()[0]
print(f"Most common commission rate: {most_common_rate} ({most_common_rate*100}%)\n")

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['sale_price'], df['commission_earned'], alpha=0.6, c=df['commission_rate'], 
            cmap='viridis', s=100, edgecolors='black', linewidth=0.5)
plt.colorbar(label='Commission Rate')
plt.title('Sale Price vs Commission Earned', fontsize=14, fontweight='bold')
plt.xlabel('Sale Price ($)', fontsize=12)
plt.ylabel('Commission Earned ($)', fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Key Concepts

- `mode()` for most frequent value
- Scatter plot with color mapping
- `colorbar()` for legend
- Alpha transparency for overlapping points

---

## Problem 11: Multi-Feature Property Search

### Approach

1. Apply multiple filter conditions
2. Chain boolean conditions with `&`
3. Sort and display results

### Solution

```python
# Apply all filters
filtered_properties = df[
    (df['bedrooms'] >= 3) &
    (df['bathrooms'] >= 2) &
    (df['school_rating'] >= 8) &
    (df['has_garage'] == 'Yes') &
    (df['sale_price'] <= 1500000) &
    (df['walkability_score'] >= 70)
].copy()

# Calculate price per sqft for filtered properties
filtered_properties['price_per_sqft'] = filtered_properties['sale_price'] / filtered_properties['square_feet']

# Sort by sale price
filtered_properties = filtered_properties.sort_values('sale_price')

# Display key columns
display_cols = ['address', 'city', 'bedrooms', 'bathrooms', 'school_rating', 
                'sale_price', 'price_per_sqft', 'walkability_score']
print(f"Found {len(filtered_properties)} properties matching criteria:\n")
print(filtered_properties[display_cols])

# Statistics
avg_price_per_sqft = filtered_properties['price_per_sqft'].mean()
print(f"\nAverage price per square foot: ${avg_price_per_sqft:.2f}")
```

### Key Concepts

- Multiple boolean conditions with `&`
- `.copy()` to avoid SettingWithCopyWarning
- Column selection for display
- Chained filtering

---

## Problem 12: Monthly Sales Trends

### Approach

1. Convert sale_date to datetime
2. Extract month information
3. Group by month and aggregate
4. Create trend visualization

### Solution

```python
# Convert to datetime
df['sale_date'] = pd.to_datetime(df['sale_date'])
df['sale_month'] = df['sale_date'].dt.month
df['sale_month_name'] = df['sale_date'].dt.strftime('%B')

# Monthly statistics
monthly_stats = df.groupby('sale_month').agg({
    'sale_price': ['sum', 'mean', 'count']
}).round(2)

monthly_stats.columns = ['total_sales_volume', 'avg_sale_price', 'properties_sold']

print("Monthly Sales Statistics:")
print(monthly_stats)

# Line chart
plt.figure(figsize=(12, 6))
plt.plot(monthly_stats.index, monthly_stats['properties_sold'], 
         marker='o', linewidth=2, markersize=8, color='steelblue')
plt.title('Properties Sold by Month', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Properties Sold', fontsize=12)
plt.grid(alpha=0.3)
plt.xticks(monthly_stats.index)

# Add value labels
for x, y in zip(monthly_stats.index, monthly_stats['properties_sold']):
    plt.text(x, y, str(int(y)), ha='center', va='bottom')

plt.tight_layout()
plt.show()
```

### Key Concepts

- `pd.to_datetime()` for date conversion
- `.dt` accessor for datetime operations
- `strftime()` for date formatting
- Multi-level column indexing after aggregation
- Line plots with markers

---

## Problem 13: Property Tax Analysis

### Approach

1. Calculate effective tax rate
2. Group by city and analyze
3. Check correlation
4. Create box plot by property type

### Solution

```python
# Calculate effective tax rate
df['effective_tax_rate'] = (df['property_tax'] / df['sale_price'] * 100)

# Average by city
city_tax_rate = df.groupby('city')['effective_tax_rate'].mean().sort_values(ascending=False)

print("Average Effective Tax Rate by City:")
print(city_tax_rate.head(10))
print(f"\nHighest: {city_tax_rate.index[0]} - {city_tax_rate.iloc[0]:.3f}%")
print(f"Lowest: {city_tax_rate.index[-1]} - {city_tax_rate.iloc[-1]:.3f}%\n")

# Correlation
correlation = df['property_tax'].corr(df['sale_price'])
print(f"Correlation between property tax and sale price: {correlation:.3f}\n")

# Box plot
plt.figure(figsize=(10, 6))
df.boxplot(column='property_tax', by='property_type', figsize=(10, 6))
plt.suptitle('')  # Remove default title
plt.title('Property Tax Distribution by Property Type', fontsize=14, fontweight='bold')
plt.xlabel('Property Type', fontsize=12)
plt.ylabel('Property Tax ($)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
```

### Key Concepts

- Percentage calculations
- `.corr()` between two Series
- Box plots for distribution analysis
- `suptitle('')` to remove default title

---

## Problem 14: Outlier Detection

### Approach

1. Calculate Q1, Q3, and IQR
2. Define outlier boundaries
3. Filter outliers
4. Calculate statistics

### Solution

```python
# Calculate quartiles and IQR
Q1 = df['sale_price'].quantile(0.25)
Q3 = df['sale_price'].quantile(0.75)
IQR = Q3 - Q1

# Define outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"Q1: ${Q1:,.2f}")
print(f"Q3: ${Q3:,.2f}")
print(f"IQR: ${IQR:,.2f}")
print(f"Lower Bound: ${lower_bound:,.2f}")
print(f"Upper Bound: ${upper_bound:,.2f}\n")

# Identify outliers
outliers = df[(df['sale_price'] < lower_bound) | (df['sale_price'] > upper_bound)]

print(f"Number of outliers: {len(outliers)}")
print(f"Percentage of outliers: {(len(outliers) / len(df) * 100):.2f}%\n")

# Display outlier properties
display_cols = ['address', 'city', 'property_type', 'sale_price', 'square_feet', 
                'bedrooms', 'bathrooms', 'school_rating']
print("Outlier Properties:")
print(outliers[display_cols].sort_values('sale_price'))
```

### Key Concepts

- `quantile()` for percentile calculations
- IQR method for outlier detection
- Boolean OR operator `|`
- Statistical analysis of distributions

---

## Problem 15: Comprehensive Property Ranking

### Approach

1. Normalize all metrics to 0-1 scale
2. Invert metrics where lower is better
3. Calculate weighted composite score
4. Rank properties

### Solution

```python
from sklearn.preprocessing import MinMaxScaler

# Create a copy for scoring
scoring_df = df.copy()

# Calculate price per sqft
scoring_df['price_per_sqft'] = scoring_df['sale_price'] / scoring_df['square_feet']

# Select features for normalization
features_to_normalize = ['price_per_sqft', 'school_rating', 'walkability_score', 
                         'days_on_market', 'crime_rate']

# Normalize features
scaler = MinMaxScaler()
normalized = scaler.fit_transform(scoring_df[features_to_normalize])

# Create normalized columns
for i, feature in enumerate(features_to_normalize):
    scoring_df[f'{feature}_norm'] = normalized[:, i]

# Calculate value score (invert where lower is better)
scoring_df['value_score'] = (
    (1 - scoring_df['price_per_sqft_norm']) * 0.2 +  # Lower price/sqft is better
    scoring_df['school_rating_norm'] * 0.2 +          # Higher is better
    scoring_df['walkability_score_norm'] * 0.2 +      # Higher is better
    (1 - scoring_df['days_on_market_norm']) * 0.2 +   # Lower is better
    (1 - scoring_df['crime_rate_norm']) * 0.2         # Lower is better
)

# Get top 10 properties
top_10 = scoring_df.nlargest(10, 'value_score')

# Display results
display_cols = ['address', 'city', 'property_type', 'sale_price', 'value_score',
                'school_rating', 'walkability_score', 'days_on_market']
print("Top 10 Properties by Value Score:")
print(top_10[display_cols].reset_index(drop=True))
```

### Key Concepts

- `MinMaxScaler` from sklearn for normalization
- Composite scoring with multiple factors
- Score inversion for inverse relationships
- `nlargest()` for top N selection
- Equal weighting of multiple factors

---

## Bonus Challenge: Simple Linear Regression

### Approach

1. Prepare features and target
2. Split data (optional for this exercise)
3. Train linear regression model
4. Evaluate and predict

### Solution

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# Prepare features and target
features = ['square_feet', 'bedrooms', 'bathrooms', 'school_rating']
X = df[features]
y = df['sale_price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("Model Performance:")
print(f"R² Score: {r2:.3f}")
print(f"Mean Absolute Error: ${mae:,.2f}\n")

# Feature importance
print("Feature Coefficients:")
for feature, coef in zip(features, model.coef_):
    print(f"{feature}: ${coef:,.2f}")
print(f"Intercept: ${model.intercept_:,.2f}\n")

# Predict for hypothetical property
hypothetical = [[2000, 3, 2, 8]]  # 2000 sqft, 3 bed, 2 bath, rating 8
prediction = model.predict(hypothetical)

print(f"Predicted price for hypothetical property:")
print(f"2000 sq ft, 3 bedrooms, 2 bathrooms, school rating 8")
print(f"Predicted Sale Price: ${prediction[0]:,.2f}")
```

### Key Concepts

- `train_test_split()` for data splitting
- `LinearRegression()` model training
- `r2_score()` for model evaluation
- Feature coefficients interpretation
- Making predictions with new data

---

## General Tips for All Problems

### Data Exploration

```python
# Always start with these
df.info()                    # Data types and null values
df.describe()                # Statistical summary
df.head()                    # First few rows
df.shape                     # Dimensions
df.columns                   # Column names
df.isnull().sum()           # Count of null values
```

### Common Pandas Operations

```python
# Filtering
df[df['column'] > value]
df[(df['col1'] > val1) & (df['col2'] == val2)]

# Grouping
df.groupby('column').agg({'col1': 'mean', 'col2': 'sum'})

# Sorting
df.sort_values('column', ascending=False)

# Creating new columns
df['new_col'] = df['col1'] + df['col2']
```

### Visualization Best Practices

```python
# Always include:
plt.figure(figsize=(width, height))  # Set size
plt.title('Title', fontsize=14)      # Clear title
plt.xlabel('X Label', fontsize=12)   # Axis labels
plt.ylabel('Y Label', fontsize=12)
plt.grid(alpha=0.3)                  # Grid for readability
plt.tight_layout()                   # Prevent label cutoff
plt.show()                           # Display plot
```

---

## Summary

These 15 problems cover essential data analysis skills:

✅ **Aggregation & Grouping** - Problems 1, 2, 7
✅ **Derived Metrics** - Problems 3, 8, 13
✅ **Correlation Analysis** - Problem 4
✅ **Categorical Analysis** - Problems 5, 6
✅ **Time Series** - Problem 12
✅ **Filtering & Selection** - Problem 11
✅ **Statistical Analysis** - Problem 14
✅ **Composite Scoring** - Problems 7, 15
✅ **Data Visualization** - All problems
✅ **Machine Learning** - Bonus problem

Practice these solutions, understand the concepts, and try variations to deepen your understanding! 🚀

---

## The Learning Journey

These 15 problems follow a **progressive learning path**:

**Foundation (Problems 1-3)**: Basic aggregation, grouping, and derived metrics

- Learn to summarize data by categories
- Calculate new columns from existing ones
- Create simple visualizations

**Intermediate (Problems 4-9)**: Statistical analysis and feature engineering

- Understand relationships between variables
- Create categorical variables from continuous ones
- Compare groups and calculate premiums
- Build composite scores

**Advanced (Problems 10-15)**: Complex filtering, outlier detection, and ranking

- Multi-criteria filtering for business use cases
- Time series analysis
- Statistical outlier detection
- Multi-factor normalization and scoring
- Introduction to predictive modeling

**Real-World Application**: Each problem mirrors actual business scenarios:

- Problem 1 = Market segmentation reports
- Problem 2 = Sales team dashboards
- Problem 4 = Feature selection for ML
- Problem 7 = Location scoring systems
- Problem 11 = Property search engines
- Problem 15 = Recommendation systems

By completing these exercises, you're not just learning pandas syntax - you're developing the **analytical thinking** that separates good data analysts from great ones.
