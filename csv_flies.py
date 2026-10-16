# CSV = Comma-Separated Values

# 5.a Importing CSV
import csv

# 5.b Writing CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Adi", 21, "CSE"])

# 5.c Reading CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# 5.d CSV Use Cases
# Student records
# Employee records
# Expenses
# Sales data