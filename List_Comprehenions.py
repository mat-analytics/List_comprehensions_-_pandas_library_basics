products = ['coffee', 'tea', 'sugar', 'cookies']
netto_sales = [500, 200, 100, 450]

#counting gross value of sales
gross_sales = [i*1.23 for i in netto_sales]

#showing values >300 from gross_sales
high_sales = [i for i in gross_sales if i>300]

#printing
print(f"List of gross sales: {gross_sales}")
print(f"Values >300 from gross sales: {high_sales}")