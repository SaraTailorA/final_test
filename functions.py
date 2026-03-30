
def add_student(students):
    """
    Add a new student to the list validing Id, name, age, course and status
    """
    name = input("Enter student's name: \n").strip()

    while name == "":
                print("Error: The coder's name cannot be empty. Please enter a valid name.")
                name = input("Type the coder's name: ").strip()

    try:
        # Ask and validate the UI inmediately
        ui = int(input("Enter student's ID: \n"))
        if ui < 0:
            print("Error: Unique identifier (UI) cannot be negative.\n")
            return  # It throws them onto the menu BEFORE asking for their age
        for student in students:
            if student["ui"] == ui:
                print("error: This ID already exist.\n")
                return

        # If the ID was correct, NOW we will ask for your age
        age = int(input("Enter student's age: \n"))
        if age < 0:
            print("Error: age cannot be negative.\n")
            return  # It returns to the menu if the amount is negative.
        
        course = input("Enter the course's name: \n").strip()
        while course == "":
            print("Error: The course's name cannot be empty. Please enter a valid course.")
            course = input("Enter the course's name: ").strip()
        
        status= input("Enter the student's status (APPROVED/ NOT APPROVED): \n").strip().lower()
        while status not in ["approved", "not approved"]:
            print("Error: The status cannot be empty. Please enter a valid status")
            status = input ("Enter status (approved or not approved)").strip().lower()

        # 3. If everything is good, save it.
        student = {
            "name": name,
            "ui": ui,
            "age": age,
            "course": course,
            "status": status
        }

        students.append(student)
        print("\nStudent added successfully.\n")
    except ValueError:
        print("\nError: Invalid input. You must enter numbers for ID and age.\n")


def students_list(students):
    """
    show all current students in a simple table.
    """
    if len(students) == 0:
        print("\nNo students available.\n")
    else:
        print("-" * 50)
        print("                  Students ")
        print("-" * 50)
        for student in students:
            print(f"Name: {student['name']} | ui: {student['ui']} | Age: {student['age']} | Course: {student['course']} | Status: {student['status']}")
        print()


def search_student(students):
    """
    Search a student using their name and print their details.
    """
    name = input("Enter student name to search: ").strip()

    for student in students:
        if student["name"].lower() == name.lower():
            print(f"\nStudent found -> Name: {student['name']} | ui: {student['ui']} | Age: {student['age']} | Course: {student['course']} | Status: {student['status']}\n")
            return

    print("Student not found.\n")


def update_student(students):
    """
    Update student's details like, name, age, course and status.
    """
    ui = int(input("Enter student UI to update: "))

    for student in students:
        if student["ui"] == ui:

            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Age")
            print("3. Course")
            print("4. Status")

            choice = input ("Choose an option: ")

            if choice == "1":
                new_name = input("New name: ").strip()
                if new_name:
                    student["name"] = new_name
            elif choice == "2":
                try:
                    new_age = int(input("New age: "))
                    if new_age >= 0:
                        student["age"] = new_age
                    else:
                        print("Age cannot be negative.")
                except ValueError:
                    print("Invalid age. ")
            elif choice == "3":
                new_course = input("New course: ").strip()
                if new_course:
                    student["course"] = new_course 
            elif choice == "4":
                new_status = input ("New status (approved/not approved): ").strip().lower()
                if new_status in ["approved", "not approved"]:
                    student["status"] = new_status
                else:
                    print("Invalid status")
            else:
                print("Invalid option.")
            print("\nStudent updated succesfully.\n")
            return

    print("student not found.\n")


def delete_student(students):
    """
    Delete a student through their name.
    """
    name = input("Enter student's name to delete: ").strip()

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("student deleted successfully.\n")
            return

    print("student not found.\n")