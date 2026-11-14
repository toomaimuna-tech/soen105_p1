print("STUDENT PERFORMANCE MANAGEMENT SYSTEM")
print("======================================")

students = {}


def register_student():
    print("\nRegister new student")
    name = input("Enter name: ")
    reg_no = input("Enter reg_no: ")

    if reg_no in students:
        print("Registration number is already in the system")
        return

    cat1 = float(input("Enter CAT 1 marks: "))
    cat2 = float(input("Enter CAT 2 marks: "))
    exam = float(input("Enter Exam marks: "))

    final_score = (cat1 * 0.15) + (cat2 * 0.15) + (exam * 0.70)

    if final_score >= 70:
        grade = "A"
        status = "Pass"
    elif final_score >= 60:
        grade = "B"
        status = "Pass"
    elif final_score >= 50:
        grade = "C"
        status = "Pass"
    elif final_score >= 40:
        grade = "D"
        status = "Pass"
    else:
        grade = "E"
        status = "Fail"

    students[reg_no] = {
        "Name": name,
        "Reg_no": reg_no,
        "CAT 1": cat1,
        "CAT 2": cat2,
        "Exam": exam,
        "Final score": final_score,
        "Grade": grade,
        "Status": status,
    }

    print("Student registered successfully")


def search_student():
    print("\nSearch for student")
    reg_no = input("Enter reg_no: ")

    if reg_no in students:
        student = students[reg_no]
        print("\nStudent Details:")
        for key, value in student.items():
            print(f"{key}: {value}")
    else:
        print("Student not found")


def view_all_students():
    print("\nAll Registered Students")
    if not students:
        print("No students registered yet.")
        return

    for reg_no, student in students.items():
        print(f"\nReg No: {reg_no}")
        for key, value in student.items():
            print(f"  {key}: {value}")


def update_student():
    print("\nUpdate student record")
    reg_no = input("Enter reg_no: ")

    if reg_no not in students:
        print("Student not found")
        return

    student = students[reg_no]
    print("Press Enter to keep current value")

    name = input(f"Enter new name ({student['Name']}): ") or student['Name']
    cat1 = input(f"Enter new CAT 1 ({student['CAT 1']}): ")
    cat2 = input(f"Enter new CAT 2 ({student['CAT 2']}): ")
    exam = input(f"Enter new Exam ({student['Exam']}): ")

    if cat1:
        student['CAT 1'] = float(cat1)
    if cat2:
        student['CAT 2'] = float(cat2)
    if exam:
        student['Exam'] = float(exam)

    student['Name'] = name

    final_score = (student['CAT 1'] * 0.15) + (student['CAT 2'] * 0.15) + (student['Exam'] * 0.70)
    student['Final score'] = final_score

    if final_score >= 70:
        student['Grade'] = "A"
        student['Status'] = "Pass"
    elif final_score >= 60:
        student['Grade'] = "B"
        student['Status'] = "Pass"
    elif final_score >= 50:
        student['Grade'] = "C"
        student['Status'] = "Pass"
    elif final_score >= 40:
        student['Grade'] = "D"
        student['Status'] = "Pass"
    else:
        student['Grade'] = "E"
        student['Status'] = "Fail"

    print("Student record updated successfully")


def delete_student():
    print("\nDelete student record")
    reg_no = input("Enter reg_no: ")

    if reg_no in students:
        del students[reg_no]
        print("Student record deleted successfully")
    else:
        print("Student not found")


while True:
    print("\nMenu")
    print("1. Register Student")
    print("2. Search Student")
    print("3. View All Students")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        register_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        view_all_students()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting system")
        break
    else:
        print("Invalid option. Please try again.")
