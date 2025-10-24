# main.py
# Student Grade Calculator


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def main():
    print("=== Student Grade Calculator ===")
    name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))

    marks = []
    for i in range(num_subjects):
        mark = float(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / num_subjects
    grade = calculate_grade(average)

    print("\n--- Result ---")
    print(f"Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
