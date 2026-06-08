# Triangle Type Checker

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Check if a valid triangle exists
if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid Triangle")

    # Check triangle type
    if a == b == c:
        print("Type: Equilateral")
    elif a == b or b == c or a == c:
        print("Type: Isosceles")
    else:
        print("Type: Scalene")

    # Check if right-angled
    sides = sorted([a, b, c])

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("Right-Angled: Yes")
    else:
        print("Right-Angled: No")

else:
    print("Invalid Triangle")