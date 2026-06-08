# Cinema Ticket Price System

age = int(input("Enter age: "))
group_size = int(input("Enter group size: "))

# Determine ticket price using nested if
if age >= 18:
    if age >= 60:
        price = 100
        print("Senior Citizen Ticket: ₹100")
    else:
        price = 200
        print("Adult Ticket: ₹200")
else:
    if age < 5:
        price = 0
        print("Child under 5: Free Entry")
    else:
        price = 80
        print("Child Ticket: ₹80")

# Calculate total cost
total = price * group_size

# Apply group discount
if group_size > 10:
    total = total * 0.8  # 20% discount
    print("Group Discount Applied: 20%")

print("Total Amount: ₹", total)