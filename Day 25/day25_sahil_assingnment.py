print("\n========== Question 1: Basic Dictionary Application ==========\n")
# 1) Create the dictionary 
student = {
    "name": "Sahil",
    "age": 20,
    "course": "B.Tech"
}

print("Student details:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])


# 2) Access and print the value 
key = "course"
print("\nValue of", key, ":", student[key])


# 3) Add a new key-value pair 
student["year"] = "3rd Year"
print("\nAfter adding new key-value pair:", student)


# 4) Update the value 
student["age"] = 21
print("\nAfter updating age:", student)


# 5) Delete a specific key 
del student["year"]
print("\nAfter deleting year:", student)






print("\n========== Question 2: Phone Book using Dictionary (CRUD) ==========\n")



phonebook = {
    "Sahil": "9876543210",
    "Kanishk": "9123456780",
    "Prince": "9988776655",
    "Ashoutosh": "9876501234"
}

while True:
    print("\n===== PHONE BOOK MENU =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Add Contact
        name = input("Enter contact name: ")
        if name in phonebook:
            print("Contact already exists.")
        else:
            number = input("Enter phone number: ")
            phonebook[name] = number
            print("Contact added successfully.")

    elif choice == 2:
        # Search Contact
        name = input("Enter contact name to search: ")
        if name in phonebook:
            print("Phone Number:", phonebook[name])
        else:
            print("Contact not found.")

    elif choice == 3:
        # Update Contact
        name = input("Enter contact name to update: ")
        if name in phonebook:
            number = input("Enter new phone number: ")
            phonebook[name] = number
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == 4:
        # Delete Contact
        name = input("Enter contact name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == 5:
        # Display All Contacts
        if len(phonebook) == 0:
            print("Phone book is empty.")
        else:
            print("\n----- Contact List -----")
            for name, number in phonebook.items():
                print(name, ":", number)

    elif choice == 6:
        print("Exiting Phone Book...")
        break

    else:
        print("Invalid choice! Please try again.")