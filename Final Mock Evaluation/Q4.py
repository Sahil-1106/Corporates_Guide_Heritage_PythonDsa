n = int(input("Enter size: "))

temp = input("Enter List: ").split()
arr = []

for i in temp:
    arr.append(int(i))

result = []

for num in arr:
    if num not in result:
        result.append(num)
print("List with no repetation: ")
for num in result:
    print(num, end=" ")