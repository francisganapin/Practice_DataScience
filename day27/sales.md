# Advanced Sales Analysis - Homework & Quiz

**Instructions**:
1.  Open your `sales.ipynb` Jupyter Notebook.
2.  Run the cells to generate the data and perform the initial analysis.
3.  Use the notebook to answer the questions below.

---

## Part 1: Conceptual Quiz
*Answer these to test your understanding of the concepts.*

**Q1. The Pareto Principle (80/20 Rule) in sales typically suggests that:**
- [ ] A. 80% of your sales come from 20% of your customers or products.
- [ ] B. You should spend 80% of your time on 20% of your data.
- [ ] C. 80% of products are returned.

**Q2. In RFM Analysis, what does the 'R' stand for and why is it important?**
- [ ] A. **Revenue**: How much money they made.
- [ ] B. **Recency**: How recently they purchased (active customers are more likely to buy again).
- [ ] C. **Retention**: How long they have been a customer.

**Q3. Why do we use a "Rolling Average" (e.g., 30-day rolling mean) in time series charts?**
- [ ] A. To calculate the total sum of sales.
- [ ] B. To hide the data points.
- [ ] C. To smooth out daily volatility/noise and visualize the underlying trend.

---

## Part 2: Practical Coding Exercises
*Write code in your notebook to find the answers.*

**Exercise 1: Data Manipulation**
-   **Task**: In the `generate_sales_data` function, change the `num_orders` from `1000` to `5000`.
-   **Question**: Re-run the dataframe generation. What is the new total revenue (sum of `Total Sales`)?

**Exercise 2: Category Analysis**
-   **Task**: Group by `Category` and calculate the *average* price (`Price`) per category.
-   **Question**: Which category has the highest average price?

**Exercise 3: Time Series Deep Dive**
-   **Task**: Resample the time series data to **Weekly** (`'W'`) frequency instead of Daily.
-   **Question**: Plot the weekly sales. Do you see a clearer pattern compared to the daily plot?

**Exercise 4: Identifying "Whales" (Pareto)**
-   **Task**: Perform a Pareto analysis on **Customers** (instead of Products).
-   **Question**: How many individual customers account for the top 50% of the total revenue?

**Exercise 5: RFM Segmentation**
-   **Task**: Filter your RFM dataframe to find customers with an `RFM_Score` of **12** (Best Score: 444).
-   **Question**: List the `CustomerID`s of your absolute best customers.

---

## Part 3: Advanced Challenge
**Heatmap Visualization**
-   Create a Pivot Table with `DayOfWeek` as the index and `Hour` (0-23) as the columns.
-   The values should be the count of orders.
-   Use `sns.heatmap()` to visualize when the most orders are placed during the week.
