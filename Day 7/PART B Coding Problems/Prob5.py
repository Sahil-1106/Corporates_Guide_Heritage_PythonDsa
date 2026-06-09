# Part A: Count, Sum, Maximum and Minimum

count = 0
total = 0
maximum = None
minimum = None

print("Enter integers (0 to stop):")

while True:
    num = int(input())

    if num == 0:
        break

    count += 1
    total += num

    if maximum is None or num > maximum:
        maximum = num

    if minimum is None or num < minimum:
        minimum = num

print("\nPart A Results")
print("Count =", count)
print("Sum =", total)
print("Maximum =", maximum)
print("Minimum =", minimum)


# Part B: Prime Numbers from 1 to 100

prime_count = 0

print("\nPrime numbers between 1 and 100:")

for num in range(2, 101):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
        prime_count += 1

print("\nTotal Prime Numbers =", prime_count)


# Part C: Reverse a Number

num = int(input("\nEnter a number to reverse: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed Number =", reverse)