
with open("sales_data.csv", "w") as file:
    file.write("Product,Quantity,Revenue,Profit\n")

    

import os

folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, "makeup_sales.csv")

# Product information
product_name = "concealer"
price = 600
quantity = 10
shipping_cost = 120
selling_price = 1200

# Calculate the results
total_product_cost = price * quantity
total_cost = total_product_cost + shipping_cost
total_revenue = selling_price * quantity
profit = total_revenue - total_cost

# Save the headings and product results
with open(file_path, "w") as file:
    file.write(
        "Product,Buying Price,Quantity,Shipping,"
        "Selling Price,Revenue,Total Cost,Profit\n"
    )

    file.write(
        f"{product_name},{price},{quantity},{shipping_cost},"
        f"{selling_price},{total_revenue},{total_cost},{profit}\n"
    )

print("Product results saved successfully!")
print("Profit:", profit)
print("File location:", file_path)


import os

folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, "makeup_sales.csv")

with open(file_path, "w") as file:
    file.write(
        "Product,Buying Price,Quantity,Shipping,"
        "Selling Price,Revenue,Total Cost,Profit\n"
    )

    for i in range(3):
        # Collect product information
        product_name = input("Enter product name: ")
        price = int(input("Enter buying price: "))
        quantity = int(input("Enter quantity: "))
        shipping_cost = int(input("Enter shipping cost: "))
        selling_price = int(input("Enter selling price: "))

        # Calculate results
        total_product_cost = price * quantity
        total_cost = total_product_cost + shipping_cost
        total_revenue = selling_price * quantity
        profit = total_revenue - total_cost

        # Save this product's results
        file.write(
            f"{product_name},{price},{quantity},{shipping_cost},"
            f"{selling_price},{total_revenue},{total_cost},{profit}\n"
        )

        print("Profit for", product_name, "is", profit)

print("All product results saved!")
print("File location:", file_path)