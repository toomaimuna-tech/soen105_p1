# Validate marks

def get_marks(prompt="Enter marks (0-100): "):
    while True:
        marks = input(prompt)
        try:
            marks = float(marks)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 0 <= marks <= 100:
            return marks

        print("Marks must be between 0 and 100.")


# Calculate grade

def calculate_grade(final_score):
    if final_score >= 70:
        grade = 'A'
    elif final_score >= 60:
        grade = 'B'
    elif final_score >= 50:
        grade = 'C'
    elif final_score >= 40:
        grade = 'D'
    else:
        grade = 'E'

    if final_score >= 40:
        status = 'Pass'
    else:
        status = 'Fail'

    return grade, status


student = {}


# Register student
def register_student():
    name = input("Enter student name: ")
    reg_no = input("Enter registration number: ")

    if reg_no in student:
        print("Student already registered.")
        return

    cat1 = get_marks("Enter CAT1 marks: ")
    cat2 = get_marks("Enter CAT2 marks: ")
    final_exam = get_marks("Enter final exam marks: ")
    final_score = (cat1 * 0.15) + (cat2 * 0.15) + (final_exam * 0.7)
    grade, status = calculate_grade(final_score)

    student[reg_no] = {
        'name': name,
        'reg_no': reg_no,
        'CAT1': cat1,
        'CAT2': cat2,
        'final_exam': final_exam,
        'final_score': final_score,
        'grade': grade,
        'status': status
    }

    print("\nStudent registered successfully!")
    print("Final Score: ", round(final_score, 2))
    print("Grade: ", grade)
    print("Status: ", status)


# Display student details
def display_student(reg_no=None):
    if reg_no is None:
        reg_no = input("Enter registration number: ")

    if reg_no in student:
        info = student[reg_no]
        print("Student Name: ", info['name'])
        print("Registration Number: ", info['reg_no'])
        print("CAT1 Marks: ", info['CAT1'])
        print("CAT2 Marks: ", info['CAT2'])
        print("Final Exam Marks: ", info['final_exam'])
        print("Final Score: ", round(info['final_score'], 2))
        print("Grade: ", info['grade'])
        print("Status: ", info['status'])
    else:
        print("Student not found.")


# Display all students
def display_all_students():
    if not student:
        print("No students registered.")
        return

    print("\nAll Registered Students:")
    for reg_no in student:
        display_student(reg_no)
        print()


# Search student by registration number
def search_student():
    reg_no = input("Enter registration number to search: ")
    if reg_no in student:
        print("Student found:")
        display_student(reg_no)
    else:
        print("Student not found.")


# Generate class performance report
def generate_report():
    if not student:
        print("No students registered.")
        return

    scores = [info['final_score'] for info in student.values()]
    average_score = sum(scores) / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)
    pass_count = sum(1 for info in student.values() if info['status'] == 'Pass')
    fail_count = sum(1 for info in student.values() if info['status'] == 'Fail')

    print("\nClass Performance Report:")
    print("Average Score: ", round(average_score, 2))
    print("Highest Score: ", highest_score)
    print("Lowest Score: ", lowest_score)
    print("Number of Students Passed: ", pass_count)
    print("Number of Students Failed: ", fail_count)
    print("Total Students: ", len(student))


# Main menu
def main_menu():
    while True:
        print("\nStudent performance management system")
        print("1. Register Student")
        print("2. Display Student Details")
        print("3. Display All Students")
        print("4. Search Student by Registration Number")
        print("5. Generate Class Performance Report")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            display_student()
        elif choice == "3":
            display_all_students()
        elif choice == "4":
            search_student()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
