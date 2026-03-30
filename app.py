from functions import *
from files import *

# Main list to save students information (students in memory)
students = []

# Variable to handle the menu loop
option = ""

# Main loop to show the main until the user choose exit(8)
while option != "9":
    print("=" * 40)
    print("                   MENU                  ")
    print("=" * 40)
    print("1. Add student")
    print("2. Student list")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Save CSV")
    print("7. Load CSV")
    print("8. Exit")

    option = input("\nChoose an option: ")

    if option == "1":
        add_student(students)

    elif option == "2":
        students_list(students)

    elif option == "3":
        search_student(students)

    elif option == "4":
        update_student(students)

    elif option == "5":
        delete_student(students)

    elif option == "6":
        file_name = input("Enter file name to save (example: data.csv): ")
        save_csv(students, file_name)

    elif option == "7":
        file_name = input("Enter file name to load: ")
        loaded_students = load_csv(file_name)
        
        # Si se cargó información correctamente, preguntamos qué hacer con ella
        if loaded_students:
            choice = input("Overwrite current student list? (Y/N): ").strip().upper()
            
            if choice == "Y":
                # Sobrescribir: reemplazamos la lista actual
                students = loaded_students
                print("Student list overwritten successfully.\n")
            else:
                # Fusionar por nombre (si existe, suma cantidad y actualiza precio)
                for new_item in loaded_students:
                    found = False
                    for existing_item in students:
                        if existing_item["name"].lower() == new_item["name"].lower():
                            existing_item["quantity"] += new_item["quantity"]
                            existing_item["price"] = new_item["price"]
                            found = True
                            break
                    
                    # Si no se encontró el producto, lo agregamos como nuevo
                    if not found:
                        students.append(new_item)
                print("Student list merged successfully.\n")

    elif option == "8":
        print("Closing program... Goodbye!")

    else:
        print("Invalid option. Please enter a number from 1 to 8.\n")