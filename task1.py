import csv

students = []
for i in range(10):
    reg_no = input("Enter Register Number: ")
    name = input("Enter Student Name: ")
    dept = input("Enter Department: ")
    python_marks = input("Enter Python Marks: ")
    ds_marks = input("Enter Data Science Marks: ")
    students.append([reg_no, name, dept, python_marks, ds_marks])

with open("student_marks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Register Number", "Student Name", "Department", "Python Marks", "Data Science Marks"])
    writer.writerows(students)

print("✅ student_marks.csv created successfully!")
