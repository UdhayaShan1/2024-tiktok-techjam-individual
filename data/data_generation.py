import pandas as pd
import random

# Base data
data = [
    {'interest_area': 'cooking', 'price_preference': 'low', 'trendiness': 'mainstream', 'design_style': 'professional', 'recipient': 'yourself', 'location': 'Singapore', 'delivery_timeline': 7, 'recommended_product': 'pan'},
    {'interest_area': 'outdoor', 'price_preference': 'high', 'trendiness': 'non-mainstream', 'design_style': 'minimalist', 'recipient': 'siblings', 'location': 'USA', 'delivery_timeline': 14, 'recommended_product': 'tent'},
    {'interest_area': 'baby', 'price_preference': 'medium', 'trendiness': 'mainstream', 'design_style': 'vintage', 'recipient': 'parents', 'location': 'Canada', 'delivery_timeline': 3, 'recommended_product': 'baby stroller'},
    {'interest_area': 'automotive', 'price_preference': 'high', 'trendiness': 'mainstream', 'design_style': 'monochromatic', 'recipient': 'spouse', 'location': 'UK', 'delivery_timeline': 5, 'recommended_product': 'car polish'},
    {'interest_area': 'apparel', 'price_preference': 'low', 'trendiness': 'non-mainstream', 'design_style': 'universal', 'recipient': 'friends', 'location': 'Australia', 'delivery_timeline': 7, 'recommended_product': 't-shirt'},
    {'interest_area': 'plush', 'price_preference': 'medium', 'trendiness': 'non-mainstream', 'design_style': 'caricature', 'recipient': 'colleagues', 'location': 'India', 'delivery_timeline': 4, 'recommended_product': 'teddy bear'},
    {'interest_area': 'toys', 'price_preference': 'high', 'trendiness': 'mainstream', 'design_style': 'Chinese', 'recipient': 'children', 'location': 'China', 'delivery_timeline': 14, 'recommended_product': 'lego set'},
    {'interest_area': 'pet-friendly', 'price_preference': 'low', 'trendiness': 'non-mainstream', 'design_style': 'Western', 'recipient': 'pets', 'location': 'Germany', 'delivery_timeline': 7, 'recommended_product': 'dog food'},
    {'interest_area': 'kitchen', 'price_preference': 'medium', 'trendiness': 'mainstream', 'design_style': 'Asian', 'recipient': 'neighbors', 'location': 'Japan', 'delivery_timeline': 5, 'recommended_product': 'blender'},
    {'interest_area': 'dancing', 'price_preference': 'high', 'trendiness': 'mainstream', 'design_style': 'cute', 'recipient': 'classmates', 'location': 'France', 'delivery_timeline': 7, 'recommended_product': 'dancing shoes'}
]

# Define logical products for each interest area
logical_products = {
    'cooking': ['pan', 'knife set', 'blender', 'frying pan', 'spatula', 'cutting board'],
    'outdoor': ['tent', 'camping stove', 'lantern', 'backpack'],
    'baby': ['baby stroller', 'baby monitor', 'baby bottle', 'baby swing', 'baby walker', 'baby crib'],
    'automotive': ['car polish', 'tire cleaner', 'car wax', 'car vacuum', 'car seat cover'],
    'apparel': ['t-shirt', 'jeans', 'hoodie', 'dress', 'jacket', 'shirt'],
    'plush': ['teddy bear', 'plush elephant', 'plush panda', 'plush lion', 'plush tiger', 'plush bear'],
    'toys': ['lego set', 'action figure', 'board game', 'puzzle', 'robot toy', 'toy truck'],
    'pet-friendly': ['dog food', 'cat food', 'bird food', 'fish food', 'rabbit food', 'dog leash'],
    'kitchen': ['blender', 'food processor', 'microwave', 'rice cooker', 'coffee maker', 'kettle'],
    'dancing': ['dancing shoes', 'tap shoes', 'ballet slippers', 'jazz shoes', 'salsa shoes']
}

# Generate additional logical data
extended_data = []

for _ in range(100):  # Adjusted to reach approximately 1000 rows
    for item in data:
        new_item = item.copy()
        new_item['location'] = random.choice(['Singapore', 'USA', 'Canada', 'UK', 'Australia', 'India', 'China', 'Germany', 'Japan', 'France'])
        new_item['delivery_timeline'] = random.choice([3, 5, 7, 10, 14])
        new_item['recommended_product'] = random.choice(logical_products[item['interest_area']])
        extended_data.append(new_item)

# Create DataFrame and save to CSV
df = pd.DataFrame(extended_data)
df.to_csv('data/large_logical_dataset.csv', index=False)