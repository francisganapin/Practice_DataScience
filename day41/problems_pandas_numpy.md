# 15 Medium Real Estate Problems - Pandas & NumPy

## Dataset: `real_estate_data.csv`

---

### Problem 1: Calculate Price Per Square Foot
Create a new column `price_per_sqft` by dividing `sold_price` by `area_sqft`. Find the top 5 properties with the highest price per square foot.

---

### Problem 2: Profit/Loss Calculation
Create a column `price_difference` that shows the difference between `listing_price` and `sold_price`. Calculate the total loss across all properties.

---

### Problem 3: Average Days on Market by Property Type
Calculate the average `days_on_market` for each `property_type`. Which property type sells the fastest?

---

### Problem 4: Filter and Sort
Find all properties in "Beachfront" location with more than 3 bedrooms, sorted by `sold_price` in descending order.

---

### Problem 5: Agent Performance Analysis
Calculate the total `sold_price` for each agent. Rank agents from highest to lowest total sales.

---

### Problem 6: Percentage Discount Calculation
Create a column showing the percentage discount: `((listing_price - sold_price) / listing_price) * 100`. Find properties with discount greater than 5%.

---

### Problem 7: Property Age Calculation
Calculate the age of each property (2025 - year_built). Find the average age of properties for each property type.

---

### Problem 8: Location Statistics
Using groupby, calculate the mean, min, and max `sold_price` for each location.

---

### Problem 9: Bedroom-Bathroom Ratio
Create a column for bedroom-to-bathroom ratio. Find properties where this ratio is greater than 2.

---

### Problem 10: Monthly Sales Analysis
Extract month from `sale_date` and calculate total sales volume (sum of sold_price) for each month.

---

### Problem 11: NumPy Statistical Analysis
Using NumPy, calculate the mean, median, standard deviation, and variance of `sold_price`.

---

### Problem 12: Conditional Filtering with Multiple Criteria
Find all Condos or Townhouses that have parking_spaces >= 2 AND sold_price < 500000.

---

### Problem 13: Pivot Table Creation
Create a pivot table showing average `sold_price` for each combination of `property_type` and `location`.

---

### Problem 14: Percentile Analysis
Using NumPy, find the 25th, 50th, and 75th percentile of `area_sqft`. Categorize properties as 'Small', 'Medium', or 'Large' based on these percentiles.

---

### Problem 15: Agent Efficiency Score
Calculate an "efficiency score" for each agent: `total_sold_price / total_days_on_market`. Which agent is most efficient?

---

## Good luck! 🏠
