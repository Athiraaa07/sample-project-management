# main.py
# Student Grade Calculator with input validation for marks

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

    
    while True:
        try:
            num_subjects = int(input("Enter number of subjects: "))
            if num_subjects > 0:
                break
            else:
                print("Number of subjects must be positive.")
        except ValueError:
            print("Please enter a valid integer.")

    marks = []
    for i in range(num_subjects):
        while True:
            try:
                mark = float(input(f"Enter mark for subject {i+1}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Mark must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    average = round(total / num_subjects, 2)
    grade = calculate_grade(average)

    print("\n--- Result ---")
    print(f"Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
