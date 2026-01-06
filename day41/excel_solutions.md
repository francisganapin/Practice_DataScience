# Excel Solutions for 15 Real Estate Problems

## First: Import the CSV into Excel
1. Open Excel → Data tab → From Text/CSV → Select `real_estate_data.csv`

---

## Problem 1: Price Per Square Foot
**Excel Formula (in column O, assuming headers in row 1):**
```
=G2/F2
```
Then copy down for all rows.

**Top 5:** Sort column O descending → Select first 5 rows.

---

## Problem 2: Profit/Loss Calculation
**Excel Formula (in column O):**
```
=G2-H2
```
**Total Loss:**
```
=SUM(O:O)
```

---

## Problem 3: Average Days on Market by Property Type
**Using AVERAGEIF:**
```
=AVERAGEIF(B:B,"Single Family",I:I)
=AVERAGEIF(B:B,"Condo",I:I)
=AVERAGEIF(B:B,"Townhouse",I:I)
```

---

## Problem 4: Filter Beachfront with >3 Bedrooms
1. Select all data
2. Data → Filter
3. Filter Location = "Beachfront"
4. Filter Bedrooms > 3
5. Sort by Sold_Price (Largest to Smallest)

---

## Problem 5: Agent Performance (Total Sales)
**Using SUMIF:**
```
=SUMIF(J:J,"Anna Rodriguez",H:H)
=SUMIF(J:J,"Mark Thompson",H:H)
=SUMIF(J:J,"Lisa Chen",H:H)
=SUMIF(J:J,"James Wilson",H:H)
```

---

## Problem 6: Percentage Discount
**Excel Formula (in column O):**
```
=((G2-H2)/G2)*100
```
**Filter properties with discount > 5%:**
Use AutoFilter on column O and set filter >5

---

## Problem 7: Property Age
**Excel Formula (in column O):**
```
=2025-M2
```
**Average Age by Property Type:**
```
=AVERAGEIF(B:B,"Single Family",O:O)
=AVERAGEIF(B:B,"Condo",O:O)
=AVERAGEIF(B:B,"Townhouse",O:O)
```

---

## Problem 8: Location Statistics
**Mean by Location:**
```
=AVERAGEIF(C:C,"Downtown",H:H)
=AVERAGEIF(C:C,"Suburbs",H:H)
=AVERAGEIF(C:C,"Midtown",H:H)
=AVERAGEIF(C:C,"Beachfront",H:H)
```
**Min by Location:**
```
=MINIFS(H:H,C:C,"Downtown")
=MINIFS(H:H,C:C,"Suburbs")
=MINIFS(H:H,C:C,"Midtown")
=MINIFS(H:H,C:C,"Beachfront")
```
**Max by Location:**
```
=MAXIFS(H:H,C:C,"Downtown")
=MAXIFS(H:H,C:C,"Suburbs")
=MAXIFS(H:H,C:C,"Midtown")
=MAXIFS(H:H,C:C,"Beachfront")
```

---

## Problem 9: Bedroom-Bathroom Ratio
**Excel Formula (in column O):**
```
=D2/E2
```
**Filter ratio > 2:**
Apply AutoFilter on column O, condition: >2

---

## Problem 10: Monthly Sales Analysis
**Extract Month (in column O):**
```
=MONTH(K2)
```
**Sum by Month (assuming months 1-6):**
```
=SUMIF(O:O,1,H:H)
=SUMIF(O:O,2,H:H)
=SUMIF(O:O,3,H:H)
=SUMIF(O:O,4,H:H)
=SUMIF(O:O,5,H:H)
=SUMIF(O:O,6,H:H)
```

---

## Problem 11: Statistical Analysis
**Mean:**
```
=AVERAGE(H:H)
```
**Median:**
```
=MEDIAN(H:H)
```
**Standard Deviation:**
```
=STDEV(H:H)
```
**Variance:**
```
=VAR(H:H)
```

---

## Problem 12: Multiple Criteria Filter
**Using Filter Feature:**
1. Filter property_type = "Condo" OR "Townhouse"
2. Filter parking_spaces >= 2
3. Filter sold_price < 500000

**Using FILTER function (Excel 365):**
```
=FILTER(A2:N41,((B2:B41="Condo")+(B2:B41="Townhouse"))*(N2:N41>=2)*(H2:H41<500000))
```

---

## Problem 13: Pivot Table
1. Select all data
2. Insert → PivotTable
3. Rows: property_type
4. Columns: location  
5. Values: Average of sold_price

---

## Problem 14: Percentile Analysis
**Calculate Percentiles:**
```
=PERCENTILE(F:F,0.25)    // 25th percentile
=PERCENTILE(F:F,0.5)     // 50th percentile (median)
=PERCENTILE(F:F,0.75)    // 75th percentile
```

**Categorize (in column O):**
```
=IF(F2<=PERCENTILE($F$2:$F$41,0.25),"Small",IF(F2<=PERCENTILE($F$2:$F$41,0.75),"Medium","Large"))
```

---

## Problem 15: Agent Efficiency Score
**Step 1 - Total Sold Price per Agent:**
```
=SUMIF(J:J,"Anna Rodriguez",H:H)
=SUMIF(J:J,"Mark Thompson",H:H)
=SUMIF(J:J,"Lisa Chen",H:H)
=SUMIF(J:J,"James Wilson",H:H)
```

**Step 2 - Total Days on Market per Agent:**
```
=SUMIF(J:J,"Anna Rodriguez",I:I)
=SUMIF(J:J,"Mark Thompson",I:I)
=SUMIF(J:J,"Lisa Chen",I:I)
=SUMIF(J:J,"James Wilson",I:I)
```

**Step 3 - Efficiency Score:**
```
=Total_Sold_Price / Total_Days_on_Market
```

Example for Anna Rodriguez:
```
=SUMIF(J:J,"Anna Rodriguez",H:H)/SUMIF(J:J,"Anna Rodriguez",I:I)
```

---

## 📊 Bonus Tips:
- Use **Conditional Formatting** to highlight important values
- Use **Named Ranges** for cleaner formulas
- Use **XLOOKUP** for more flexible lookups (Excel 365)
