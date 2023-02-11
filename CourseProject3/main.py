# course project 3 of python
#  college management system with file handling in python

def main_menu():
    print("\n Welcome to College Management System")
    print("1. Add a student")
    print("2. Delete a student")
    print("3. Display all students")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    return choice

# adding student record 
def add_student():
    with open("students.txt", "a") as f:
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        f.write(f"{name},{roll}\n")
    print("Student added successfully")

# deleting student record 
def delete_student():
    roll = input("Enter roll number of student to delete: ")
    with open("students.txt", "r") as f:
        lines = f.readlines()
    with open("students.txt", "w") as f:
        for line in lines:
            if roll not in line:
                f.write(line)
    print("Student deleted successfully")

# display student record 
def display_students():
    with open("students.txt", "r") as f:
        lines = f.readlines()
    print("Name, Roll Number")
    for line in lines:
        print(line.strip())

while True:
    choice = main_menu()
    if choice == 1:
        add_student()
    elif choice == 2:
        delete_student()
    elif choice == 3:
        display_students()
    elif choice == 4:
        break
    else:
        print("Invalid choice, try again")