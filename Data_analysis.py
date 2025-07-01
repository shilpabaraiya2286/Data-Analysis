#Step 1: Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt

#Step 2: Load the CSV
df = pd.read_csv('sale_data.csv')
print("First 5 rows:")
print(df.head())

#Step 3: Add a 'Total' Column
df['Total'] = df['Quantity'] * df['Price']

#Step 4: Group by Product and Sum
product_sales = df.groupby('Product')['Total'].sum()
print("\nTotal Sales by Product:")
print(product_sales)

#Step 5: Visualize Product Sales
product_sales.plot(kind='bar', title='Total Sales by Product', color='skyblue')
plt.xlabel('Product')
plt.ylabel('Sales (INR)')
plt.tight_layout()
plt.show()

#Step 6: Group by Region and Sum
region_sales = df.groupby('Region')['Total'].sum()
print("\nTotal Sales by Region:")
print(region_sales)

#Step 7: Visualize Region Sales
region_sales.plot(kind='pie', autopct='%1.1f%%', startangle=140, title='Sales by Region')
plt.ylabel('')  
plt.show()
