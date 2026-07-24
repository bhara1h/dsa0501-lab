import json

faculties = []
for i in range(5):
    fid = input("Enter Faculty ID: ")
    name = input("Enter Faculty Name: ")
    dept = input("Enter Department: ")
    designation = input("Enter Designation: ")
    experience = input("Enter Experience (Years): ")
    faculties.append({
        "Faculty ID": fid,
        "Faculty Name": name,
        "Department": dept,
        "Designation": designation,
        "Experience": experience
    })

with open("faculty.json", "w") as file:
    json.dump(faculties, file, indent=4)

print("✅ faculty.json created successfully!")
