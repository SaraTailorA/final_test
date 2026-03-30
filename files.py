def save_csv(students, file_name):
    """
    Save the current students list in a csv file.
    Use 'with open' to a handle file in a safe way.
    """
    if len(students) == 0:
        print("Students list is empty, nothing to save.\n")
        return
    # If text DOES NOT end in.csv, we're going to add it automatically.
    if not file_name.lower().endswith('.csv'):
        file_name = file_name + ".csv"
        print(f"Auto-corrected file name to: {file_name}")

    try:
        # 'with' abre el archivo y lo cierra automáticamente al terminar
        with open(file_name, "w", encoding="utf-8") as file:
            # Escribir encabezado
            file.write("name, ui, age, course, status\n")

            # Escribir productos
            for student in students:
                line = f"Name: {student['name']} | ui: {student['ui']} | Age: {student['age']} | Course: {student['course']} | Status: {student['status']}\n"
                file.write(line)

        print(f"Students saved successfully in {file_name}.\n")

    except Exception as e:
        # Atrapa cualquier error de permisos o de escritura sin cerrar la app
        print(f"Error saving file: {e}\n")


def load_csv(file_name):
    """
    Carga productos desde un archivo CSV.
    Omite filas inválidas y cuenta cuántas fueron para avisarle al usuario.
    """
    loaded_students = []
    skipped_lines = 0

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

            # Si el archivo está vacío
            if len(lines) <= 1:
                print("File is empty or only has headers.\n")
                return loaded_students

            # Recorrer a partir de la fila 1 para saltar el encabezado
            for i in range(1, len(lines)):
                parts = lines[i].strip().split(",")

                # Validar que tenga exactamente 5 columnas
                if len(parts) != 5:
                    skipped_lines += 1
                    continue

                try:
                    name = parts[0].strip()
                    ui = int(parts[1])
                    age = int(parts[2])
                    course = parts[3].strip()
                    status = parts[4].strip()

                    # Validar que no sean negativos
                    if id < 0 or age < 0:
                        skipped_lines += 1
                        continue

                    student = {
                        "name": name,
                        "ui": ui,
                        "age": age,
                        "course": course,
                        "status": status
                    }
                    loaded_students.append(student)

                except ValueError:
                    # If ui or age are not numbers, skip this line fila
                    skipped_lines += 1

        print(f"\nFile loaded. {len(loaded_students)} student found.")
        
        if skipped_lines > 0:
            print(f"Warning: {skipped_lines} invalid rows were skipped.")
            
        return loaded_students

    except FileNotFoundError:
        print("\nError: The specified file was not found.\n")
        return None
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}\n")
        return None