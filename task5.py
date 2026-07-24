import xml.etree.ElementTree as ET

courses = ET.Element("Courses")

for i in range(5):
    course = ET.SubElement(courses, "Course")
    ET.SubElement(course, "CourseCode").text = input("Enter Course Code: ")
    ET.SubElement(course, "CourseName").text = input("Enter Course Name: ")
    ET.SubElement(course, "Credits").text = input("Enter Credits: ")
    ET.SubElement(course, "Department").text = input("Enter Department: ")
    ET.SubElement(course, "FacultyName").text = input("Enter Faculty Name: ")

tree = ET.ElementTree(courses)
tree.write("courses.xml")

print("✅ courses.xml created successfully!")
