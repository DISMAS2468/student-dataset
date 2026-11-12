import csv

students = [
    ["STU001", "Computer Science", 100, 92, 78],
    ["STU002", "Cyber Security", 200, 85, 81],
    ["STU003", "Software Engineering", 300, 96, 88],
    ["STU004", "Information Technology", 100, 74, 69],
    ["STU005", "Computer Science", 400, 89, 91],
    ["STU006", "Data Science", 200, 91, 84],
    ["STU007", "Cyber Security", 300, 80, 76],
    ["STU008", "Software Engineering", 200, 93, 87],
    ["STU009", "Information Technology", 400, 86, 73],
    ["STU010", "Data Science", 300, 98, 95],
    ["STU011", "Computer Science", 200, 77, 72],
    ["STU012", "Cyber Security", 100, 88, 80],
    ["STU013", "Software Engineering", 400, 90, 89],
    ["STU014", "Information Technology", 300, 82, 75],
    ["STU015", "Data Science", 100, 95, 92],
]

# Save the fictional student records in a CSV file.
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Student_ID",
        "Department",
        "Level",
        "Attendance_Percentage",
        "Average_Examination_Score"
    ])
    writer.writerows(students)

print("Student dataset created successfully: students.csv")
