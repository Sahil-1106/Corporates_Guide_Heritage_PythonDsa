print("=================================")
print("Question 1: Reverse an Array/List")
print("=================================")

arr = [10, 20, 30, 40, 50]

reversed_arr = []
for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])

print("Input :", arr)
print("Output:", reversed_arr)



print("==========================================")
print("Question 2: Largest and Smallest Element")
print("==========================================")

arr = [12, 45, 7, 89, 23]

largest = arr[0]
smallest = arr[0]

for num in arr:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Input :", arr)
print("Largest =", largest)
print("Smallest =", smallest)



print("\n"+"=========================================")
print("Question 3: Remove Duplicate Elements")
print("===============================================")

arr = [1, 2, 2, 3, 4, 4, 5]

unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("Input :", arr)
print("Output:", unique)



print("\n"+"===========================================")
print("Question 4: Count Frequency of Each Element")
print("=================================================")

arr = [1, 2, 2, 3, 1, 4, 2]

frequency = {}

for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Input :", arr)
print("Output:")
for key in frequency:
    print(key, "→", frequency[key])




print("\n"+"==============================================")
print("Question 5: Find the Second Largest Number")
print("==============================================")

arr = [15, 10, 45, 32, 60]

largest = second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Input :", arr)
print("Second Largest =", second_largest)