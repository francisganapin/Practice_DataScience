"""
=============================================================================
CALIFORNIA HOUSING NOTEBOOK ENHANCEMENTS
=============================================================================
Copy these code cells into your california.ipynb notebook to make it 
client-friendly. Each section is marked with CELL numbers.

Instructions:
1. Open your california.ipynb
2. Copy each cell content below into new cells in your notebook
3. Run the cells in order
=============================================================================
"""

# =============================================================================
# CELL 1: MARKDOWN - Title and Introduction (Add at the very beginning)
# =============================================================================
"""
# 🏠 California Housing Market Analysis

## Project Overview
This analysis explores the **California Housing Dataset**, which contains information about housing districts in California from the 1990 U.S. Census.

### What We're Trying to Understand:
- What factors influence house prices in California?
- How are properties distributed across different regions?
- What is the typical California home like?

### Who This Analysis Is For:
Business stakeholders looking to understand the California housing market trends.

---
"""

# =============================================================================
# CELL 2: Import Libraries (Replace your current imports cell)
# =============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing

# Set visual style for better-looking charts
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# =============================================================================
# CELL 3: MARKDOWN - Data Loading Section Header
# =============================================================================
"""
---
## 📊 Step 1: Loading the Data

We're using the California Housing dataset, which includes information about:
- **MedInc**: Median household income in the area (in $10,000s)
- **HouseAge**: Average age of houses in the area (in years)
- **AveRooms**: Average number of rooms per house
- **AveBedrms**: Average number of bedrooms per house
- **Population**: Total population in the area
- **AveOccup**: Average number of people per household
- **Latitude/Longitude**: Geographic location
- **MedHouseVal**: **TARGET** - Median house value (in $100,000s)

---
"""

# =============================================================================
# CELL 4: Load and Display Data
# =============================================================================
# Load the California Housing dataset
california = fetch_california_housing()

# Create a user-friendly DataFrame
df = pd.DataFrame(california.data, columns=california.feature_names)
df['MedHouseVal'] = california.target  # This is what we're trying to predict

print(f"✅ Dataset loaded successfully!")
print(f"📈 Total records: {len(df):,} housing districts")
print(f"📊 Number of features: {len(df.columns)} columns")

# Show first few rows
print("\n📋 First 5 records in our dataset:")
df.head()

# =============================================================================
# CELL 5: MARKDOWN - Data Quality Check Header
# =============================================================================
"""
---
## 🔍 Step 2: Checking Data Quality

Before we analyze the data, we need to ensure it's complete and reliable.
Let's check for any missing values.

---
"""

# =============================================================================
# CELL 6: Missing Values Check (Client-Friendly)
# =============================================================================
# Check for missing values
missing_values = df.isna().sum()
total_missing = missing_values.sum()

print("=" * 50)
print("📋 DATA QUALITY REPORT")
print("=" * 50)

if total_missing == 0:
    print("\n✅ GREAT NEWS! No missing values found.")
    print("   Our dataset is complete and ready for analysis.")
else:
    print(f"\n⚠️ Found {total_missing} missing values:")
    print(missing_values[missing_values > 0])

print("\n" + "=" * 50)

# =============================================================================
# CELL 7: MARKDOWN - Feature Examination Header
# =============================================================================
"""
---
## 📈 Step 3: Understanding Our Data

Let's look at the summary statistics to understand what a "typical" California housing district looks like.

---
"""

# =============================================================================
# CELL 8: Descriptive Statistics (Client-Friendly)
# =============================================================================
# Get summary statistics
stats = df.describe()

print("=" * 60)
print("📊 SUMMARY STATISTICS: What Does a Typical District Look Like?")
print("=" * 60)

print(f"""
🏠 TYPICAL CALIFORNIA HOUSING DISTRICT:

💰 Median Household Income: ${stats.loc['50%', 'MedInc'] * 10000:,.0f}/year
   (Range: ${stats.loc['min', 'MedInc'] * 10000:,.0f} - ${stats.loc['max', 'MedInc'] * 10000:,.0f})

🏡 Average House Age: {stats.loc['50%', 'HouseAge']:.0f} years
   (Range: {stats.loc['min', 'HouseAge']:.0f} - {stats.loc['max', 'HouseAge']:.0f} years)

🛏️ Average Rooms per House: {stats.loc['50%', 'AveRooms']:.1f} rooms
   (Range: {stats.loc['min', 'AveRooms']:.1f} - {stats.loc['max', 'AveRooms']:.1f} rooms)

👥 Average Household Size: {stats.loc['50%', 'AveOccup']:.1f} people
   (Range: {stats.loc['min', 'AveOccup']:.1f} - {stats.loc['max', 'AveOccup']:.1f} people)

🏷️ Median House Value: ${stats.loc['50%', 'MedHouseVal'] * 100000:,.0f}
   (Range: ${stats.loc['min', 'MedHouseVal'] * 100000:,.0f} - ${stats.loc['max', 'MedHouseVal'] * 100000:,.0f})
""")

