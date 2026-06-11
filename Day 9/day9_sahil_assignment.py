# ===== Question 1 =====
print("\n===== Question 1 =====")
# a) Create a dictionary called 'student'
student = {
    "name": "Sahil",
    "age": 21,
    "course": "B.Tech CSE",
    "city": "Kolkata",
    "gpa": 8.5
}

print("Initial Dictionary:")
print(student)

# b) Access and print each value using [] and get()

print("\nUsing [] notation:")
print(student["name"])
print(student["age"])
print(student["course"])
print(student["city"])
print(student["gpa"])

print("\nUsing get() method:")
print(student.get("name"))
print(student.get("age"))
print(student.get("course"))
print(student.get("city"))
print(student.get("gpa"))

# c) Add email and phone

student["email"] = "sahil@example.com"
student["phone"] = "9876543210"

print("\nAfter adding email and phone:")
print(student)

# d) Update GPA and delete city

student["gpa"] = 8.9
del student["city"]

print("\nAfter updating GPA and deleting city:")
print(student)

# e) Check keys using in

print("\nKey Checks:")
print("name" in student)
print("address" in student)

# f) Total key-value pairs

print("\nTotal key-value pairs:")
print(len(student))














# ===== Question 2 =====
print("\n===== Question 2 =====")

inventory = {
    'apple': 50,
    'banana': 30,
    'mango': 0,
    'cherry': 15,
    'grape': 0
}

print("Inventory:")
print(inventory)

# a) Print all product names using keys()

print("\nProduct Names:")
print(list(inventory.keys()))

# b) Print all quantities using values()

print("\nQuantities:")
print(list(inventory.values()))

# c) Print items using items()

print("\nInventory Details:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity} units")

# d) Check quantity of papaya safely

print("\nPapaya Quantity:")
print(inventory.get("papaya", "Not available"))

# e) Remove mango and print popped value

removed = inventory.pop("mango")
print("\nRemoved Item Quantity:")
print(removed)

print("Inventory After Removing Mango:")
print(inventory)

# f) Add 3 new products using update()

inventory.update({
    "orange": 20,
    "kiwi": 12,
    "pear": 18
})

print("\nInventory After Update:")
print(inventory)

# g) Add watermelon only if it doesn't exist

inventory.setdefault("watermelon", 25)

print("\nInventory After setdefault():")
print(inventory)

# h) Print out-of-stock items

print("\nOut of Stock Products:")
for product, quantity in inventory.items():
    if quantity == 0:
        print(f"{product}: {quantity} units")
        
















# ===== Question 3 =====

print("\n===== Question 3 =====")

# a) Create phonebook with at least 8 contacts

phonebook = {
    "Aman": {
        "phone": "9876543210",
        "email": "aman@gmail.com",
        "city": "Kolkata"
    },
    "Riya": {
        "phone": "9876543211",
        "email": "riya@gmail.com",
        "city": "Delhi"
    },
    "Rahul": {
        "phone": "9876543212",
        "email": "rahul@gmail.com",
        "city": "Mumbai"
    },
    "Neha": {
        "phone": "9876543213",
        "email": "neha@gmail.com",
        "city": "Pune"
    },
    "Arjun": {
        "phone": "9876543214",
        "email": "arjun@gmail.com",
        "city": "Kolkata"
    },
    "Priya": {
        "phone": "9876543215",
        "email": "priya@gmail.com",
        "city": "Chennai"
    },
    "Ishita": {
        "phone": "9876543216",
        "email": "ishita@gmail.com",
        "city": "Delhi"
    },
    "Karan": {
        "phone": "9876543217",
        "email": "karan@gmail.com",
        "city": "Bangalore"
    }
}

# b) Search Contact

def search_contact(name):
    if name in phonebook:
        print(f"\n{name} Details:")
        print(phonebook[name])
    else:
        print("Contact not found")


# c) Add Contact

def add_contact(name, phone, email, city):
    phonebook[name] = {
        "phone": phone,
        "email": email,
        "city": city
    }
    print(f"{name} added successfully")


# d) Delete Contact

def delete_contact(name):
    if name in phonebook:
        phonebook.pop(name)
        print(f"{name} deleted successfully")
    else:
        print("Contact not found")


# e) Contacts in a specific city

def contacts_in_city(city):
    result = []

    for name, details in phonebook.items():
        if details["city"].lower() == city.lower():
            result.append(name)

    return result


# f) Display all contacts

def display_all():
    print("\nAll Contacts:")

    for name, details in phonebook.items():
        print(f"""
Name : {name}
Phone: {details['phone']}
Email: {details['email']}
City : {details['city']}
-------------------------
""")


# g) Testing all functions (minimum 3 calls each)

print("\n--- Testing search_contact() ---")
search_contact("Aman")
search_contact("Riya")
search_contact("Unknown")

