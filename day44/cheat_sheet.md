# 📋 Data Analytics Cheat Sheet (Python/Pandas)

## 🔧 Setup & Imports

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
```

---

## 📂 Loading Data

```python
# CSV
df = pd.read_csv('file.csv')

# Excel
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')

# JSON
df = pd.read_json('file.json')
```

---

## 🔍 Data Exploration

| Task | Code |
|------|------|
| First n rows | `df.head(n)` |
| Last n rows | `df.tail(n)` |
| Shape (rows, cols) | `df.shape` |
| Column names | `df.columns` |
| Data types | `df.dtypes` |
| Summary info | `df.info()` |
| Statistics | `df.describe()` |
| Unique values | `df['col'].unique()` |
| Value counts | `df['col'].value_counts()` |
| Null check | `df.isnull().sum()` |

---

## 🎯 Selecting Data

```python
# Single column
df['column_name']

# Multiple columns
df[['col1', 'col2', 'col3']]

# Rows by index
df.iloc[0:5]        # First 5 rows
df.iloc[0:5, 0:3]   # First 5 rows, first 3 columns

# Rows by label
df.loc[df['city'] == 'Seattle']

# Multiple conditions
df[(df['price'] > 500000) & (df['bedrooms'] >= 3)]
df[(df['city'] == 'LA') | (df['city'] == 'SF')]
```

---

## 🧮 Creating & Modifying Columns

```python
# New column from calculation
df['price_per_sqft'] = df['sold_price'] / df['sqft']

# Conditional column
df['is_expensive'] = df['price'] > 500000

# Apply function
df['city_upper'] = df['city'].apply(lambda x: x.upper())

# Using np.where (if-else)
df['status'] = np.where(df['days'] < 30, 'Fast', 'Slow')

# Multiple conditions with np.select
conditions = [
    df['price'] < 400000,
    df['price'] < 600000,
    df['price'] >= 600000
]
choices = ['Budget', 'Mid-Range', 'Premium']
df['segment'] = np.select(conditions, choices)

# Binning with pd.cut
df['price_bin'] = pd.cut(df['price'], 
                         bins=[0, 400000, 600000, 1000000], 
                         labels=['Low', 'Medium', 'High'])
```

---

## 📊 Grouping & Aggregation

```python
# Single aggregation
df.groupby('city')['price'].mean()

# Multiple aggregations
df.groupby('city')['price'].agg(['mean', 'median', 'std', 'count'])

# Multiple columns, multiple aggregations
df.groupby('city').agg({
    'sold_price': ['mean', 'sum'],
    'days_on_market': 'mean',
    'property_id': 'count'
})

# Reset index after groupby
df.groupby('city')['price'].mean().reset_index()

# Named aggregations (cleaner output)
df.groupby('city').agg(
    avg_price=('sold_price', 'mean'),
    total_sales=('sold_price', 'sum'),
    count=('property_id', 'count')
)
```

---

## 📈 Sorting

```python
# Sort by column (ascending)
df.sort_values('price')

# Sort descending
df.sort_values('price', ascending=False)

# Sort by multiple columns
df.sort_values(['city', 'price'], ascending=[True, False])

# Top N values
df.nlargest(5, 'price')
df.nsmallest(5, 'days_on_market')
```

---

## 🔄 Handling Missing Data

```python
# Check nulls
df.isnull().sum()

# Drop rows with any null
df.dropna()

# Drop rows where specific column is null
df.dropna(subset=['price'])

# Fill with value
df['col'].fillna(0)

# Fill with mean
df['col'].fillna(df['col'].mean())

# Forward/backward fill
df['col'].ffill()  # forward
df['col'].bfill()  # backward
```

---

## 📅 Date Operations

```python
# Convert to datetime
df['date'] = pd.to_datetime(df['date'])

# Extract components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.dayofweek  # 0=Monday
df['quarter'] = df['date'].dt.quarter

# Date difference
df['days_diff'] = (df['sold_date'] - df['listing_date']).dt.days

# Filter by date
df[df['date'] >= '2024-01-01']
df[df['date'].between('2024-01-01', '2024-03-31')]
```

---

## 🔗 Merging & Joining

```python
# Merge (SQL-like join)
pd.merge(df1, df2, on='key_column')
pd.merge(df1, df2, left_on='col1', right_on='col2')
pd.merge(df1, df2, on='key', how='left')   # left, right, outer, inner

