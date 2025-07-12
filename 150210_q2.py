class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment, grade):
        self.assignments[assignment] = grade

    def display_grades(self):
        if not self.assignments:
            print("No grades recorded.")
        else:
            for assignment, grade in self.assignments.items():
                print(f"{assignment}: {grade}")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' added.")

    def assign_grade(self, student_id, assignment, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment, grade)
                print(f"Grade {grade} added for {student.name} in '{assignment}'")
                return
        print("Student not found.")

    def display_all_students(self):
        if not self.students:
            print("No students enrolled.")
        else:
            for student in self.students:
                print(f"\n{student.name} ({student.student_id})")
                student.display_grades()


if __name__ == "__main__":
    instructor_name = input("Instructor name: ")
    course_name = input("Course name: ")
    instructor = Instructor(instructor_name, course_name)

    while True:
        print("\nMenu:")
        print("1. Add student")
        print("2. Assign grade")
        print("3. Display student grades")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("Student name: ")
            student_id = input("Student ID: ")
            instructor.add_student(Student(name, student_id))

        elif choice == "2":
            student_id = input("Student ID: ")
            assignment = input("Assignment name: ")
            try:
                grade = float(input("Grade: "))
                instructor.assign_grade(student_id, assignment, grade)
            except:
                print("Invalid grade input.")

        elif choice == "3":
            instructor.display_all_students()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option.")
