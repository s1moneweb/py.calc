product_name= "concealer"
price= 600
shipping_cost= 1200
quantity= 10
selling_price= 1200

#calculate total product cost
total_product_cost = price * quantity 
print(total_product_cost) 

#total cost of the product including shipping cost
total_cost= total_product_cost + shipping_cost
print("total_cost is", total_cost)

#total revenue from selling the product
total_revenue= selling_price * quantity
print("total_revenue is", total_revenue)

#calculate profit
profit= total_revenue - total_cost 
print("profit is", profit) 




