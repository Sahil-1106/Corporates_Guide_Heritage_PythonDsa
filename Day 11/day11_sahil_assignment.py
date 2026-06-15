# ============================================================
# DAY 9 ASSIGNMENT
# Dictionaries & Sets
# ============================================================

# ============================================================
# Q1. Student Marks Dictionary
# ============================================================
print("\n" + "=" * 60)
print("Q1. Student Marks Dictionary")
print("=" * 60)

students = {
    "Rahul": 85,
    "Amit": 79,
    "Priya": 91,
    "Sneha": 76,
    "Karan": 81
}

print("Student Names:", list(students.keys()))
print("All Marks:", list(students.values()))

average_marks = sum(students.values()) / len(students)
print("Average Marks:", average_marks)


# ============================================================
# Q2. Word Frequency Counter
# ============================================================
print("\n" + "=" * 60)
print("Q2. Word Frequency Counter")
print("=" * 60)

text = "python is easy and python is powerful"

frequency = {}

for word in text.split():
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)


# ============================================================
# Q3. Employee Lookup using get()
# ============================================================
print("\n" + "=" * 60)
print("Q3. Employee Lookup using get()")
print("=" * 60)

employees = {
    "E101": "Rahul",
    "E102": "Amit",
    "E103": "Priya",
    "E104": "Sneha",
    "E105": "Karan"
}

emp_id = input("Enter Employee ID: ")

employee = employees.get(emp_id, "Employee Not Found")
print(employee)


# ============================================================
# Q4. Dictionary Inventory Management
# ============================================================
print("\n" + "=" * 60)
print("Q4. Dictionary Inventory Management")
print("=" * 60)

inventory = {
    "Laptop": 15,
    "Mouse": 50,
    "Keyboard": 30
}

print("Products:")
print(list(inventory.keys()))

print("\nQuantities:")
print(list(inventory.values()))

print("\nProduct and Quantity Pairs:")
for product, quantity in inventory.items():
    print(product, ":", quantity)


# ============================================================
# Q5. Common Subjects Between Students
# ============================================================
print("\n" + "=" * 60)
print("Q5. Common Subjects Between Students")
print("=" * 60)

student1 = {"Math", "Physics", "Chemistry", "English"}
student2 = {"Math", "Biology", "English", "History"}

common_subjects = student1.intersection(student2)
only_student1 = student1.difference(student2)
only_student2 = student2.difference(student1)

print("Common Subjects:", common_subjects)
print("Subjects only taken by Student 1:", only_student1)
print("Subjects only taken by Student 2:", only_student2)


# ============================================================
# Q6. Remove Duplicate Customer IDs
# ============================================================
print("\n" + "=" * 60)
print("Q6. Remove Duplicate Customer IDs")
print("=" * 60)

customer_ids = [101, 102, 103, 101, 104, 102, 105, 103]

unique_ids = sorted(set(customer_ids))

print("Unique Customer IDs:", unique_ids)


# ============================================================
# Q7. Library Membership Analysis
# ============================================================
print("\n" + "=" * 60)
print("Q7. Library Membership Analysis")
print("=" * 60)

library_A = {"Rahul", "Amit", "Priya", "Sneha"}
library_B = {"Priya", "Karan", "Amit", "Vikram"}

both = library_A.intersection(library_B)
either = library_A.union(library_B)
only_A = library_A.difference(library_B)

print("Members present in both libraries:", both)
print("Members present in either library:", either)
print("Members only in Library A:", only_A)


# ============================================================
# Q8. Dictionary-Based Shopping Cart
# ============================================================
print("\n" + "=" * 60)
print("Q8. Dictionary-Based Shopping Cart")
print("=" * 60)

shopping_cart = {
    "Book": 500,
    "Pen": 20,
    "Notebook": 80
}

print("Original Cart:")
print(shopping_cart)

# Add a new product
shopping_cart["Pencil"] = 10

# Update price of existing product
shopping_cart["Pen"] = 25

# Remove a product
removed_product = shopping_cart.pop("Notebook")

print("\nUpdated Cart:")
print(shopping_cart)

total_value = sum(shopping_cart.values())

print("Total Cart Value:", total_value)


# ============================================================
# Q9. Set-Based Event Registration System
# ============================================================
print("\n" + "=" * 60)
print("Q9. Set-Based Event Registration System")
print("=" * 60)

event1 = {"Aman", "Riya", "Karan", "Neha"}
event2 = {"Neha", "Riya", "Vikas", "Rohan"}

both_events = event1.intersection(event2)
exactly_one = event1.symmetric_difference(event2)
total_unique = len(event1.union(event2))

print("Attendees registered for both events:", both_events)
print("Attendees registered for exactly one event:", exactly_one)
print("Total unique attendees:", total_unique)


# ============================================================
# Q10. Choosing the Right Data Structure
# ============================================================
print("\n" + "=" * 60)
print("Q10. Choosing the Right Data Structure")
print("=" * 60)

# Dictionary:
# Used for storing student details because each student ID
# maps to a student's information.

student_details = {
    101: {"Name": "Rahul", "Course": "Python"},
    102: {"Name": "Priya", "Course": "Java"},
    103: {"Name": "Amit", "Course": "C++"}
}

# Set:
# Used for course categories because categories must be unique.

course_categories = {
    "Programming",
    "Data Science",
    "Web Development",
    "Machine Learning"
}

# Dictionary:
# Used for course ratings because each course name
# can be mapped to its rating.

course_ratings = {
    "Python": 4.8,
    "Java": 4.5,
    "C++": 4.6,
    "Machine Learning": 4.9
}

print("Student Details:")
print(student_details)

print("\nUnique Course Categories:")
print(course_categories)

print("\nCourse Ratings:")
print(course_ratings)