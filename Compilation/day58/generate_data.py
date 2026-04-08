import pandas as pd
import numpy as np
import random
import os

# Set seed for reproducibility
np.random.seed(42)

# Generate 500 rows of data
n_samples = 500

# Features
square_feet = np.random.normal(2000, 500, n_samples).astype(int)
square_feet = np.clip(square_feet, 500, 5000)

bedrooms = np.random.randint(1, 6, n_samples)
bathrooms = np.random.randint(1, 4, n_samples)
age = np.random.randint(0, 50, n_samples)
location_score = np.random.randint(1, 11, n_samples) # 1 to 10
has_garage = np.random.randint(0, 2, n_samples) # 0 or 1

# Calculate Price based on a formula + some noise
price = (
    50000 +
    (square_feet * 150) +
    (bedrooms * 10000) +
    (bathrooms * 15000) -
    (age * 1000) +
    (location_score * 10000) +
    (has_garage * 20000) +
    np.random.normal(0, 25000, n_samples)
)

# Create DataFrame
df = pd.DataFrame({
    'Square_Feet': square_feet,
    'Bedrooms': bedrooms,
    'Bathrooms': bathrooms,
    'Age': age,
    'Location_Score': location_score,
    'Has_Garage': has_garage,
    'Price': price.astype(int)
})

# Introduce some missing values for practice
df.loc[random.sample(range(n_samples), 5), 'Square_Feet'] = np.nan
df.loc[random.sample(range(n_samples), 5), 'Location_Score'] = np.nan

# Save to CSV
output_path = 'house_prices.csv'
df.to_csv(output_path, index=False)

print(f"Dataset generated at: {os.path.abspath(output_path)}")
