# Joe Botelle COP2373 PROGRAMMING EXERCISE 1
# This application allows pre-sell of 20 tickets and
# maximum purchase of 4 tickets per transaction

# Handles purchase logic
def ticket_logic(tickets):
    try:
        purchase = int(input(f"{tickets} tickets remaining.\nHow many tickets would you like (max 4)? "))
        if purchase < 1 or purchase > 4:
            print("Please enter a number between 1 and 4.")
            return tickets, False
        if purchase <= tickets:
            tickets -= purchase
            print(f"{tickets} tickets remaining.")
            return tickets, True
        else:
            print(f"Only {tickets} tickets remaining. Please try a smaller number.")
            return tickets, False
    except ValueError:
        print("Please enter a valid number.")
        return tickets, False

# Displays final summary
def display_summary(buyer_count):
    print("\nAll tickets sold.")
    print(f"Total number of buyers: {buyer_count}")

# Main function
def main():
    tickets = 20
    buyer_count = 0
    while tickets > 0:
        tickets, success = ticket_logic(tickets)
        if success:
            buyer_count += 1
    display_summary(buyer_count)

# Start the program
if __name__ == "__main__":
    main()