# Function to create student tuples and store in a list
def create_students():
    students = [
        ("Alice", 1, (85, 90, 95), "A"),
        ("Bob", 2, (78, 82, 88), "B"),
        ("Charlie", 3, (92, 94, 96), "A"),
    ]
    return students

# Function to display all students
def display_students(students):
    print("All Student Records:")
    for student in students:
        print(student)

# Function to add a new student
def add_student(students, name, roll_number, marks, grade):
    new_student = (name, roll_number, marks, grade)
    students.append(new_student)

# Function to search for a student by roll number
def search_student(students, roll_number):
    for student in students:
        if student[1] == roll_number:
            print("Student Found:", student)
            return
    print("Student not found.")

# Function to calculate total marks for each student
def calculate_total_marks(students):
    print("Total Marks for Each Student:")
    for student in students:
        total_marks = sum(student[2])
        print(f"{student[0]} (Roll Number {student[1]}): {total_marks}")

# Function to update a student's grade
def update_grade(students, roll_number, new_grade):
    for i, student in enumerate(students):
        if student[1] == roll_number:
            students[i] = (student[0], student[1], student[2], new_grade)
            print("Grade updated.")
            return
    print("Student not found.")

# Function to remove a student by roll number
def remove_student(students, roll_number):
    for i, student in enumerate(students):
        if student[1] == roll_number:
            students.pop(i)
            print("Student removed.")
            return
    print("Student not found.")

# Main Program
students = create_students()
display_students(students)
add_student(students, "Dave", 4, (75, 80, 85), "B")
display_students(students)
search_student(students, 2)
calculate_total_marks(students)
update_grade(students, 3, "A+")
display_students(students)
remove_student(students, 1)
display_students(students)