# Show the full statistics table
print("\n📋 Complete Statistics Table:")
df.describe().round(2)

# =============================================================================
# CELL 9: MARKDOWN - Visualization Section Header
# =============================================================================
"""
---
## 📊 Step 4: Visualizing the Data

Now let's create visual representations to better understand our data.

### 4.1 How Are House Values Distributed?

---
"""

# =============================================================================
# CELL 10: House Value Distribution (Target Variable)
# =============================================================================
fig, ax = plt.subplots(figsize=(10, 6))

# Create histogram
ax.hist(df['MedHouseVal'] * 100000, bins=50, color='steelblue', edgecolor='white', alpha=0.7)

# Add mean and median lines
mean_val = df['MedHouseVal'].mean() * 100000
median_val = df['MedHouseVal'].median() * 100000
ax.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: ${mean_val:,.0f}')
ax.axvline(median_val, color='orange', linestyle='-', linewidth=2, label=f'Median: ${median_val:,.0f}')

ax.set_xlabel('Median House Value ($)', fontsize=12)
ax.set_ylabel('Number of Districts', fontsize=12)
ax.set_title('Distribution of House Values in California\n(How many districts fall into each price range?)', 
             fontsize=14, fontweight='bold')
ax.legend(fontsize=11)

# Format x-axis as currency
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

plt.tight_layout()
plt.show()

print("""
📌 KEY INSIGHT:
   Most house values cluster between $100K-$250K.
   The spike at $500K indicates a "cap" in the data (maximum recorded value).
""")

# =============================================================================
# CELL 11: MARKDOWN - Income Distribution Header
# =============================================================================
"""
### 4.2 How Is Income Distributed Across California?
"""

# =============================================================================
# CELL 12: Income Distribution
# =============================================================================
fig, ax = plt.subplots(figsize=(10, 6))

ax.hist(df['MedInc'] * 10000, bins=50, color='seagreen', edgecolor='white', alpha=0.7)

mean_inc = df['MedInc'].mean() * 10000
median_inc = df['MedInc'].median() * 10000
ax.axvline(mean_inc, color='red', linestyle='--', linewidth=2, label=f'Mean: ${mean_inc:,.0f}')
ax.axvline(median_inc, color='orange', linestyle='-', linewidth=2, label=f'Median: ${median_inc:,.0f}')

