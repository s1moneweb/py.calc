product_name1= input("Enter product name: ")
price1= int(input("Enter product price: "))
quantity1= int(input("Enter product quantity: "))
shipping_cost1= int(input("Enter shipping cost: "))
selling_price1= int(input("Enter selling price: "))

product_name2= input("Enter product name: ")
price2= int(input("Enter product price: "))
quantity2= int(input("Enter product quantity: "))
shipping_cost2= int(input("Enter shipping cost: "))
selling_price2= int(input("Enter selling price: "))

product_name3= input("Enter product name: ")
price3= int(input("Enter product price: "))
quantity3= int(input("Enter product quantity: "))
shipping_cost3= int(input("Enter shipping cost: "))
selling_price3= int(input("Enter selling price: "))


#total product cost for product 1
total_product_cost1 = price1 * quantity1
print("Total product cost for", product_name1, "is", total_product_cost1)

#total product cost for product 2
total_product_cost2 = price2 * quantity2
print("Total product cost for", product_name2, "is", total_product_cost2)

#total product cost for product 3
total_product_cost3 = price3 * quantity3
print("Total product cost for", product_name3, "is", total_product_cost3)

#total cost of the product including shipping cost for product 1
total_cost1= total_product_cost1 + shipping_cost1
print("Total cost for", product_name1, "is", total_cost1)

#total cost of the product including shipping cost for product 2
total_cost2= total_product_cost2 + shipping_cost2
print("Total cost for", product_name2, "is", total_cost2)

#total cost of the product including shipping cost for product 3
total_cost3= total_product_cost3 + shipping_cost3
print("Total cost for", product_name3, "is", total_cost3)

#total revenue from selling the product for product 1
total_revenue1= selling_price1 * quantity1
print("Total revenue for", product_name1, "is", total_revenue1)

#total revenue from selling the product for product 2
total_revenue2= selling_price2 * quantity2
print("Total revenue for", product_name2, "is", total_revenue2)

#total revenue from selling the product for product 3
total_revenue3= selling_price3 * quantity3
print("Total revenue for", product_name3, "is", total_revenue3)

#calculate profit for product 1
profit1= total_revenue1 - total_cost1
print("Profit for", product_name1, "is", profit1)

#calculate profit for product 2
profit2= total_revenue2 - total_cost2
print("Profit for", product_name2, "is", profit2)

#calculate profit for product 3
profit3= total_revenue3 - total_cost3
print("Profit for", product_name3, "is", profit3)

#comparison operators
if profit1 > profit2 and profit1 > profit3:
    print(product_name1, "has the highest profit of", profit1)
elif profit2 > profit3:
    print(product_name2, "has the highest profit of", profit2)
else:
    print(product_name3, "has the highest profit of", profit3)

if profit1 > 2000:
    print(product_name1, "is profitable")
    
if profit2 > 2000:
    print(product_name2, "is profitable")
    
if profit3 > 2000:
    print(product_name3, "is profitable")

if profit1 > 5000:
    print("great profit! product is worth selling")

elif profit1 > 1000 and profit1 < 5000:
    print("okay product! consider selling price")  

else:
    print("not profitable! consider changing product")

if profit2 > 5000:
    print("great profit! product is worth selling")
elif profit2 > 1000 and profit2 < 5000:
    print("okay product! consider selling price")
else:
    print("not profitable! consider changing product")

if profit3 > 5000:
    print("great profit! product is worth selling")
elif profit3 > 1000 and profit3 < 5000:
    print("okay product! consider selling price")
else:
    print("not profitable! consider changing product")

for i in range(3):
    product_name= input("Enter product name: ")
    price= int(input("Enter product price: "))
    quantity= int(input("Enter product quantity: "))
    shipping_cost= int(input("Enter shipping cost: "))
    selling_price= int(input("Enter selling price: "))

    total_product_cost = price * quantity
    total_cost= total_product_cost + shipping_cost
    total_revenue= selling_price * quantity
    profit= total_revenue - total_cost

    print("Total product cost for", product_name, "is", total_product_cost)
    print("Total cost for", product_name, "is", total_cost)
    print("Total revenue for", product_name, "is", total_revenue)
    print("Profit for", product_name, "is", profit)

#logical operators
concealer_profit = 4800
concealer_revenue = 12000

blush_profit = 6880
blush_revenue = 13000

bronzer_profit = 6880
bronzer_revenue = 15000

if blush_profit > 5000 and blush_revenue > 13000:
    print("review product")
else:
    print("product meets target")

if blush_profit >= 5000 and not (blush_revenue < 13000):
    print("review product")
else:
    print("product meets target")
