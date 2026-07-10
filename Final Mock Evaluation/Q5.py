n = int(input("Enter the number of Employes: "))

best_name = ""
best_score = float("-inf")

for i in range(n):
    empid, name, score = input("Enter Details: ").split()
    score = int(score)

    if score > best_score:
        best_score = score
        best_name = name
    elif score == best_score:
        if name < best_name:
            best_name = name

print(best_name, best_score)