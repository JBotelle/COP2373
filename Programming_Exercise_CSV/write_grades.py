# Joe Botelle
# Programming Exercise: CSV

# This program collects student grade data and writes it to grades.csv.
# User has option to open read_grades.py to view results in a table.
# There's also a three-try system in place that exits the program after three invalid inputs.

import csv
import sys
import subprocess
import os
import re


# ------------------------------------------------------------------------------------------------------------------
# INPUT VALIDATION FUNCTIONS
# ------------------------------------------------------------------------------------------------------------------

# Prompt user for integer input with range validation. Three failed attempts exits program
def get_int(prompt, min_value=0, max_value=100):
    attempts = 0
    while attempts < 3:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        attempts += 1
    print("I'm sorry, but I don't understand your input. Please try again later.")
    sys.exit()


# Prompt user for yes/no input. Three failed attempts exits program
def get_yes_no(prompt):
    attempts = 0
    while attempts < 3:
        choice = input(prompt).strip().lower()
        if choice in ("y", "ye", "yes"):
            return True
        elif choice in ("n", "no", "nope"):
            return False
        else:
            print("Please enter 'y' or 'n'.")
            attempts += 1
    print("I'm sorry, please try again later.")
    sys.exit()


# Prompt user for name input. Accepts letters, apostrophes, hyphens, and spaces
def get_name(prompt):
    attempts = 0
    pattern = re.compile(r"^[A-Za-z][A-Za-z'\- ]*$")
    while attempts < 3:
        name = input(prompt).strip()
        if pattern.match(name):
            return name
        else:
            print("Please enter a valid name (letters, apostrophes, and hyphens allowed).")
            attempts += 1
    print("I'm sorry, please try again later.")
    sys.exit()


# ------------------------------------------------------------------------------------------------------------------
# INPUT / OUTPUT FUNCTIONS
# ------------------------------------------------------------------------------------------------------------------

# Load grades.csv into a list of dictionaries
def load_grades():
    if not os.path.exists("grades.csv"):
        return []
    try:
        with open("grades.csv", mode="r", newline="") as file:
            reader = csv.DictReader(file)
            expected_fields = ["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"]
            if reader.fieldnames != expected_fields:
                print("There's an issue with grades.csv. Unexpected headers found.")
                return []
            return list(reader)
    except Exception as e:
        print(f"Error: {e}")
        return []


