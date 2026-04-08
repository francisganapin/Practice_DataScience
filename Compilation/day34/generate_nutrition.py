import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define data
food_items = [
    'Chicken Breast', 'Salmon', 'Egg', 'Tofu', 'Lentils',
    'Brown Rice', 'Quinoa', 'Oats', 'Sweet Potato', 'Broccoli',
    'Spinach', 'Almonds', 'Walnuts', 'Greek Yogurt', 'Milk',
    'Apple', 'Banana', 'Orange', 'Blueberries', 'Avocado',
    'Beef Steak', 'Pork Chop', 'Shrimp', 'Tuna', 'Chickpeas',
    'Pasta', 'Bread', 'Cheese', 'Butter', 'Olive Oil'
]

categories = {
    'Chicken Breast': 'Meat', 'Salmon': 'Fish', 'Egg': 'Dairy/Egg', 'Tofu': 'Plant-Based', 'Lentils': 'Plant-Based',
    'Brown Rice': 'Grains', 'Quinoa': 'Grains', 'Oats': 'Grains', 'Sweet Potato': 'Vegetable', 'Broccoli': 'Vegetable',
    'Spinach': 'Vegetable', 'Almonds': 'Nut/Seed', 'Walnuts': 'Nut/Seed', 'Greek Yogurt': 'Dairy/Egg', 'Milk': 'Dairy/Egg',
    'Apple': 'Fruit', 'Banana': 'Fruit', 'Orange': 'Fruit', 'Blueberries': 'Fruit', 'Avocado': 'Fruit',
    'Beef Steak': 'Meat', 'Pork Chop': 'Meat', 'Shrimp': 'Seafood', 'Tuna': 'Seafood', 'Chickpeas': 'Plant-Based',
    'Pasta': 'Grains', 'Bread': 'Grains', 'Cheese': 'Dairy/Egg', 'Butter': 'Dairy/Egg', 'Olive Oil': 'Fat'
}

data = []

for food in food_items:
    category = categories[food]
    
    # Generate somewhat realistic values based on category (simplified)
    if category in ['Meat', 'Fish', 'Seafood']:
        calories = random.randint(100, 300)
        protein = random.uniform(20, 30)
        carbs = random.uniform(0, 5)
        fat = random.uniform(1, 15)
    elif category in ['Grains']:
        calories = random.randint(100, 400)
        protein = random.uniform(2, 10)
        carbs = random.uniform(20, 60)
        fat = random.uniform(0, 5)
    elif category in ['Vegetable']:
        calories = random.randint(20, 100)
        protein = random.uniform(1, 5)
        carbs = random.uniform(2, 15)
        fat = random.uniform(0, 1)
    elif category in ['Fruit']:
        calories = random.randint(40, 100)
        protein = random.uniform(0, 2)
        carbs = random.uniform(10, 25)
        fat = random.uniform(0, 1)
    elif category in ['Dairy/Egg']:
        calories = random.randint(50, 400)
        protein = random.uniform(3, 25)
        carbs = random.uniform(0, 15)
        fat = random.uniform(0, 30)
    elif category in ['Nut/Seed', 'Fat']:
        calories = random.randint(150, 700)
        protein = random.uniform(2, 20)
        carbs = random.uniform(2, 20)
        fat = random.uniform(15, 70)
    else: # Plant-Based protein
        calories = random.randint(100, 200)
        protein = random.uniform(8, 15)
        carbs = random.uniform(5, 20)
        fat = random.uniform(1, 10)

    data.append([
        food,
        category,
        round(calories),
        round(protein, 1),
        round(carbs, 1),
        round(fat, 1)
    ])

df = pd.DataFrame(data, columns=['Food_Item', 'Category', 'Calories', 'Protein', 'Carbohydrates', 'Fat'])

# Save to CSV
df.to_csv('nutrition.csv', index=False)
print("nutrition.csv created successfully.")
