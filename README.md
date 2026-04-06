
# Student Registration System
Welcome to my Student Registration project! This is a Python program designed to facilitate the recording and tracking of student data.
---
## Description

This system allows interaction with a dynamic menu to manage students information. The program guarantees data integrity through validations, offers to updating student's informations, allows saving and loading information in CSV files, ensuring that data is not lost when the application is closed.

The program asks the user to enter the name, ui (unique identifier), age, course and status (approved/not approved)
---
## Technologies and Concepts Used

For the development of this tool, I applied fundamental programming concepts that ensure clean and functional code:

### **Tecnologías**
* **Language: ** Python 3.x
* **Storage: ** .csv (Comma-Separated Values)
* **Execution Environment: ** Terminal / Console
* **Editor: ** VS Code (Visual Studio Code)

### **Programming Concepts Applied**
* **Data Structures: ** Use of `lists` for global storage and dictionaries to represent each student (name, ui, age, course, status).
* **Flow Control: ** Implementation of `while loops` for menu persistence and `if-elif-else` conditionals for navigation logic.
* **Data Validation (Error Handling): **Use of `try-except` blocks to prevent unexpected closures if the user enters non-numeric data or empty data.
* **Modularization: ** Organization of the code using specific functions `(add_student, student_list, search_student, update_student, delete_student)` to improve readability.

* **Full CRUD Operations: **Logic to create, read, update, and delete students records.
* **Data Persistence (File I/O): **Reading and writing text files using context managers (with open()) for safe memory management.
* **Advanced Modularization: **Architecture divided into multiple files `(app.py, functions.py, files.py)` and module import to separate the interface, business logic, and data access.
* **Best Practices: **Implementation of docstrings for internal documentation of functions and `merge/overwrite` algorithms to avoid data duplication.

## Examples of use
We can use this system to register new students or update the current one, for example in a public school that needs to register many students when a new scholar year starts and also update the old students in new course. 
---
## Status

> The program is currently running as a basic learning project and is demonstrating how Python handles user input and data validation.
