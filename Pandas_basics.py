import pandas as pd

df_coffee_shop = pd.DataFrame({
    'product': ['coffee', 'tea', 'sugar', 'cookies'],
    'netto_sales': [500, 200, 100, 450]
})

#creating new column with gross sales values
df_coffee_shop['gross_sales'] = df_coffee_shop['netto_sales'] * 1.23

#creating new column with sum of gross sales values
gross_sales_summary = df_coffee_shop['gross_sales'].sum()
print(f"Total gross sales equals: {gross_sales_summary}")
