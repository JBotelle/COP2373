# Joe Botelle
# Programming Exercise 3 Budget Summary

# This program asks user for an expense and its monthly amount.
# Program uses reduce to calculate total, highest and lowest expenses.

from functools import reduce
import textwrap

# Prompt user to enter expense type and amounts
def get_expenses():
    expenses = []
    print("\n" + "-" * 40)
    print("Enter your monthly expenses.")
    print("Type 'done' when finished.")
    print("-" * 40 + "\n")

    # Validate entry
    while True:
        print("\n--- New Expense Entry ---")
        expense_type = input("Expense type: ").strip()
        if expense_type.lower() == 'done':
            break
        if not expense_type:
            print("Expense type cannot be empty.")
            continue
        # Nested loop, to go back to expense type and validate entry
        while True:
            print()
            amount_input = input(f"Amount for {expense_type} ('back' to cancel): ").strip()
            if amount_input.lower() == 'back':
                break
            try:
                amount = float(amount_input)
                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue
                expenses.append((expense_type, amount))
                break
            except ValueError:
                print("Invalid amount. Please enter a number or 'back'.")
    return expenses


# Use reduce to calculate total, highest and lowest expenses
def analyze_expenses(expenses):
    total = reduce(lambda acc, x: acc + x[1], expenses, 0)
    highest = reduce(lambda a, b: a if a[1] > b[1] else b, expenses)
    lowest = reduce(lambda a, b: a if a[1] < b[1] else b, expenses)
    return total, highest, lowest


# Display the expenses in a formatted table and print summary stats
def display_results(expenses, total, highest, lowest):
    print("\n+-----------------------------------+--------------------+")
    print("| Expense Type                        | Amount ($)       |")
    print("+-------------------------------------+------------------+")
    for etype, amount in expenses:
        wrapped_lines = textwrap.wrap(etype, width=35)
        for i, line in enumerate(wrapped_lines):
            if i == 0:
                print(f"| {line.ljust(35)} | {f'{amount:.2f}'.rjust(10)}       |")
            else:
                print(f"| {line.ljust(35)} | {'':>10} |")
    print("+-----------------------------------+--------------------+")

    print("\n--- Summary ---")
    print(f"Total Expense: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} ${lowest[1]:.2f}")


# Main function
def main():
    expenses = get_expenses()
    if not expenses:
        print("No expenses entered. Exiting.")
        return
    total, highest, lowest = analyze_expenses(expenses)
    display_results(expenses, total, highest, lowest)


if __name__ == "__main__":
    main()