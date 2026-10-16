import json

def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: File contains invalid data.")
        return {}

def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

def add_students(students):
    student_id = input("Enter student ID: ")

    if student_id in students:
        print("ID already exists.")
        return

    name = input("Enter Student Name: ")

    try:
        marks = float(input("Enter student marks: "))
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Please enter valid marks.")
        return

    students[student_id] = {
        "name": name,
        "marks": marks
    }

    save_students(students)
    print("Saved successfully.")

def view_students(students):
    if not students:
        print("Records not found.")
        return

    print("-------- Students Record --------")
    for student_id, details in students.items():
        print("Student ID:", student_id)
        print("Name:", details["name"])
        print("Marks:", details["marks"])
        print("----------------")

def search_students(students):
    student_id = input("Enter student ID: ")

    if student_id in students:
        print("\nFound!")
        print("Student ID:", student_id)
        print("Name:", students[student_id]["name"])
        print("Marks:", students[student_id]["marks"])
    else:
        print("Student not found.")

def update_student(students):
    student_id = input("Enter student ID you want to update: ")

    if student_id not in students:
        print("Student not found.")
        return

    print("1. Update Name")
    print("2. Update Marks")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter new name: ")
        students[student_id]["name"] = name
    elif choice == "2":
        try:
            marks = float(input("Enter new marks: "))
            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                return
            students[student_id]["marks"] = marks
        except ValueError:
            print("Please enter valid marks.")
            return
    else:
        print("Invalid choice.")
        return

    save_students(students)
    print("Student record updated successfully!")

def main():
    students = load_students()

    while True:
        print("\n===== STUDENT RECORDS SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_students(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_students(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

main()