print("\n--- Testing add_contact() ---")
add_contact("Zoya", "9999999999", "zoya@gmail.com", "Delhi")
add_contact("Meera", "8888888888", "meera@gmail.com", "Kolkata")
add_contact("Dev", "7777777777", "dev@gmail.com", "Mumbai")

print("\n--- Testing delete_contact() ---")
delete_contact("Dev")
delete_contact("Meera")
delete_contact("Unknown")

print("\n--- Testing contacts_in_city() ---")
print(contacts_in_city("Kolkata"))
print(contacts_in_city("Delhi"))
print(contacts_in_city("Mumbai"))

print("\n--- Testing display_all() ---")
display_all()
























# ===== Question 4 =====

print("\n===== Question 4 =====")

import string

# a) Given paragraph
text = """
Python is a high-level programming language. Python is easy to learn and easy to use.
Python is used for web development, data science, and automation.
"""

# b) Convert to lowercase and remove punctuation
text = text.lower()

for char in string.punctuation:
    text = text.replace(char, "")

print("\nCleaned Text:")
print(text)

# c) Count word frequency using dictionary and get()

word_frequency = {}

words = text.split()

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

print("\nWord Frequencies:")
for word, count in word_frequency.items():
    print(f"{word}: {count}")

# d) Print top 5 most frequent words

print("\nTop 5 Most Frequent Words:")

