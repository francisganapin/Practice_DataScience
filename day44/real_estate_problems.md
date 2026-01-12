# 🏠 Real Estate Data Analytics Problems

**Dataset:** `real_estate_data.csv`

Use Python (pandas, numpy, matplotlib/seaborn) to solve these problems. Start by loading the data:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('real_estate_data.csv')
```

---

## 📊 BEGINNER LEVEL (Problems 1-5)

### Problem 1: Basic Exploration
**Task:** Load the dataset and answer:
- How many properties are in the dataset?
- What are the column names and their data types?
- Are there any missing values?

**Skills:** `df.shape`, `df.info()`, `df.isnull().sum()`

---

### Problem 2: Property Type Distribution
**Task:** Find the count and percentage of each property type (Single Family, Condo, Townhouse).

**Expected Output Format:**
```
Property Type    Count    Percentage
Single Family    14       46.67%
Condo            10       33.33%
Townhouse        6        20.00%
```

**Skills:** `value_counts()`, percentage calculation

---

### Problem 3: Average Prices by City
**Task:** Calculate the average listing price and average sold price for each city. Which city has the highest average sold price?

**Skills:** `groupby()`, `mean()`, sorting

---

### Problem 4: Price Per Square Foot
**Task:** Create a new column called `price_per_sqft` (using sold_price / sqft). Find the top 5 properties with the highest price per square foot.

**Skills:** Creating new columns, `nlargest()` or `sort_values()`

---

### Problem 5: Pool Properties Analysis
**Task:** 
- How many properties have a pool?
- What is the average sold price of properties WITH a pool vs WITHOUT a pool?
- Is there a significant price difference?

**Skills:** Boolean filtering, `groupby()`, comparison analysis

---

## 📈 INTERMEDIATE LEVEL (Problems 6-10)

### Problem 6: Agent Performance Analysis
**Task:** For each agent, calculate:
- Total number of properties sold
- Total sales volume (sum of sold_price)
- Average days on market for their listings

Rank agents by total sales volume.

**Skills:** `groupby()` with multiple aggregations, `agg()`

---

### Problem 7: Price Negotiation Analysis
**Task:** 
- Create a column `price_difference` = listing_price - sold_price
- Create a column `price_diff_pct` = (price_difference / listing_price) * 100
- Which property type has the highest average negotiation discount?
- Find properties that sold ABOVE listing price

**Skills:** Feature engineering, conditional filtering

---

### Problem 8: Market Speed by State
**Task:** Analyze how quickly properties sell in different states:
- Average days on market by state
- Median days on market by state
- Create a bar chart visualizing average days on market by state

**Skills:** `groupby()`, `median()`, matplotlib/seaborn visualization

---

### Problem 9: Correlation Analysis
**Task:** 
- Calculate the correlation between: sqft, bedrooms, bathrooms, school_rating, walkability_score, and sold_price
- Create a correlation heatmap
- Which feature has the strongest positive correlation with sold price?

**Skills:** `corr()`, heatmap visualization, interpreting correlations

---

### Problem 10: Time-Based Analysis
**Task:** 
- Convert listing_date and sold_date to datetime
- Find which month had the most listings
- Calculate the average sale price by listing month
- Is there a seasonal pattern?

**Skills:** `pd.to_datetime()`, `dt.month`, time series grouping

---

## 🚀 ADVANCED LEVEL (Problems 11-15)

### Problem 11: Market Segmentation
**Task:** Create market segments based on price:
- Budget: sold_price < $400,000
- Mid-Range: $400,000 <= sold_price < $600,000
- Premium: $600,000 <= sold_price < $800,000
- Luxury: sold_price >= $800,000

For each segment, find:
- Count of properties
- Average sqft
- Average days on market
- Most common property type

**Skills:** `pd.cut()` or conditional logic, multi-level aggregation

---

### Problem 12: ROI & Investment Analysis
**Task:** 
- Assume annual appreciation rate of 3% based on year_built to current year (2024)
- Calculate estimated original purchase price
- Calculate total appreciation for each property
- Which neighborhood has the best estimated ROI?

**Formula hint:** `original_price = sold_price / (1.03 ** years_since_built)`

**Skills:** Financial calculations, feature engineering, complex aggregations

---

### Problem 13: Predictive Feature Importance
**Task:** Build a simple linear regression model to predict sold_price using:
- sqft, bedrooms, bathrooms, year_built, school_rating, walkability_score

Answer:
- What is the R² score of your model?
- Which features are most important (highest coefficients)?
- What would be the predicted price for a 2000 sqft, 3 bed, 2 bath property built in 2010 with school_rating 8 and walkability 75?

**Skills:** `sklearn`, LinearRegression, model evaluation

---

### Problem 14: Anomaly Detection
**Task:** Identify potential outliers/anomalies in the dataset:
- Properties where price_per_sqft is more than 2 standard deviations from the mean
- Properties where days_on_market is unusually high (> 1.5 * IQR above Q3)
- Properties that sold more than 5% above listing price

For each anomaly type, investigate why these properties might be outliers.

**Skills:** Statistical analysis, Z-scores, IQR method, data investigation

---

### Problem 15: Comprehensive Market Report
**Task:** Create a complete market analysis report that includes:

1. **Executive Summary:** Key metrics (total volume, avg price, avg days on market)
2. **Geographic Analysis:** Best/worst performing cities and states
3. **Agent Leaderboard:** Top 3 agents by volume and efficiency
4. **Price Trend Visualization:** Multiple charts showing:
   - Price distribution histogram
   - Boxplot of prices by property type
   - Scatter plot: sqft vs sold_price colored by property type
5. **Recommendations:** Based on data, which areas should investors focus on?

**Skills:** Data storytelling, multiple visualizations, business insights

---

## 🎯 How to Use This Problem Set

1. **Start with Problems 1-5** to warm up with basic pandas operations
2. **Progress to 6-10** for more complex analysis
3. **Challenge yourself with 11-15** for real-world analytics scenarios
4. **Use the cheat sheet** (`cheat_sheet.md`) when you get stuck
5. **Save your solutions** in a Jupyter notebook or Python script

---

## ✅ Solution Hints (Don't peek until you try!)

<details>
<summary>Click to reveal hints for each problem</summary>

**P1:** Use `df.shape[0]` for row count, `df.dtypes` for types
**P2:** `df['property_type'].value_counts(normalize=True) * 100`
**P3:** `df.groupby('city')[['listing_price', 'sold_price']].mean()`
**P4:** `df['price_per_sqft'] = df['sold_price'] / df['sqft']`
**P5:** `df.groupby('has_pool')['sold_price'].mean()`
**P6:** Use `agg({'property_id': 'count', 'sold_price': 'sum', 'days_on_market': 'mean'})`
**P7:** Properties above listing: `df[df['sold_price'] > df['listing_price']]`
**P8:** `df.groupby('state')['days_on_market'].agg(['mean', 'median'])`
**P9:** `df[numeric_cols].corr()` then `sns.heatmap()`
**P10:** `df['listing_date'] = pd.to_datetime(df['listing_date'])`
**P11:** Use `pd.cut(df['sold_price'], bins=[0, 400000, 600000, 800000, float('inf')])`
**P12:** `years = 2024 - df['year_built']`
**P13:** `from sklearn.linear_model import LinearRegression`
**P14:** `z_scores = (df['price_per_sqft'] - mean) / std`
**P15:** Combine multiple groupby and visualization techniques

</details>

---

**Good luck! 🍀 Happy analyzing!**
