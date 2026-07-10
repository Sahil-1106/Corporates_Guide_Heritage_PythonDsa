n = int(input("Number of Students: "))

students = []
total = 0

for i in range(n):
    name, marks = input("Enter Student details: ").split()
    marks = int(marks)

    students.append([name, marks])
    total += marks

avg = total / n
print(f"Average marks are: {avg}")
result = []

for student in students:
    if student[1] >= avg:
        result.append(student[0])

result.sort()

for name in result:
    print(f"Names of student scoring above average in Alphabetical Order are: \n{name}")