# Day 8 Assignment
# Name: Sahil Manzoor
# File Name: day8_sahil_assignment.py

# ==========================================================
# Question 1 - List Creation & Basic Operations
# ==========================================================

print("\n===== Question 1 =====")

student_marks = [45, 67, 89, 76, 54, 91, 73, 82, 100, 60]

print("First 3 elements:", student_marks[:3])
print("Last 3 elements:", student_marks[-3:])
print("Every alternate element:", student_marks[::2])
print("Total number of elements:", len(student_marks))

student_marks[4] = 95
print("Updated list:", student_marks)

print("Reversed list:", student_marks[::-1])

# ==========================================================
# Question 2 - List Methods
# ==========================================================

print("\n===== Question 2 =====")

scores = [55, 72, 88, 43, 91, 67, 55, 76]

original_count = scores.count(55)

scores.append(80)
print("After append:", scores)

scores.insert(3, 100)
print("After insert:", scores)

scores.remove(55)
print("After removing first 55:", scores)

print("Ascending:", sorted(scores))
print("Descending:", sorted(scores, reverse=True))

print("Count of 55 originally:", original_count)
print("Index of 88:", scores.index(88))

popped = scores.pop()
print("Popped value:", popped)
print("Remaining list:", scores)

# ==========================================================
# Question 3 - List Comprehension
# ==========================================================

print("\n===== Question 3 =====")

squares = [x**2 for x in range(1, 16)]
print("Squares:", squares)

evens = [x for x in range(1, 51) if x % 2 == 0]
print("Even numbers:", evens)

words = ['hello', 'world', 'python', 'is', 'great']
long_words = [word for word in words if len(word) > 4]
print("Long words:", long_words)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
flattened = [item for row in matrix for item in row]
print("Flattened matrix:", flattened)

tuples_list = [(x, x**2) for x in range(1, 9)]
print("Number-square tuples:", tuples_list)

# ==========================================================
# Question 4 - Tuple Creation & Immutability
# ==========================================================

print("\n===== Question 4 =====")

months = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

print("3rd month:", months[2])
print("Last month:", months[-1])
print("Months index 3 to 6:", months[3:7])

try:
    months[0] = "January_New"
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable.")

name_tuple = ("Sahil",)
print("Single element tuple:", name_tuple)
print("Type:", type(name_tuple))

months_list = list(months)
months_list.append("Intercalary")
months = tuple(months_list)
print("Updated tuple:", months)

# ==========================================================
# Question 5 - Tuple Unpacking & Swapping
# ==========================================================

print("\n===== Question 5 =====")

employee = ('Rajesh Kumar', 34, 'Data Analyst', 75000, 'Bangalore')

name, age, designation, salary, city = employee

print("Name:", name)
print("Age:", age)
print("Designation:", designation)
print("Salary:", salary)
print("City:", city)

sample = ("Rajesh", "Kumar", 34, "Data Analyst", 75000, "Bangalore")

first_name, *middle_items, second_last, last_item = sample

print("First Name:", first_name)
print("Middle Items:", middle_items)
print("Last Two Items:", second_last, last_item)

x, y, z = 10, 20, 30
x, y, z = z, x, y

print("After swapping:", x, y, z)

data = [('Alice',90), ('Bob',85), ('Charlie',78), ('Diana',92)]

for student, score in data:
    print(f"{student} scored {score}/100")

def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([12, 45, 78, 3, 99, 21])

print("Minimum:", minimum)
print("Maximum:", maximum)

# ==========================================================
# Question 6 - Loops with Lists & Tuples
# ==========================================================

print("\n===== Question 6 =====")

temperatures = [22, 35, 18, 40, 28, 15, 33, 27]

for index, temp in enumerate(temperatures):
    print(f"Index {index}: {temp}")

count = 0
for temp in temperatures:
    if temp > 30:
        count += 1

print("Temperatures above 30:", count)

names = ['Alice', 'Bob', 'Charlie']
marks = [85, 92, 78]

for name, mark in zip(names, marks):
    print(f"{name}: {mark}")

temps_copy = temperatures.copy()

while any(temp <= 25 for temp in temps_copy):
    for temp in temps_copy:
        if temp <= 25:
            temps_copy.remove(temp)
            print("After removal:", temps_copy)
            break

print("Remaining temperatures:", temps_copy)

print("\nMultiplication Table (1 to 5)")

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()

# ==========================================================
# Challenge 1 - Student Grade System
# ==========================================================

print("\n===== Challenge 1 =====")

students = [
    ("Alice",101,[80,85,90,75,88]),
    ("Bob",102,[70,65,75,80,72]),
    ("Charlie",103,[95,92,96,94,90]),
    ("Diana",104,[60,62,58,65,70]),
    ("Ethan",105,[88,85,87,90,89]),
    ("Fiona",106,[76,74,78,80,77]),
    ("George",107,[55,60,58,62,59]),
    ("Helen",108,[91,93,89,90,92]),
    ("Ian",109,[68,70,72,65,69]),
    ("Julia",110,[84,82,86,88,85])
]

def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

averages = [(student[0], calculate_average(student[2])) for student in students]

ranked = sorted(averages, key=lambda x: x[1], reverse=True)

print("\nClass Rank")
for rank, (name, avg) in enumerate(ranked, start=1):
    print(f"{rank}. {name} - {avg:.2f}")

above_75 = sum(1 for _, avg in ranked if avg > 75)
print("Students above 75 average:", above_75)

print("Topper:", ranked[0])
print("Lowest Average:", ranked[-1])

# ==========================================================
# Challenge 2 - Inventory Management
# ==========================================================

print("\n===== Challenge 2 =====")

inventory = [
    (101,"Laptop",50000,8),
    (102,"Mouse",500,3),
    (103,"Keyboard",1500,4),
    (104,"Monitor",12000,6),
    (105,"Printer",8000,2),
    (106,"Speaker",2500,10),
    (107,"Router",3000,1),
    (108,"Webcam",2000,7)
]

def add_product(product):
    inventory.append(product)

def remove_product(name):
    global inventory
    inventory[:] = [item for item in inventory if item[1] != name]

def update_quantity(name, qty):
    for i, item in enumerate(inventory):
        if item[1] == name:
            inventory[i] = (item[0], item[1], item[2], qty)

def total_inventory_value():
    return sum(price * quantity for _, _, price, quantity in inventory)

print("Total Inventory Value:", total_inventory_value())

print("\nLow Stock Alert")
for product in inventory:
    if product[3] < 5:
        print(product)

print("\nProducts Sorted by Price")
sorted_products = sorted(inventory, key=lambda x: x[2])

for product in sorted_products:
    print(product)

search_name = "Router"

for product in inventory:
    if product[1].lower() == search_name.lower():
        print("\nProduct Found:")
        print(product)
        break
else:
    print("Product not found")
