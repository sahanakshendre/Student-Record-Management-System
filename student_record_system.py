
import json

FILE_NAME = "students.txt"

# ---------------- FILE HANDLING ----------------

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

students = load_students()


# ---------------- GRADE CALCULATION ----------------

def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'


# ---------------- ADD STUDENT ----------------

def add_student():
    roll = input("Enter Roll Number: ")

    for student in students:
        if student['roll'] == roll:
            print("❌ Roll Number already exists!\n")
            return

    name = input("Enter Student Name: ")

    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for Subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)
    save_students()

    print("✅ Student Added Successfully!\n")


# ---------------- VIEW STUDENTS ----------------

def view_students():
    if not students:
        print("No students available.\n")
        return

    print("\n================ STUDENT RECORDS ================\n")
    for student in students:
        print("-----------------------------------")
        print("Name    :", student['name'])
        print("Roll No :", student['roll'])
        print("Marks   :", student['marks'])
        print("Total   :", student['total'])
        print("Average :", round(student['average'], 2))
        print("Grade   :", student['grade'])
    print("-----------------------------------\n")


# ---------------- SEARCH STUDENT ----------------

def search_student():
    roll = input("Enter Roll Number to search: ")

    for student in students:
        if student['roll'] == roll:
            print("\nStudent Found:")
            print(student)
            return

    print("❌ Student not found.\n")


# ---------------- CLASS STATISTICS ----------------

def class_statistics():
    if not students:
        print("No students available.\n")
        return

    total_students = len(students)
    class_average = sum(s['average'] for s in students) / total_students

    highest = max(students, key=lambda x: x['total'])
    lowest = min(students, key=lambda x: x['total'])

    print("\n========== CLASS STATISTICS ==========")
    print("Total Students :", total_students)
    print("Class Average  :", round(class_average, 2))
    print("Highest Scorer :", highest['name'], "-", highest['total'])
    print("Lowest Scorer  :", lowest['name'], "-", lowest['total'])
    print("======================================\n")


# ---------------- SORT BY TOTAL ----------------

def sort_students():
    if not students:
        print("No students available.\n")
        return

    sorted_list = sorted(students, key=lambda x: x['total'], reverse=True)

    print("\n====== STUDENTS SORTED BY TOTAL (High to Low) ======\n")
    for student in sorted_list:
        print(student['name'], "- Total:", student['total'])
    print("\n")


# ---------------- UPDATE MARKS ----------------

def update_marks():
    roll = input("Enter Roll Number to update: ")

    for student in students:
        if student['roll'] == roll:
            print("Enter new marks:")
            new_marks = []
            for i in range(1, 6):
                mark = float(input(f"Subject {i}: "))
                new_marks.append(mark)

            student['marks'] = new_marks
            student['total'] = sum(new_marks)
            student['average'] = student['total'] / 5
            student['grade'] = calculate_grade(student['average'])

            save_students()
            print("✅ Marks Updated Successfully!\n")
            return

    print("❌ Student not found.\n")


# ---------------- GRADE DISTRIBUTION ----------------

def grade_distribution():
    grades = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}

    for student in students:
        grades[student['grade']] += 1

    print("\n------ GRADE DISTRIBUTION ------")
    for grade, count in grades.items():
        print(grade, ":", count)
    print("--------------------------------\n")


# ---------------- MAIN MENU ----------------

while True:

    print("======== Student Record Management System ========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Class Statistics")
    print("5. Sort Students by Total Marks")
    print("6. Update Student Marks")
    print("7. Grade Distribution")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        class_statistics()
    elif choice == '5':
        sort_students()
    elif choice == '6':
        update_marks()
    elif choice == '7':
        grade_distribution()
    elif choice == '8':
        print("Exiting Program... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")