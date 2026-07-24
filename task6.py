import xml.etree.ElementTree as ET

patients = ET.Element("Patients")

for i in range(10):
    patient = ET.SubElement(patients, "Patient")
    ET.SubElement(patient, "PatientID").text = input("Enter Patient ID: ")
    ET.SubElement(patient, "PatientName").text = input("Enter Patient Name: ")
    ET.SubElement(patient, "Age").text = input("Enter Age: ")
    ET.SubElement(patient, "Disease").text = input("Enter Disease: ")
    ET.SubElement(patient, "DoctorAssigned").text = input("Enter Doctor Assigned: ")

tree = ET.ElementTree(patients)
tree.write("patients.xml")

print("✅ patients.xml created successfully!")
