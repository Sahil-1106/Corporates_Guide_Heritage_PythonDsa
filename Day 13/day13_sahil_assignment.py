# =============================================================================
# DSA Assignment - Sorting Algorithms
# =============================================================================


def section(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


# -----------------------------------------------------------------------------
# Q1. Bubble Sort – Trace the Steps
# -----------------------------------------------------------------------------
def bubble_sort_trace(arr):
    a = arr.copy()
    n = len(a)

    print("Original Array:", a)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        print(f"After Pass {i + 1}: {a}")

        if not swapped:
            break

    print("\nFully Sorted Array:", a)
    print("Passes required before array became sorted: 3")


# -----------------------------------------------------------------------------
# Q2. Selection Sort – Implementation & Explanation
# -----------------------------------------------------------------------------
def selection_sort(arr):
    a = arr.copy()
    n = len(a)

    print("Original Array:", a)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]

        print(f"After Step {i + 1}: {a}")

    print("\nFinal Sorted Array:", a)
    print("Minimum number of swaps possible = 0")
    print("Reason: If the array is already sorted, no swaps are needed.")


# -----------------------------------------------------------------------------
# Q3. Insertion Sort – Best vs Worst Case
# -----------------------------------------------------------------------------
def insertion_sort_with_count(arr):
    a = arr.copy()
    comparisons = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break

        a[j + 1] = key

    return a, comparisons


# -----------------------------------------------------------------------------
# Q4. Merge Sort – Recursion Tree
# -----------------------------------------------------------------------------
def print_merge_tree(arr, level=0):
    print("   " * level + str(arr))

    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    print_merge_tree(left, level + 1)
    print_merge_tree(right, level + 1)


# -----------------------------------------------------------------------------
# Q5. Quick Sort – One Partition Pass
# -----------------------------------------------------------------------------
def quick_partition(arr):
    a = arr.copy()
    pivot = a[-1]

    print("Array Before Partition:", a)
    print("Pivot =", pivot)

    i = -1

    for j in range(len(a) - 1):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[-1] = a[-1], a[i + 1]

    print("Array After Partition :", a)


# =============================================================================
# DEMO / OUTPUT SECTION
# =============================================================================

section("Q1. Bubble Sort – Trace the Steps")
arr1 = [29, 10, 14, 37, 13]
bubble_sort_trace(arr1)

section("Q2. Selection Sort – Implementation & Explanation")
arr2 = [64, 25, 12, 22, 11, 90, 3]
selection_sort(arr2)

section("Q3. Insertion Sort – Best vs Worst Case")

print("Part A : Already Sorted Array")
arr3a = [3, 5, 7, 9, 11]
sorted_arr, comparisons = insertion_sort_with_count(arr3a)
print("Array:", arr3a)
print("Sorted:", sorted_arr)
print("Comparisons:", comparisons)

print("\nPart B : Reverse Sorted Array")
arr3b = [11, 9, 7, 5, 3]
sorted_arr, comparisons = insertion_sort_with_count(arr3b)
print("Array:", arr3b)
print("Sorted:", sorted_arr)
print("Comparisons:", comparisons)

print("\nConclusion:")
print("Best Case  -> O(n)")
print("Worst Case -> O(n²)")
print("Insertion Sort is efficient for nearly sorted arrays.")

section("Q4. Merge Sort – Recursion Tree")
arr4 = [8, 3, 5, 4, 2, 7, 1, 6]

print("Recursion Tree:")
print_merge_tree(arr4)

print("\nMerge Steps:")
print("[8] + [3]       -> [3, 8]")
print("[5] + [4]       -> [4, 5]")
print("[2] + [7]       -> [2, 7]")
print("[1] + [6]       -> [1, 6]")
print("[3, 8] + [4, 5] -> [3, 4, 5, 8]")
print("[2, 7] + [1, 6] -> [1, 2, 6, 7]")
print("[3, 4, 5, 8] + [1, 2, 6, 7]")
print("                 -> [1, 2, 3, 4, 5, 6, 7, 8]")

section("Q5. Quick Sort – Pivot Selection & Comparison")

print("Part A : One Partition Pass")
arr5 = [15, 3, 9, 8, 5, 2, 7, 1, 6]
quick_partition(arr5)

print("\nPart B : Worst Case")
print("Worst Case Time Complexity : O(n²)")
print("Example Input : [1, 2, 3, 4, 5]")
print("Reason : Choosing the last element as pivot creates")
print("one empty partition and one partition of size n-1.")
print("To avoid this, use:")
print("1. Random Pivot")
print("2. Median-of-Three Pivot")
print("3. Introsort (used in many libraries)")