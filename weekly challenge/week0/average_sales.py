# Combine what you’ve learned:
#     - Create a `.csv` with dummy sales data
#     - Write a Python script to read it, clean it, and output total 
#       sales per customer
# Push the `.csv`, the script, and the output file to GitHub

# given that the data I'm choosing to use doesn't have a customer ID
# as an unique identifier, I'm going to assume every customer name from
# the same postal code is one individual

import csv

with open("salesdata.csv", 'r') as sales_data:
    lines = csv.reader(sales_data)
    total_orders, total_customers = 0, 0
    sales_dict = {}
    
    for line in lines:
        total_orders += 1
        key = line[4] + " " + line[7]
        if key in sales_dict:
            total_customers += 1
        sales_dict[key] = sales_dict.get(key, 0) + 1

    if (total_customers > 0):
        print ("Sales per customer = {:.2f}".format(total_orders / total_customers))
    else:
        print ("Sales per customer = 0")