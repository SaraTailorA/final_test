#El sistema debe permitir:
""" 
• ID (identificador único)
• Nombre
• Edad
• Curso o programa
• Estado (activo/inactivo)• Registrar nuevos estudiantes. """
def add_student(students):
    """
    Add a new student to the list validing Id, name, age, course and status
    """
    name = input("Enter student's name: \n").strip()

    while name == "":
                print("Error: The coder's name cannot be empty. Please enter a valid name.")
                name = input("Type the coder's name: ").strip()

    try:
        # 1. Pedimos y validamos el ID INMEDIATAMENTE
        unique_identifier = float(input("Enter student's ID $: \n"))
        if unique_identifier < 0:
            print("Error: Unique identifier (UI) cannot be negative.\n")
            return  # Lo expulsa al menú ANTES de pedir la edad

        # 2. Si el ID estuvo bien, AHORA SÍ pedimos la edad
        age = int(input("Enter student's age: \n"))
        if age < 0:
            print("Error: age cannot be negative.\n")
            return  # Lo expulsa al menú si la cantidad es negativa
        
        course = input("Enter the course's name: \n").strip()
        while course == "":
            print("Error: The course's name cannot be empty. Please enter a valid name.")
            course = input("Enter the course's name: ").strip()
        
        status= input("Enter the student's status (APPROVED/ NOT APPROVED): \n").strip().lower
        while status == "":
            print("Error: The course's name cannot be empty. Please enter a valid name.")
            course = input("Enter the course's name: ").strip()
            if status == "approved":
                print(f"Student's status = APPROVED")
            else:
                print("Student's status = NOT APPROVED")

        # 3. If everything is good, save it.
        student = {
            "name": name,
            "unique identifier": unique_identifier,
            "age": age,
            "course": course,
            "status": status
        }

        students.append(student)
        print("\nStudent added successfully.\n")
    except:
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
            print(f"Name: {student['name']} | Unique indetifier: ${student['unique indetifier']} | Age: {student['age']} | Course: {student['course']} | Status: {student['status']}")
        print()


def search_student(students):
    """
    Search a student using their name and print their details.
    """
    name = input("Enter product name to search: ").strip()

    for student in students:
        if student["name"].lower() == name.lower():
            print(f"\nStudent found -> Name: {student['name']} | Unique indetifier: ${student['unique indetifier']} | Age: {student['age']} | Course: {student['course']} | Status: {student['status']}\n")
            return

    print("Student not found.\n")


def update_student(students):
    """
    Update student's details like age, course and status.
    """
    name = input("Enter product name to update: ").strip()

    for student in students:
        if student["name"].lower() == name.lower():
            try:
                new_age = int(input("New age: "))
                new_course = (input("New course "))

                if new_age < 0: 
                    print("Values cannot be negative.\n")
                    return

                student["age"] = new_age
                student["course"] = new_course
                print("Student updated successfully.\n")
                return
            except:
                print("Error: Invalid values. Please enter numbers.\n")
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