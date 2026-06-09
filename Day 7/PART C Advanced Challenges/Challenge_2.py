history = []

while True:
    print("\n===== Calculator Menu =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ")

    if choice == "6":
        print("\nOperation History:")
        if len(history) == 0:
            print("No operations performed.")
        else:
            for operation in history:
                print(operation)

        print("\nExiting Calculator...")
        break

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice! Please select a valid option.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = num1 + num2
        operation = f"{num1} + {num2} = {result}"

    elif choice == "2":
        result = num1 - num2
        operation = f"{num1} - {num2} = {result}"

    elif choice == "3":
        result = num1 * num2
        operation = f"{num1} * {num2} = {result}"

    elif choice == "4":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue

        result = num1 / num2
        operation = f"{num1} / {num2} = {result}"

    elif choice == "5":
        result = num1 ** num2
        operation = f"{num1} ^ {num2} = {result}"

    print("Result:", result)
    history.append(operation)