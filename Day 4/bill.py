product_name = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per unit: "))

total_cost = quantity * price
gst = total_cost * 0.18
final_bill = total_cost + gst

print(f"Product Name : {product_name}")
print(f"Quantity     : {quantity}")
print(f"Price        : ₹{price}")
print(f"Total Cost   : ₹{total_cost}")
print(f"GST (18%)    : ₹{gst}")
print(f"Final Bill   : ₹{final_bill}")