# Concatenate
pd.concat([df1, df2])           # stack vertically
pd.concat([df1, df2], axis=1)   # stack horizontally
```

---

## 📉 Statistics & Correlation

```python
# Basic stats
df['col'].mean()
df['col'].median()
df['col'].std()
df['col'].var()
df['col'].min()
df['col'].max()
df['col'].sum()
df['col'].quantile(0.25)  # 25th percentile

# Correlation matrix
df[['price', 'sqft', 'beds']].corr()

# Specific correlation
df['price'].corr(df['sqft'])
```

---

## 📊 Visualization Quick Reference

### Histogram
```python
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=20, edgecolor='black')
plt.xlabel('Price')
plt.ylabel('Count')
plt.title('Price Distribution')
plt.show()
```

### Bar Chart
```python
df.groupby('city')['price'].mean().plot(kind='bar', figsize=(10,6))
plt.title('Average Price by City')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Box Plot
```python
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='property_type', y='sold_price')
plt.title('Price by Property Type')
plt.show()
```

### Scatter Plot
```python
plt.figure(figsize=(10, 6))
plt.scatter(df['sqft'], df['price'], alpha=0.5)
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.title('Price vs Square Feet')
plt.show()

# With color by category
sns.scatterplot(data=df, x='sqft', y='price', hue='property_type')
```

### Heatmap (Correlation)
```python
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()
```

### Multiple Subplots
```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].hist(df['price'])
axes[0].set_title('Price Distribution')

axes[1].scatter(df['sqft'], df['price'])
axes[1].set_title('Price vs Sqft')

plt.tight_layout()
plt.show()
```

---

## 🤖 Simple Machine Learning (sklearn)

### Linear Regression
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# Prepare data
X = df[['sqft', 'bedrooms', 'bathrooms']]
y = df['sold_price']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
print(f"R² Score: {r2_score(y_test, predictions):.3f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, predictions)):.2f}")

# Coefficients
for feat, coef in zip(X.columns, model.coef_):
    print(f"{feat}: {coef:.2f}")
```

---

## 🎯 Outlier Detection

```python
# Z-Score Method
from scipy import stats
z_scores = np.abs(stats.zscore(df['price']))
outliers = df[z_scores > 2]  # > 2 std deviations

# IQR Method
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df['price'] < lower) | (df['price'] > upper)]
```

---

## 💾 Saving Results

```python
# To CSV
df.to_csv('output.csv', index=False)

# To Excel
df.to_excel('output.xlsx', index=False)

# Save plot
plt.savefig('chart.png', dpi=300, bbox_inches='tight')
```

---

## ⚡ Quick Pandas Tips

```python
# Display options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.float_format', '{:.2f}'.format)

# Reset options
pd.reset_option('all')

# Memory usage
df.memory_usage(deep=True)

# Copy DataFrame
df_copy = df.copy()

# Rename columns
df.rename(columns={'old_name': 'new_name'})

# Drop columns
df.drop(columns=['col1', 'col2'])

# Drop duplicates
df.drop_duplicates()
df.drop_duplicates(subset=['col1'])

# String operations
df['city'].str.lower()
df['city'].str.upper()
df['city'].str.contains('San')
df['city'].str.replace('Old', 'New')
```

---

## 🔥 Common Real Estate Formulas

```python
# Price per square foot
df['price_per_sqft'] = df['sold_price'] / df['sqft']

# Price difference (negotiation)
df['price_diff'] = df['listing_price'] - df['sold_price']
df['price_diff_pct'] = (df['price_diff'] / df['listing_price']) * 100

# Appreciation (simple annual)
years = 2024 - df['year_built']
df['appreciation'] = df['sold_price'] / (1.03 ** years)

# Cap Rate (if rental data available)
# cap_rate = (annual_rent - expenses) / property_value * 100

# ROI
# roi = (current_value - purchase_price) / purchase_price * 100
```

---

**🎓 Pro Tips:**
1. Always explore data first with `.info()` and `.describe()`
2. Check for nulls before analysis
3. Use descriptive variable names
4. Comment your code
5. Save intermediate results to avoid re-running

**Happy Analyzing! 📊**
