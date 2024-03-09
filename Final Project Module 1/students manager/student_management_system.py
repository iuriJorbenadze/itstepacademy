
import json

class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

class StudentList:
    def __init__(self):
        self.students = []
        self.load_students()

    def load_students(self):
        # Load student data from a file if it exists
        try:
            with open('students.json', 'r') as f:
                data = json.load(f)
                self.students = [Student(student['name'], student['roll_number'], student['grade']) for student in data]
        except FileNotFoundError:
            pass  # It's okay if the file doesn't exist; we'll start with an empty list

    def save_students(self):
        # Save current list of students to a file
        with open('students.json', 'w') as f:
            json.dump([student.__dict__ for student in self.students], f)

    def add_student(self, name, roll_number, grade):
        # Validate the input before adding a student
        if grade not in ["A", "B", "C", "D", "E", "F"]:
            print("Invalid grade. Grade should be one of: A, B, C, D, E, F")
            return
        
        if any(student.roll_number == roll_number for student in self.students):
            print(f"Student with roll number {roll_number} already exists.")
            return

        self.students.append(Student(name, roll_number, grade))
        self.save_students()
        print("Student added successfully!")

    def view_all_students(self):
        # Display all students in the list
        for student in self.students:
            print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")

    def search_student_by_roll_number(self, roll_number):
        # Search for a student by roll number
        for student in self.students:
            if student.roll_number == roll_number:
                print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")
                return
        print("Student not found!")

    def update_grade(self, roll_number, new_grade):
        # Update the grade of a student by roll number
        if new_grade not in ["A", "B", "C", "D", "E", "F"]:
            print("Invalid grade. Grade should be one of: A, B, C, D, E, F")
            return

        found_student = next((student for student in self.students if student.roll_number == roll_number), None)
        if not found_student:
            print(f"No student found with roll number {roll_number}.")
            return

        found_student.grade = new_grade
        self.save_students()
        print("Grade updated successfully.")

def main():
    student_system = StudentList()

    while True:
        print("\nMenu:")
        print("1. Add new student")
        print("2. View all students")
        print("3. Search student by roll number")
        print("4. Update student grade")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            roll_number = input("Enter roll number: ")
            grade = input("Enter grade: ")

            # Validate roll number is an integer
            try:
                roll_number = int(roll_number)
                student_system.add_student(name, roll_number, grade)
            except ValueError:
                print("Roll number must be an integer.")
        elif choice == "2":
            student_system.view_all_students()
        elif choice == "3":
            try:
                roll_number = int(input("Enter roll number to search: "))
                student_system.search_student_by_roll_number(roll_number)
            except ValueError:
                print("Roll number must be an integer.")
        elif choice == "4":
            try:
                roll_number = int(input("Enter roll number to update grade: "))
                new_grade = input("Enter new grade: ")
                student_system.update_grade(roll_number, new_grade)
            except ValueError:
                print("Roll number must be an integer.")
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
