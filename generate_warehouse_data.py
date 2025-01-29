import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


def generate_warehouse_data(num_products=100):
    # Product categories and their subcategories
    categories = {
        'Electronics': ['Smartphones', 'Laptops', 'Tablets', 'Accessories'],
        'Furniture': ['Chairs', 'Tables', 'Storage', 'Beds'],
        'Clothing': ['Shirts', 'Pants', 'Dresses', 'Outerwear'],
        'Tools': ['Power Tools', 'Hand Tools', 'Garden Tools', 'Safety Equipment']
    }

    # Warehouse zones and their aisles
    zones = ['A', 'B', 'C', 'D']

    # Lists to store data
    data = []

    # Generate product IDs
    product_ids = [f'PRD{str(i).zfill(6)}' for i in range(num_products)]

    for pid in product_ids:
        # Select random category and subcategory
        category = random.choice(list(categories.keys()))
        subcategory = random.choice(categories[category])

        # Generate location
        zone = random.choice(zones)
        aisle = random.randint(1, 20)
        shelf = random.randint(1, 5)
        bin_number = random.randint(1, 10)
        location = f"{zone}-{aisle:02d}-{shelf}-{bin_number:02d}"

        # Generate specifications based on category
        if category == 'Electronics':
            specs = {
                'weight': f"{random.uniform(0.2, 5.0):.2f} kg",
                'dimensions': f"{random.randint(5, 50)}x{random.randint(5, 50)}x{random.randint(2, 20)} cm",
                'power': f"{random.choice([5, 9, 12, 24, 48])}V",
                'warranty': f"{random.choice([12, 24, 36])} months"
            }
        elif category == 'Furniture':
            specs = {
                'weight': f"{random.uniform(5.0, 100.0):.2f} kg",
                'dimensions': f"{random.randint(30, 200)}x{random.randint(30, 200)}x{random.randint(30, 200)} cm",
                'material': random.choice(['Wood', 'Metal', 'Plastic', 'Glass']),
                'assembly_required': random.choice(['Yes', 'No'])
            }
        elif category == 'Clothing':
            specs = {
                'size': random.choice(['S', 'M', 'L', 'XL', 'XXL']),
                'color': random.choice(['Black', 'White', 'Blue', 'Red', 'Green']),
                'material': random.choice(['Cotton', 'Polyester', 'Wool', 'Blend']),
                'care': random.choice(['Machine wash', 'Dry clean', 'Hand wash'])
            }
        else:  # Tools
            specs = {
                'weight': f"{random.uniform(0.5, 20.0):.2f} kg",
                'material': random.choice(['Steel', 'Aluminum', 'Plastic', 'Carbon Fiber']),
                'warranty': f"{random.choice([12, 24, 36, 60])} months",
                'safety_rating': random.choice(['Basic', 'Professional', 'Industrial'])
            }

        # Generate stock and price information
        current_stock = random.randint(0, 200)
        min_stock = random.randint(10, 50)
        max_stock = random.randint(100, 300)
        unit_price = round(random.uniform(10.0, 1000.0), 2)

        # Generate last restock date
        last_restock = datetime.now() - timedelta(days=random.randint(0, 90))

        # Create record
        record = {
            'Product_ID': pid,
            'Category': category,
            'Subcategory': subcategory,
            'Location': location,
            'Current_Stock': current_stock,
            'Min_Stock_Level': min_stock,
            'Max_Stock_Level': max_stock,
            'Unit_Price': unit_price,
            'Last_Restock_Date': last_restock.strftime('%Y-%m-%d'),
            'Specifications': str(specs)
        }

        data.append(record)

    # Convert to DataFrame
    df = pd.DataFrame(data)
    return df


def save_to_excel(df, filename='warehouse_inventory.xlsx'):
    # Create Excel writer object
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        # Write main data
        df.to_excel(writer, sheet_name='Inventory', index=False)

        # Create summary sheet
        summary = pd.DataFrame({
            'Category': df.groupby('Category')['Current_Stock'].sum().index,
            'Total_Items': df.groupby('Category')['Current_Stock'].sum().values,
            'Average_Price': df.groupby('Category')['Unit_Price'].mean().round(2).values,
            'Distinct_Products': df.groupby('Category').size().values
        })
        summary.to_excel(writer, sheet_name='Summary', index=False)

        # Create low stock alerts sheet
        low_stock = df[df['Current_Stock'] <= df['Min_Stock_Level']]
        if not low_stock.empty:
            low_stock.to_excel(writer, sheet_name='Low_Stock_Alerts', index=False)


if __name__ == "__main__":
    # Generate data
    print("Generating warehouse inventory data...")
    df = generate_warehouse_data(num_products=100)

    # Save to Excel
    filename = 'warehouse_inventory.xlsx'
    save_to_excel(df, filename)
    print(f"Data saved to {filename}")

    # Print some sample statistics
    print("\nQuick Statistics:")
    print(f"Total number of products: {len(df)}")
    print(f"Products by category:\n{df['Category'].value_counts()}")
    print(f"\nTotal inventory value: ${(df['Current_Stock'] * df['Unit_Price']).sum():,.2f}")
    print(f"Low stock items: {len(df[df['Current_Stock'] <= df['Min_Stock_Level']])}")