# Save list of dictionaries to grades.csv
def save_grades(data):
    try:
        with open("grades.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print("\ngrades.csv saved.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()


# ------------------------------------------------------------------------------------------------------------------
# DATA FUNCTIONS
# ------------------------------------------------------------------------------------------------------------------

# Display indexed list of students in a bordered table
def display_students(data):
    if not data:
        print("There are no students to display.")
        return

    headers = ["#", "First Name", "Last Name"]
    widths = [4, 25, 25]
    border = "+" + "+".join(["-" * w for w in widths]) + "+"
    header_row = "|" + "|".join(f"{h:^{w}}" for h, w in zip(headers, widths)) + "|"

    print("\n" + border)
    print(header_row)
    print(border)

    for i, row in enumerate(data, start=1):
        values = [str(i), row["First Name"], row["Last Name"]]
        row_line = "|" + "|".join(f"{v:^{w}}" for v, w in zip(values, widths)) + "|"
        print(row_line)

    print(border)


# Add new student records and save after each entry
import re
import sys

def add_students(data):
    # student_count counter is for number of student being added, mismatch_attempts counter for three-try rules.
    student_count = 0
    mismatch_attempts = 0

    while True:
        print(f"\nEntering data for student {student_count + 1} "
              "(press Enter at First and Last Name to finish):")

        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()

        # If both are blank, stop adding students
        if not first_name and not last_name:
            print("Finished adding students. Returning to main menu.")
            break

        # If one is blank but not the other increase mismatch attempt
        if (not first_name and last_name) or (first_name and not last_name):
            mismatch_attempts += 1
            print(f"Both first and last name are required. "
                  f"Invalid attempt {mismatch_attempts}/3.")
            if mismatch_attempts >= 3:
                print("Too many invalid attempts. Exiting program.")
                sys.exit()
            continue  # restart loop

        # Validate names matching regex
        if not re.match(r"^[A-Za-z][A-Za-z'\- ]*$", first_name):
            mismatch_attempts += 1
            print(f"Invalid first name. Invalid attempt {mismatch_attempts}/3.")
            if mismatch_attempts >= 3:
                print("Too many invalid attempts. Exiting program.")
                sys.exit()
            continue

        if not re.match(r"^[A-Za-z][A-Za-z'\- ]*$", last_name):
            mismatch_attempts += 1
            print(f"Invalid last name. Invalid attempt {mismatch_attempts}/3.")
            if mismatch_attempts >= 3:
                print("Too many invalid attempts. Exiting program.")
                sys.exit()
            continue

        # Collect exam scores
        exam_1 = get_int("Exam 1 (0-100): ", 0, 100)
        exam_2 = get_int("Exam 2 (0-100): ", 0, 100)
        exam_3 = get_int("Exam 3 (0-100): ", 0, 100)

        # Append the new student record to the list
        data.append({
            "First Name": first_name,
            "Last Name": last_name,
            "Exam 1": exam_1,
            "Exam 2": exam_2,
            "Exam 3": exam_3
        })

        # Save immediately after each student to prevent data loss
        save_grades(data)
        student_count += 1

        # Reset mismatch counter after a successful save
        mismatch_attempts = 0

# Edit an existing student record
def edit_student(data):
    if not data:
        print("No student records available to edit.")
        return

    display_students(data)
    index = get_int("Enter the number of the student to edit: ", 1, len(data)) - 1
    student = data[index]

    print(f"\nEditing: {student['First Name']} {student['Last Name']}")

    new_first = input(f"First Name [{student['First Name']}] (press Enter to skip): ").strip()
    new_last = input(f"Last Name [{student['Last Name']}] (press Enter to skip): ").strip()

    if new_first:
        if re.match(r"^[A-Za-z][A-Za-z'\- ]*$", new_first):
            student['First Name'] = new_first
        else:
            print("Invalid name. Keeping original.")

    if new_last:
        if re.match(r"^[A-Za-z][A-Za-z'\- ]*$", new_last):
            student['Last Name'] = new_last
        else:
            print("Invalid name. Keeping original.")

    for exam in ["Exam 1", "Exam 2", "Exam 3"]:
        current = student[exam]
        new_score = input(f"{exam} [{current}] (press Enter to skip): ").strip()
        if new_score:
            try:
                score = int(new_score)
                if 0 <= score <= 100:
                    student[exam] = score
                else:
                    print(f"{exam} must be between 0 and 100. Keeping original score.")
            except ValueError:
                print(f"Invalid input for {exam}. Keeping original score.")


# Delete a student record
def delete_student(data):
    if not data:
        print("No student records available to delete.")
        return

    display_students(data)
    index = get_int("Enter the number of the student to delete: ", 1, len(data)) - 1
    student = data[index]

    confirm = get_yes_no(f"Are you sure you want to delete {student['First Name']} {student['Last Name']}? y/n: ")
    if confirm:
        del data[index]
        print("Student record deleted.")
    else:
        print("Canceled.")


# Reset class by clearing all data and overwriting grades.csv
def reset_class():
    confirm = get_yes_no("This will erase all student records. Are you sure? y/n: ")
    if confirm:
        save_grades([])  # Overwrite file with just header
        print("Class has been reset.")
        return []
    else:
        print("Reset canceled.")
        return None


# ------------------------------------------------------------------------------------------------------------------
# MAIN MENu
# ------------------------------------------------------------------------------------------------------------------

def write_grades():
    # Load any existing student data from grades.csv into memory
    data = load_grades()

    # Counter to track invalid menu attempts
    attempts = 0

    # Keep looping until the user chooses to exit
    while True:
        # Display the available menu options
        print("\nMenu:")
        print("1. Add new student(s)")
        print("2. Edit existing student")
        print("3. Delete student")
        print("4. Save and exit")
        print("5. Reset class (overwrite all data)")

        # Ask the user for their menu choice
        choice = input("Select an option (1–5): ").strip()

        # Handle each valid menu option
        if choice == "1":
            add_students(data)
            # reset invalid counter after valid choice
            attempts = 0
        elif choice == "2":
            edit_student(data)
            attempts = 0
        elif choice == "3":
            delete_student(data)
            attempts = 0
        elif choice == "4":
            save_grades(data)

            # After saving, optionally run read_grades.py to display results
            if get_yes_no("Would you like to display the grades now? y/n: "):
                try:
                    subprocess.run(["python", "read_grades.py"], check=True)
                except FileNotFoundError:
                    print("Error: read_grades.py could not be found.")
                    sys.exit()
                except subprocess.CalledProcessError:
                    print("Error: read_grades.py could not be executed.")
                    sys.exit()
            break
        elif choice == "5":
            result = reset_class()
            if result is not None:
                data = result
            attempts = 0
        else:
            # Count invalid attempts and exit after three failures
            attempts += 1
            print("Invalid selection. Please choose 1–5.")
            if attempts >= 3:
                print("Too many invalid attempts. Exiting program.")
                sys.exit()


def main():
    write_grades()

if __name__ == "__main__":
    main()