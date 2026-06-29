s = input("Enter a string: ")

# Reverse
reversed_s = ""
for i in range(len(s) - 1, -1, -1):
    reversed_s += s[i]

print("Reversed string:", reversed_s)


if s == reversed_s:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")


lst = input("Enter list elements: ").split()


unique_list = []
for item in lst:
    if item not in unique_list:
        unique_list.append(item)

print("List without duplicates:", unique_list)


n = int(input("Enter a number: "))

factorial = 1

if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial of", n, "is", factorial)
    
    
    
lst = list(map(int, input("Enter numbers separated by spaces: ").split()))


largest = lst[0]


for num in lst:
    if num > largest:
        largest = num

print("Largest element:", largest)





n = int(input("Enter a number: "))

if n <= 1:
    print(n, "is not a prime number")
else:
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")