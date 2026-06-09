attempts = 0

while True:
    password = input("Enter password: ")
    attempts += 1

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    min_length = len(password) >= 8

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True

    criteria_met = 0

    print("\nPassword Check:")

    if min_length:
        print("✓ Minimum 8 characters")
        criteria_met += 1
    else:
        print("✗ Minimum 8 characters")

    if has_upper:
        print("✓ Contains uppercase letter")
        criteria_met += 1
    else:
        print("✗ Contains uppercase letter")

    if has_lower:
        print("✓ Contains lowercase letter")
        criteria_met += 1
    else:
        print("✗ Contains lowercase letter")

    if has_digit:
        print("✓ Contains digit")
        criteria_met += 1
    else:
        print("✗ Contains digit")

    if has_special:
        print("✓ Contains special character")
        criteria_met += 1
    else:
        print("✗ Contains special character")

    if criteria_met <= 2:
        strength = "Weak"
    elif criteria_met <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print("Password Strength:", strength)
    print("Attempts:", attempts)

    if strength == "Strong":
        print("\nStrong password accepted!")
        break

    print("\nPlease try again.\n")