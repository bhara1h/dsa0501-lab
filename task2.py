import csv

employees = []
for i in range(5):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    dept = input("Enter Department: ")
    designation = input("Enter Designation: ")
    salary = input("Enter Salary: ")
    employees.append([emp_id, name, dept, designation, salary])

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Employee ID", "Employee Name", "Department", "Designation", "Salary"])
    writer.writerows(employees)

print("✅ employees.csv created successfully!")
