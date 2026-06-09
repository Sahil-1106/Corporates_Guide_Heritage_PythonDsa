import time

# Part A: Benchmark Different Looping Approaches

n = 1_000_000

# For loop with append
start = time.time()
squares = []
for i in range(1, n + 1):
    squares.append(i * i)
end = time.time()
print("For loop with append:", end - start, "seconds")

# List comprehension
start = time.time()
squares = [i * i for i in range(1, n + 1)]
end = time.time()
print("List comprehension:", end - start, "seconds")

# Generator expression
start = time.time()
squares = (i * i for i in range(1, n + 1))
for _ in squares:
    pass
end = time.time()
print("Generator expression:", end - start, "seconds")


# Part B: First n Numbers Divisible by Both 3 and 7

def using_for(n):
    result = []
    num = 21

    for i in range(n):
        result.append(num)
        num += 21

    return result


def using_while(n):
    result = []
    num = 21

    while len(result) < n:
        result.append(num)
        num += 21

    return result


def using_list_comprehension(n):
    return [21 * i for i in range(1, n + 1)]


n = 10

print("\nUsing for loop:")
print(using_for(n))

print("\nUsing while loop:")
print(using_while(n))

print("\nUsing list comprehension:")
print(using_list_comprehension(n))

print("\nReadability Comparison:")
print("List comprehension is the shortest and most readable.")
print("For loop is easy to understand and flexible.")
print("While loop works well but is slightly longer for this task.")


# Part C: Matrix Multiplication

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Using nested loops
result1 = [[0 for j in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        for k in range(3):
            result1[i][j] += A[i][k] * B[k][j]

print("\nMatrix Multiplication using Nested Loops:")
for row in result1:
    print(row)

# Using list comprehensions
result2 = [
    [
        sum(A[i][k] * B[k][j] for k in range(3))
        for j in range(3)
    ]
    for i in range(3)
]

print("\nMatrix Multiplication using List Comprehensions:")
for row in result2:
    print(row)

print("\nComparison:")
print("Nested loops are easier to understand for beginners.")
print("List comprehensions are shorter and more compact.")
print("Both produce the same result, but nested loops are usually better for learning matrix multiplication.")