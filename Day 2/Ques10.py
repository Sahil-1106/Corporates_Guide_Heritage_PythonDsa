name = "Sahil"
employee_id = "101"
salary = "55000.75"
department = "Human Resources"
is_active = "True"

employee_id = int(employee_id)
salary = float(salary)

report = f"""
EMPLOYEE PROFILE
----------------
Name       : {name}
ID         : {employee_id:06d}
Department : {department}
Salary     : ₹{salary:,.2f}
Active     : {is_active}
"""

print(report)