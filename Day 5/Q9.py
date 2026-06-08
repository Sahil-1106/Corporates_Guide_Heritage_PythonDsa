# ATM System using if-elif-else, nested if, and match-case

correct_pin = "1234"
balance = 5000.0

pin = input("Enter your PIN: ")

if pin == correct_pin:
    print("\nLogin Successful!")
    
    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    
    choice = int(input("Enter your choice (1-4): "))
    
    match choice:
        case 1:
            print(f"Current Balance: ₹{balance:.2f}")
        
        case 2:
            amount = float(input("Enter withdrawal amount: ₹"))
            
            if amount > 0:
                if amount <= balance:
                    balance -= amount
                    print("Withdrawal Successful!")
                    print(f"Remaining Balance: ₹{balance:.2f}")
                else:
                    print("Insufficient Funds!")
            else:
                print("Invalid Amount!")
        
        case 3:
            amount = float(input("Enter deposit amount: ₹"))
            
            if amount > 0:
                balance += amount
                print("Deposit Successful!")
                print(f"Updated Balance: ₹{balance:.2f}")
            else:
                print("Invalid Amount!")
        
        case 4:
            print("Thank you for using the ATM.")
        
        case _:
            print("Invalid Menu Choice!")
else:
    print("Incorrect PIN! Access Denied.")