def factorial(n):
    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return

    result = 1
    for i in range(1, n + 1):
        result *= i

    print(f"Factorial of {n} = {result}")


def fibonacci(n):
    if n <= 0:
        print("Error: Number of terms must be positive.")
        return

    a, b = 0, 1
    count = 0

    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
    print()


# Part A
num = int(input("Enter a number for factorial: "))
factorial(num)

# Part B
terms = int(input("Enter number of Fibonacci terms: "))
fibonacci(terms)