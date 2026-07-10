n = int(input("Enter size: "))

temp = input("Enter Element: ").split()
arr = []

for i in temp:
    arr.append(int(i))

first = float("-inf")
second = float("-inf")

for x in arr:
    if x > first:
        second = first
        first = x
    elif x != first and x > second:
        second = x

if second == float("-inf"):
    print(-1)
else:
    print(f"Second Largest no. is {second}")