# ============================================
# All questions in one Python script
# ============================================

import time

def section(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


# --------------------------------------------------
# Q1. Basic Binary Search
# --------------------------------------------------
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# --------------------------------------------------
# Q2. Count Occurrences Using Binary Search
# --------------------------------------------------
def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            ans = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans


def last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            ans = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans


def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    if first == -1:
        return 0
    last = last_occurrence(arr, target)
    return last - first + 1


# --------------------------------------------------
# Q3. Recursive Binary Search
# --------------------------------------------------
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


# --------------------------------------------------
# Q4. Factorial Using Recursion + Sum of Digits Using Recursion
# --------------------------------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def sum_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)


# --------------------------------------------------
# Q5. Performance Comparison
# --------------------------------------------------
def performance_comparison():
    # (a) Append 100,000 elements to a Python list
    start = time.time()
    py_list = []
    for i in range(100_000):
        py_list.append(i)
    list_time = time.time() - start

    # (b) Create a NumPy array of 100,000 elements
    try:
        import numpy as np

        start = time.time()
        np_array = np.arange(100_000)
        numpy_time = time.time() - start

        print(f"Python list append time: {list_time:.6f} seconds")
        print(f"NumPy array creation time: {numpy_time:.6f} seconds")
        print("Comparison: NumPy is usually faster for bulk numeric array creation.")
    except ImportError:
        print(f"Python list append time: {list_time:.6f} seconds")
        print("NumPy is not installed, so NumPy timing could not be measured.")


# --------------------------------------------------
# Q6. Pair Sum – Find All Pairs
# --------------------------------------------------
def find_all_pairs(arr, target):
    left = 0
    right = len(arr) - 1
    pairs = []

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return pairs


# --------------------------------------------------
# Q7. Remove Duplicates In-Place (Two-Pointer)
# --------------------------------------------------
def remove_duplicates_in_place(arr):
    if not arr:
        return 0

    slow = 0

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1


# --------------------------------------------------
# Q8. Max Average Subarray
# --------------------------------------------------
def max_average_subarray(arr, k):
    if k <= 0 or k > len(arr):
        raise ValueError("k must be between 1 and len(arr)")

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k


# --------------------------------------------------
# Q9. Longest Subarray with Sum <= K (Positive Integers)
# --------------------------------------------------
def longest_subarray_sum_leq_k(arr, K):
    left = 0
    current_sum = 0
    max_len = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > K and left <= right:
            current_sum -= arr[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# --------------------------------------------------
# BONUS. Search in a 2D Matrix
# --------------------------------------------------
def search_2d_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    row = 0
    col = cols - 1  # top-right corner

    while row < rows and col >= 0:
        current = matrix[row][col]

        if current == target:
            return True
        elif target < current:
            col -= 1
        else:
            row += 1

    return False


# ==================================================
# DEMO / TEST CASES
# ==================================================

section("Q1. Basic Binary Search")
arr1 = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target1 = 23
print("Array:", arr1)
print("Target:", target1)
print("Index found:", binary_search(arr1, target1))

section("Q2. Count Occurrences Using Binary Search")
arr2 = [1, 2, 2, 2, 3, 4]
target2 = 2
print("Array:", arr2)
print("Target:", target2)
print("Count:", count_occurrences(arr2, target2))

section("Q3. Recursive Binary Search")
print("Array:", arr1)
print("Target:", target1)
print("Index found:", binary_search_recursive(arr1, target1, 0, len(arr1) - 1))

section("Q4. Factorial and Sum of Digits Using Recursion")
n = 5
num = 1234
print(f"factorial({n}) =", factorial(n))
print(f"sum_of_digits({num}) =", sum_of_digits(num))

section("Q5. Performance Comparison")
performance_comparison()

section("Q6. Pair Sum – Find All Pairs")
arr6 = [1, 2, 3, 4, 5, 6, 7]
target6 = 8
pairs = find_all_pairs(arr6, target6)
print("Array:", arr6)
print("Target:", target6)
print("Pairs found:", pairs)

section("Q7. Remove Duplicates In-Place")
arr7 = [1, 1, 2, 3, 3, 4]
new_len = remove_duplicates_in_place(arr7)
print("Modified array:", arr7[:new_len])
print("New length:", new_len)

section("Q8. Max Average Subarray")
arr8 = [1, 12, -5, -6, 50, 3]
k8 = 4
print("Array:", arr8)
print("k:", k8)
print("Maximum average:", max_average_subarray(arr8, k8))

section("Q9. Longest Subarray with Sum <= K")
arr9 = [1, 2, 3, 4, 5]
K9 = 9
print("Array:", arr9)
print("K:", K9)
print("Longest length:", longest_subarray_sum_leq_k(arr9, K9))
print("Note: with positive integers, the correct answer for this example is 3.")

section("BONUS. Search in a 2D Matrix")
matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
target_bonus = 5
print("Matrix:", matrix)
print("Target:", target_bonus)
print("Found:", search_2d_matrix(matrix, target_bonus))