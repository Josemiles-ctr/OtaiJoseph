with open("students.csv", "r") as file:
    students = file.readlines()
for student in students:
    print(student.strip())
