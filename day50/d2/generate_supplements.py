import csv
import random

def generate_data():
    categories = [
        "Protein", "Vitamins", "Minerals", "Herbal", 
        "Pre-workout", "Post-workout", "Weight Management", "Energy", "Joint Support", "Digestive Health"
    ]
    
    brands = [
        "Optimum Nutrition", "MuscleTech", "BSN", "Dymatize", "Now Foods", 
        "Garden of Life", "Cellucor", "JYM Supplement Science", "MyProtein", "Universal Nutrition"
    ]
    
    product_types = {
        "Protein": ["Whey Protein Isolate", "Casein Protein", "Plant Protein Blend", "Mass Gainer"],
        "Vitamins": ["Multivitamin Men", "Multivitamin Women", "Vitamin C 1000mg", "Vitamin D3 5000IU", "B-Complex"],
        "Minerals": ["Magnesium Glycinate", "Zinc Picolinate", "Calcium Citrate", "Iron Complex"],
        "Herbal": ["Ashwagandha Root", "Turmeric Curcumin", "Ginkgo Biloba", "Milk Thistle"],
        "Pre-workout": ["Pre-Workout Powder Fruit Punch", "Beta-Alanine", "Caffeine Pills", "Nitric Oxide Booster"],
        "Post-workout": ["BCAA Powder", "Glutamine", "Creatine Monohydrate", "Recovery Blend"],
        "Weight Management": ["Fat Burner Thermogenic", "L-Carnitine Liquid", "CLA Softgels", "Green Tea Extract"],
        "Energy": ["Energy Gel", "Electrolyte Powder", "Energy Bar"],
        "Joint Support": ["Glucosamine Chondroitin", "Collagen Peptides", "MSM Powder"],
        "Digestive Health": ["Probiotic 50 Billion", "Digestive Enzymes", "Fiber Powder"]
    }

    data = []
    
    for i in range(1, 101):
        category = random.choice(categories)
        brand = random.choice(brands)
        product_name = f"{brand} {random.choice(product_types.get(category, ['Supplement']))}"
        price = round(random.uniform(10.0, 100.0), 2)
        rating = round(random.uniform(3.0, 5.0), 1)
        stock = random.randint(0, 500)
        
        data.append([i, product_name, category, brand, price, rating, stock])

    headers = ["Product ID", "Product Name", "Category", "Brand", "Price", "Rating", "Stock Quantity"]

    with open('food_supplements.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

    print("Successfully generated food_supplements.csv with 100 entries.")

if __name__ == "__main__":
    generate_data()
