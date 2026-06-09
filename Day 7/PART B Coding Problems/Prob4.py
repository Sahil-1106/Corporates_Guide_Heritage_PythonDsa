n = 5

# Pattern A
print("Pattern A:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()

# Pattern B
print("Pattern B:")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print()

# Pattern C
print("Pattern C:")
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    
    for j in range(i):
        print("* ", end="")
    
    print()