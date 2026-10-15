product_list = ["concealer", "blush", "bronzer","lipgloss", "foundation"]
product_list.append ("setting powder")
print(product_list)

product_list.insert(2,"mascara")
print(product_list)

print("The product list contains", len(product_list), "products")

for product in product_list:
    print(product)

new_product= input("Enter new product: ")
product_list.append(new_product)
print(product_list)

new_product= input("Enter new product: ")
product_list.insert(3,new_product)
print(product_list)

for product in product_list:
    print(product)
print("The product list contains", len(product_list), "products")