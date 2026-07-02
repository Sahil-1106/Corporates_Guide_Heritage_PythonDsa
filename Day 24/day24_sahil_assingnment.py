# ==========================================
# Question 1: Find Duplicate Elements in a List
# ==========================================

print("\n========== Question 1: Find Duplicate Elements in a List ==========\n")

numbers = list(map(int, input("Enter the list elements separated by spaces: ").split()))

duplicates = []
seen = set()

for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    seen.add(num)

print("Duplicate Elements:", duplicates)


# ==========================================
# Question 2: Find the Longest Word in a String
# ==========================================

print("\n========== Question 2: Find the Longest Word in a String ==========\n")

sentence = input("Enter a sentence: ")

words = sentence.split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest Word:", longest_word)






# ==========================================
# Question 3: Find the Intersection of Two Lists
# ==========================================

print("\n========== Question 3: Find the Intersection of Two Lists ==========\n")

list1 = list(map(int, input("Enter elements of List 1 (space-separated): ").split()))
list2 = list(map(int, input("Enter elements of List 2 (space-separated): ").split()))

intersection = []

for num in list1:
    if num in list2 and num not in intersection:
        intersection.append(num)

print("Intersection:", intersection)


# ==========================================
# Question 4: Merge Two Sorted Lists
# ==========================================

print("\n========== Question 4: Merge Two Sorted Lists ==========\n")

list1 = list(map(int, input("Enter sorted elements of List 1 (space-separated): ").split()))
list2 = list(map(int, input("Enter sorted elements of List 2 (space-separated): ").split()))

merged = []
i = 0
j = 0

while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

while i < len(list1):
    merged.append(list1[i])
    i += 1

while j < len(list2):
    merged.append(list2[j])
    j += 1

print("Merged List:", merged)