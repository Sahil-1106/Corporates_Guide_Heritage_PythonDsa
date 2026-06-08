# Simple Login System using Nested if Statements

username = input("Enter username: ")
password = input("Enter password: ")

stored_username = "admin"
stored_password = "pass123"
account_active = True

if username == stored_username:
    if account_active:
        if password == stored_password:
            print("Login Successful!")
        else:
            print("Incorrect Password!")
    else:
        print("Account is Inactive!")
else:
    print("Username does not exist!")