top_words = sorted(
    word_frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

for word, count in top_words[:5]:
    print(f"{word}: {count}")

# e) Print words appearing exactly once

print("\nWords Appearing Exactly Once:")

for word, count in word_frequency.items():
    if count == 1:
        print(word)

# f) Dictionary comprehension for words appearing 2+ times

filtered_dict = {
    word: count
    for word, count in word_frequency.items()
    if count >= 2
}

print("\nWords Appearing 2+ Times:")
print(filtered_dict)






















# ===== Question 5 =====

print("\n===== Question 5 =====")

# a) Create sets A and B

A = {2, 4, 6, 8, 10, 12}
B = {3, 6, 9, 12, 15}

print("Set A:", A)
print("Set B:", B)

# b) Set Operations

print("\nUnion:")
print(A.union(B))

print("\nIntersection:")
print(A.intersection(B))

print("\nDifference (A - B):")
print(A.difference(B))

print("\nDifference (B - A):")
print(B.difference(A))

print("\nSymmetric Difference:")
print(A.symmetric_difference(B))

# c) Subset, Superset, Disjoint Checks

print("\nSubset Check:")
print("Is A a subset of B?", A.issubset(B))

print("\nSuperset Check:")
print("Is B a superset of A?", B.issuperset(A))

print("\nDisjoint Check:")
print("Are A and B disjoint?", A.isdisjoint(B))

# d) Add and Remove Elements

A.add(14)
print("\nA after adding 14:")
print(A)

B.discard(3)
print("\nB after removing 3:")
print(B)

# e) Remove duplicates from list using set

nums = [5, 1, 3, 5, 2, 1, 4, 3, 5, 2, 6]

unique_nums = set(nums)

print("\nOriginal List:")
print(nums)

print("\nUnique Values:")
print(unique_nums)

# f) Create a frozenset

frozen_A = frozenset(A)

print("\nFrozen Set:")
print(frozen_A)

print("\nTrying to modify frozenset:")

try:
    frozen_A.add(100)
except AttributeError as e:
    print("Error:", e)
    
    
    
    
    
    
    
    
    
    
    











# ===== Question 6 =====

print("\n===== Question 6 =====")

import string

# a) Define two paragraphs

paragraph1 = """
Python is a popular programming language. It is widely used for web development,
data analysis, automation, and machine learning. Python has a simple syntax and
a large community of developers.
"""

paragraph2 = """
Machine learning and data science often use Python. Python provides many useful
libraries for automation and analysis. Developers enjoy Python because it is
easy to learn and powerful.
"""

# b) Function to tokenize text and return unique lowercase words

def tokenize(text):
    text = text.lower()

    for char in string.punctuation:
        text = text.replace(char, "")

    return set(text.split())

# Create sets of unique words

words1 = tokenize(paragraph1)
words2 = tokenize(paragraph2)

print("\nUnique Words in Paragraph 1:")
print(words1)

print("\nUnique Words in Paragraph 2:")
print(words2)

# c) Set Operations

print("\nWords Appearing in BOTH Paragraphs:")
print(words1.intersection(words2))

print("\nWords ONLY in Paragraph 1:")
print(words1.difference(words2))

print("\nWords ONLY in Paragraph 2:")
print(words2.difference(words1))

print("\nAll Unique Words Across Both Paragraphs:")
print(words1.union(words2))

print("\nWords in One Paragraph but Not the Other:")
print(words1.symmetric_difference(words2))

# d) Function to find common letters between two words

def common_letters(word1, word2):
    return set(word1.lower()).intersection(set(word2.lower()))

print("\nCommon Letters Examples:")

print("python & programming:")
print(common_letters("python", "programming"))

print("data & database:")
print(common_letters("data", "database"))

print("science & machine:")
print(common_letters("science", "machine"))

# e) Find the 5 most common words across both paragraphs

combined_text = paragraph1 + " " + paragraph2

combined_text = combined_text.lower()

for char in string.punctuation:
    combined_text = combined_text.replace(char, "")

frequency = {}

for word in combined_text.split():
    frequency[word] = frequency.get(word, 0) + 1

top_5 = sorted(
    frequency.items(),
    key=lambda item: item[1],
    reverse=True
)[:5]

print("\nTop 5 Most Common Words:")

for word, count in top_5:
    print(f"{word}: {count}")
    
    






















# ===== Question 7 =====

print("\n===== Question 7 =====")

# a) Storing the 7 days of the week (should not be modified)

print("\na)")
print("Data Structure: Tuple")
print("Reason: Days of the week have a fixed order and should not be modified.")

# b) Keeping track of all unique IP addresses that visited a website today

print("\nb)")
print("Data Structure: Set")
print("Reason: Sets automatically remove duplicates and allow fast membership checks.")

# c) Mapping country codes to country names

print("\nc)")
print("Data Structure: Dictionary")
print("Reason: Dictionaries store data as key-value pairs (e.g., 'IN' -> 'India').")

# d) Storing 100 student exam scores where order matters

print("\nd)")
print("Data Structure: List")
print("Reason: Lists maintain order and allow duplicate values.")

# e) Storing an employee record: (emp_id, name, dept, salary)

print("\ne)")
print("Data Structure: Tuple")
print("Reason: Employee records are fixed collections of values that usually should not change.")































# ===== Challenge 1 =====

print("\n===== Challenge 1 =====")

# a) Store at least 10 student records

students = [
    {"name": "Aman", "roll": 1, "subjects": {"Math": 88, "Science": 76, "English": 90}},
    {"name": "Riya", "roll": 2, "subjects": {"Math": 92, "Science": 85, "English": 78}},
    {"name": "Rahul", "roll": 3, "subjects": {"Math": 45, "Science": 52, "English": 60}},
    {"name": "Neha", "roll": 4, "subjects": {"Math": 70, "Science": 65, "English": 72}},
    {"name": "Arjun", "roll": 5, "subjects": {"Math": 55, "Science": 90, "English": 82}},
    {"name": "Priya", "roll": 6, "subjects": {"Math": 98, "Science": 95, "English": 91}},
    {"name": "Ishita", "roll": 7, "subjects": {"Math": 80, "Science": 75, "English": 88}},
    {"name": "Karan", "roll": 8, "subjects": {"Math": 60, "Science": 67, "English": 70}},
    {"name": "Meera", "roll": 9, "subjects": {"Math": 86, "Science": 89, "English": 92}},
    {"name": "Dev", "roll": 10, "subjects": {"Math": 40, "Science": 42, "English": 44}}
]

# b) Function to calculate average marks

def get_average(student):
    marks = student["subjects"].values()
    return sum(marks) / len(marks)

print("\nStudent Averages:")

for student in students:
    print(f"{student['name']} -> {get_average(student):.2f}")

# c) Students who passed all subjects

passed_students = []

for student in students:
    if all(mark >= 40 for mark in student["subjects"].values()):
        passed_students.append(student["name"])

print("\nStudents Who Passed All Subjects:")
print(passed_students)

# d) Subjects where at least one student scored below 50

low_score_subjects = set()

for student in students:
    for subject, mark in student["subjects"].items():
        if mark < 50:
            low_score_subjects.add(subject)

print("\nSubjects Having At Least One Score Below 50:")
print(low_score_subjects)

# e) Dictionary of subject-wise scores

subject_scores = {}

for student in students:
    for subject, mark in student["subjects"].items():
        subject_scores.setdefault(subject, []).append(mark)

print("\nSubject Wise Scores:")

for subject, scores in subject_scores.items():
    print(f"{subject}: {scores}")

print("\nClass Average Per Subject:")

for subject, scores in subject_scores.items():
    average = sum(scores) / len(scores)
    print(f"{subject}: {average:.2f}")

# f) Find topper and rank all students

ranked_students = sorted(
    students,
    key=get_average,
    reverse=True
)

print("\nTopper:")
print(
    f"{ranked_students[0]['name']} "
    f"with average {get_average(ranked_students[0]):.2f}"
)

print("\nStudent Rankings:")

for rank, student in enumerate(ranked_students, start=1):
    print(
        f"{rank}. {student['name']} "
        f"({get_average(student):.2f})"
    )

# g) Subjects taken by ALL students

common_subjects = set(students[0]["subjects"].keys())

for student in students[1:]:
    common_subjects = common_subjects.intersection(
        set(student["subjects"].keys())
    )

print("\nSubjects Taken By All Students:")
print(common_subjects)

print("\n===== Assignment Completed Successfully =====")