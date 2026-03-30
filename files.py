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
            # Write header
            file.write("name, ui, age, course, status\n")

            # Write students
            for student in students:
                line = f"Name: {student['name']} | ui: {student['ui']} | Age: {student['age']} | Course: {student['course']} | Status: {student['status']}\n"
                file.write(line)

        print(f"Students saved successfully in {file_name}.\n")

    except Exception as e:
        # Catch any permission or write errors without closing the app
        print(f"Error saving file: {e}\n")


def load_csv(file_name):
    """
    Upload products from a CSV file.
    Skip invalid rows and count how many there were to notify the user.
    """
    loaded_students = []
    skipped_lines = 0

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

            # If the file is empty
            if len(lines) <= 1:
                print("File is empty or only has headers.\n")
                return loaded_students

            # Scroll from row 1 to skip the header
            for i in range(1, len(lines)):
                parts = lines[i].strip().split(",")

                # Validate that it has exactly 5 columns
                if len(parts) != 5:
                    skipped_lines += 1
                    continue

                try:
                    name = parts[0].strip()
                    ui = int(parts[1])
                    age = int(parts[2])
                    course = parts[3].strip()
                    status = parts[4].strip()

                    # Validate that they are not negative
                    if ui < 0 or age < 0:
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
                    # If ui or age are not numbers, skip this row
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