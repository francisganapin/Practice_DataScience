import pandas as pd

data = {
    'Date': pd.date_range(start='2025-06-01', periods=500, freq='D').astype(str),
    'Product': ['Laptop', 'Smartphone', 'Tablet'] * (500 // 3) + ['Laptop'] * (500 % 3),
    'Units_Sold': [5, 10, 3, 7, 8, 2, 6, 12, 4, 9] * 50,
    'Unit_Price': [1000, 700, 400, 1000, 700, 400, 1000, 700, 400, 1000] * 50
}

