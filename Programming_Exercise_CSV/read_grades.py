# Joe Botelle
# Programming Exercise: CSV (Program 2 of 2)

# This program opens grades.csv, displays results in a table and gives user the option to
# reopen write_grades.py

import csv
import sys
import subprocess
import os

# yes/no validation for user questions.  Three failed attempts exits program
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

# Opens grades.csv and displays in a table. User has option to open write_grades.py to write, edit or delete records.
def read_grades():

    # Checks if the file exists. If not, asks if user wants to switch to write_grades.py
    if not os.path.exists('grades.csv'):
        print("grades.csv does not exist. Please enter grades first.")
        if get_yes_no("Do you wish to continue? y/n: "):
            try:
                subprocess.run(["python", "write_grades.py"], check=True)
            except FileNotFoundError:
                print("Error: write_grades.py could not be found.")
                sys.exit()
            except subprocess.CalledProcessError:
                print("Error: write_grades.py could not be executed.")
                sys.exit()
        sys.exit()

    # Opens the csv file and
    try:
        with open("grades.csv", mode="r") as file:
            reader = csv.DictReader(file)

            # Define the column headers and widths for table.
            headers = ["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3", "AVG %"]
            col_widths = [25, 25, 10, 10, 10, 10]

            # Build the border
            border = "+" + "+".join("-" * w for w in col_widths) + "+"
            print(border)
            header_row = "|" + "|".join(f"{h:<{w}}" for h, w in zip(headers, col_widths)) + "|"
            print(header_row)
            print(border)

            rows_printed = False
            # Inside the loop where each row is printed
            for row in reader:
                rows_printed = True

                # Calculate average percentage
                try:
                    exam1 = int(row["Exam 1"])
                    exam2 = int(row["Exam 2"])
                    exam3 = int(row["Exam 3"])
                    avg = round((exam1 + exam2 + exam3) / 3, 2)
                except (ValueError, KeyError):
                    avg = 0.0

                # Build the row
                values = [
                    row["First Name"],
                    row["Last Name"],
                    row["Exam 1"],
                    row["Exam 2"],
                    row["Exam 3"],
                    f"{avg:.2f}%"
                ]
                data_row = "|" + "|".join(f"{v:<{w}}" for v, w in zip(values, col_widths)) + "|"
                print(data_row)

            # If no rows, print centered "No Data Message"
            if not rows_printed:
                print("|" + "No data found in grades.csv".center(sum(col_widths), " ") + "|")
            print(border)

    except FileNotFoundError:
        print("grades.csv does not exist. Please enter grades first.")
        sys.exit()

    if get_yes_no("Would you like to re-enter grades? y/n: "):
        try:
            subprocess.run(["python", "write_grades.py"], check = True)
        except FileNotFoundError:
            print("Error: write_grades.py could not be found.")
            sys.exit()
        except subprocess.CalledProcessError:
            print("Error: write_grades.py could not be executed.")
            sys.exit()

def main():
    read_grades()

if __name__ == "__main__":
    main()