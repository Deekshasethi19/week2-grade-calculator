# ==================================================
# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures
# Name: Deeksha Sethi
# 
# Features:
# 1. Grade Calculation
# 2. Input Validation
# 3. Class Statistics
# 4. Student Search
# 5. Save Results to File
# ==================================================


# --------------------------------------------------
# Function to calculate grade and comment
# --------------------------------------------------
def calculate_grade(average_marks):
    """Calculate grade and return comment"""

    if average_marks >= 90:
        return "A", "Excellent! Keep up the great work!"

    elif average_marks >= 80:
        return "B", "Very Good! You're doing well."

    elif average_marks >= 70:
        return "C", "Good. Room for improvement."

    elif average_marks >= 60:
        return "D", "Needs Improvement. Please study more."

    else:
        return "F", "Failed. Please seek help from teacher."


# --------------------------------------------------
# Function to validate marks input
# --------------------------------------------------
def get_valid_marks(prompt_message):
    """Get valid marks between 0 and 100"""

    while True:

        try:
            marks = float(input(prompt_message))

            if 0 <= marks <= 100:
                return marks

            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


# --------------------------------------------------
# Function to search student
# --------------------------------------------------
def search_student(student_records):
    """Search student by name"""

    search_name = input("\nEnter student name to search: ")

    student_found = False

    for record in student_records:

        if record["student_name"].lower() == search_name.lower():

            print("\nStudent Found")
            print("-" * 40)

            print("Name:", record["student_name"])
            print("Marks:", record["subject_marks"])
            print("Average:", round(record["average_marks"], 2))
            print("Grade:", record["grade"])
            print("Comment:", record["performance_comment"])

            student_found = True
            break

    if not student_found:
        print("Student not found.")


# --------------------------------------------------
# Function to save results in text file
# --------------------------------------------------
def save_results_to_file(student_records):
    """Save student results to a file"""

    with open("student_results.txt", "w") as results_file:

        results_file.write("STUDENT GRADE REPORT\n")
        results_file.write("=" * 50 + "\n\n")

        for record in student_records:

            results_file.write(
                f"Name: {record['student_name']}\n"
            )

            results_file.write(
                f"Marks: {record['subject_marks']}\n"
            )

            results_file.write(
                f"Average: {record['average_marks']:.2f}\n"
            )

            results_file.write(
                f"Grade: {record['grade']}\n"
            )

            results_file.write(
                f"Comment: {record['performance_comment']}\n"
            )

            results_file.write("-" * 50 + "\n")

    print("\nResults saved successfully in student_results.txt")


# --------------------------------------------------
# Main Function
# --------------------------------------------------
def main():

    print("=" * 60)
    print("          STUDENT GRADE CALCULATOR")
    print("=" * 60)

    # Input validation for number of students
    while True:

        try:
            total_students = int(
                input("\nEnter number of students: ")
            )

            if total_students > 0:
                break

            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Invalid input! Enter a whole number.")

    # List to store all student records
    student_records = []

    # ------------------------------------------
    # Collect student data
    # ------------------------------------------
    for student_number in range(total_students):

        print(f"\n===== STUDENT {student_number + 1} =====")

        student_name = input("Enter student name: ")

        while student_name.strip() == "":
            print("Name cannot be empty.")
            student_name = input("Enter student name: ")

        print("\nEnter marks (0-100)")

        mathematics_marks = get_valid_marks(
            "Mathematics: "
        )

        science_marks = get_valid_marks(
            "Science: "
        )

        english_marks = get_valid_marks(
            "English: "
        )

        subject_marks = [
            mathematics_marks,
            science_marks,
            english_marks
        ]

        average_marks = (
            sum(subject_marks) / len(subject_marks)
        )

        grade, performance_comment = (
            calculate_grade(average_marks)
        )

        student_record = {
            "student_name": student_name,
            "subject_marks": subject_marks,
            "average_marks": average_marks,
            "grade": grade,
            "performance_comment": performance_comment
        }

        student_records.append(student_record)

    # ------------------------------------------
    # Display Results
    # ------------------------------------------
    print("\n")
    print("=" * 95)
    print("RESULTS SUMMARY")
    print("=" * 95)

    print(
        f"{'Name':<15} {'Average':<10} {'Grade':<8} Comment"
    )

    print("-" * 95)

    for record in student_records:

        print(
            f"{record['student_name']:<15}"
            f"{record['average_marks']:<10.1f}"
            f"{record['grade']:<8}"
            f"{record['performance_comment']}"
        )

    # ------------------------------------------
    # Class Statistics
    # ------------------------------------------
    average_marks_list = []

    for record in student_records:
        average_marks_list.append(
            record["average_marks"]
        )

    class_average = (
        sum(average_marks_list)
        / len(average_marks_list)
    )

    highest_average = max(average_marks_list)
    lowest_average = min(average_marks_list)

    highest_index = average_marks_list.index(
        highest_average
    )

    lowest_index = average_marks_list.index(
        lowest_average
    )

    print("\n")
    print("=" * 60)
    print("CLASS STATISTICS")
    print("=" * 60)

    print(f"Total Students : {total_students}")
    print(f"Class Average  : {class_average:.2f}")

    print(
        f"Highest Average: {highest_average:.2f} "
        f"({student_records[highest_index]['student_name']})"
    )

    print(
        f"Lowest Average : {lowest_average:.2f} "
        f"({student_records[lowest_index]['student_name']})"
    )

    # ------------------------------------------
    # Search Feature
    # ------------------------------------------
    search_student(student_records)

    # ------------------------------------------
    # Save Results
    # ------------------------------------------
    save_results_to_file(student_records)

    print("\nThank you for using the program!")


# --------------------------------------------------
# Program Entry Point
# --------------------------------------------------
if __name__ == "__main__":
    main()