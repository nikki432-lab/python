def generate_student_report(name, grade):
    report = f"Student: {name}\nFinal Grade: {grade}"
    return report

if __name__ == "__main__":
    student_name = input("Enter the student's name: ")
    final_grade = input("Enter the final grade: ")
    
    report = generate_student_report(student_name, final_grade)
    print("\n--- Report ---")
    print(report)
