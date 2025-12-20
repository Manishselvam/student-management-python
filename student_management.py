import json
import os

FILE = "students.json"

# Load students from file if it exists
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        students = json.load(f)
else:
    students = []

def save_students():
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    students.append({"name": name, "roll": roll})
    save_students()
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return

    print(f"Total Students: {len(students)}\n")

    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}")
    print()


def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"Student Found: {s['name']}\n")
            return
    print("Student not found.\n")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for i, s in enumerate(students):
        if s["roll"] == roll:
            students.pop(i)
            save_students()
            print(f"Student {roll} deleted successfully!\n")
            return
    print("Student not found.\n")

while True:
    print("---- Student Management System ----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.\n")