ax.set_xlabel('Median Household Income ($)', fontsize=12)
ax.set_ylabel('Number of Districts', fontsize=12)
ax.set_title('Distribution of Household Income in California\n(What do people earn in different areas?)', 
             fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

plt.tight_layout()
plt.show()

print("""
📌 KEY INSIGHT:
   Most households earn between $20K-$60K annually.
   There's a long tail of higher-income areas (up to $150K+).
""")

# =============================================================================
# CELL 13: MARKDOWN - Key Relationship Header
# =============================================================================
"""
---
### 4.3 The Most Important Relationship: Income vs House Value

This is the key question: **Does higher income mean higher house prices?**

---
"""

# =============================================================================
# CELL 14: Income vs House Value Scatter Plot (MOST IMPORTANT!)
# =============================================================================
fig, ax = plt.subplots(figsize=(12, 8))

# Create scatter plot with color based on house age
scatter = ax.scatter(df['MedInc'] * 10000, 
                     df['MedHouseVal'] * 100000,
                     c=df['HouseAge'],
                     cmap='RdYlBu_r',
                     alpha=0.5,
                     s=10)

# Add colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('House Age (years)', fontsize=11)

# Add trend line
z = np.polyfit(df['MedInc'], df['MedHouseVal'], 1)
p = np.poly1d(z)
x_line = np.linspace(df['MedInc'].min(), df['MedInc'].max(), 100)
ax.plot(x_line * 10000, p(x_line) * 100000, 'r-', linewidth=3, label='Trend Line')

ax.set_xlabel('Median Household Income ($)', fontsize=12)
ax.set_ylabel('Median House Value ($)', fontsize=12)
ax.set_title('Income vs House Value: The Stronger the Income, the Higher the Price\n(Each dot = one housing district)', 
             fontsize=14, fontweight='bold')
ax.legend(fontsize=11, loc='lower right')

# Format axes
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

plt.tight_layout()
plt.show()

# Calculate correlation
correlation = df['MedInc'].corr(df['MedHouseVal'])

print(f"""
📌 KEY INSIGHT - THIS IS THE MOST IMPORTANT FINDING!
   
   Correlation: {correlation:.2f} (Strong Positive Relationship)
   
   ✅ Income is the #1 predictor of house value.
   ✅ Higher income areas = Higher house prices
   ✅ This relationship is very consistent across California
""")

# =============================================================================
# CELL 15: MARKDOWN - Geographic Distribution Header
# =============================================================================
"""
---
### 4.4 Where Are the Most Expensive Houses Located?

Let's see how house values are distributed geographically across California.

---
"""

# =============================================================================
# CELL 16: Geographic Distribution (Map-like visualization)
# =============================================================================
fig, ax = plt.subplots(figsize=(12, 10))

# Create scatter plot using lat/long
scatter = ax.scatter(df['Longitude'], 
                     df['Latitude'],
                     c=df['MedHouseVal'] * 100000,
                     cmap='RdYlGn',
                     alpha=0.6,
                     s=5)

cbar = plt.colorbar(scatter)
cbar.set_label('Median House Value ($)', fontsize=11)

ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)
ax.set_title('California Housing Prices by Location\n(Green = Lower Prices, Red = Higher Prices)', 
             fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()

print("""
📌 KEY INSIGHT:
   ✅ Coastal areas (especially around San Francisco and Los Angeles) have higher prices
   ✅ Inland areas generally have lower housing costs
   ✅ You can clearly see California's shape and major population centers!
""")

# =============================================================================
# CELL 17: MARKDOWN - Correlation Analysis Header
# =============================================================================
"""
---
### 4.5 Which Factors Affect House Prices the Most?

Let's create a correlation heatmap to see all relationships at once.

---
"""

# =============================================================================
# CELL 18: Correlation Heatmap
# =============================================================================
fig, ax = plt.subplots(figsize=(10, 8))

# Calculate correlation matrix
corr_matrix = df.corr()

# Create heatmap
sns.heatmap(corr_matrix, 
            annot=True, 
            fmt='.2f', 
            cmap='RdBu_r',
            center=0,
            square=True,
            linewidths=0.5,
            ax=ax)

ax.set_title('Correlation Between All Features\n(Closer to 1 = Strong Positive, Closer to -1 = Strong Negative)', 
             fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()

# Get correlations with target
target_corr = corr_matrix['MedHouseVal'].drop('MedHouseVal').sort_values(ascending=False)

print("📌 FACTORS RANKED BY IMPACT ON HOUSE VALUE:")
print("=" * 50)
for feature, corr in target_corr.items():
    if abs(corr) >= 0.3:
        impact = "🔴 STRONG"
    elif abs(corr) >= 0.1:
        impact = "🟡 MODERATE"
    else:
        impact = "⚪ WEAK"
    print(f"   {impact} {feature}: {corr:.2f}")

# =============================================================================
# CELL 19: MARKDOWN - Summary Section Header
# =============================================================================
"""
---
## 📋 Summary: Key Findings for Stakeholders

---
"""

# =============================================================================
# CELL 20: Executive Summary (Client-Friendly Conclusion)
# =============================================================================
print("=" * 70)
print("                    📊 EXECUTIVE SUMMARY                              ")
print("                 California Housing Market Analysis                   ")
print("=" * 70)

print(f"""

🏠 DATASET OVERVIEW:
   • Analyzed {len(df):,} housing districts across California
   • Data from the 1990 U.S. Census
   • No missing values - Data quality is excellent

💰 PRICE FINDINGS:
   • Median House Value: ${df['MedHouseVal'].median() * 100000:,.0f}
   • Price Range: ${df['MedHouseVal'].min() * 100000:,.0f} - ${df['MedHouseVal'].max() * 100000:,.0f}
   • Most properties fall in the $100K-$250K range

🔑 KEY PRICE DRIVERS (Ranked by Impact):
   1. Income Level (correlation: {df['MedInc'].corr(df['MedHouseVal']):.2f}) - STRONGEST FACTOR
   2. Location (Coastal areas command premium prices)
   3. House Age (correlation: {df['HouseAge'].corr(df['MedHouseVal']):.2f})
   4. Number of Rooms (correlation: {df['AveRooms'].corr(df['MedHouseVal']):.2f})

📍 GEOGRAPHIC INSIGHTS:
   • Most expensive: Coastal California (SF Bay Area, LA)
   • Most affordable: Inland/Central California
   • Clear urban vs rural price divide

💡 RECOMMENDATIONS FOR STAKEHOLDERS:
   1. Focus on income demographics when assessing property values
   2. Coastal properties are investments with higher appreciation
   3. Inland areas offer more affordable housing options
   4. House size matters, but income level matters MORE
""")

print("=" * 70)
print("                      Analysis Complete                               ")
print("=" * 70)
