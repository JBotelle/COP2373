# Joe Botelle COP2373 PROGRAMMING EXERCISE 1
# This application allows pre-sell of 20 tickets and
# maximum purchase of 4 tickets per transaction

# Handles purchase logic
def ticket_logic(tickets):
    # Set ticket count to 20 and create accumulator for buyers
    buyer_count = 0

    # Loop until tickets are sold
    while tickets > 0:
        try:
            # Ask how many tickets
            purchase = int(input(f"How many tickets would you like (max 4)? "))
            # Validate purchase request
            if purchase < 1 or purchase > 4:
                # User input out of range
                print("Please enter a number between 1 and 4.")
                continue
            if purchase <= tickets:
                # Valid purchase. Subtract and confirm
                tickets -= purchase
                print(f"{tickets} tickets remaining.")
                # If successful, increase buyer count
                buyer_count += 1
            else:
                # User asked for more than available
                print(f"Only {tickets} tickets remaining. Please try a smaller number.")
        except ValueError:
            # User entered not a number.
            print("Please enter a valid number.")

    # return buyer count after loop ends
    return buyer_count

# Displays final summary
def display_summary(buyer_count):
    # Print total number of buyers after all tickets are sold
    print(f"\nAll tickets sold.")
    print(f"Total number of buyers: {buyer_count}")

# Main Function
def main():
    # Call purchase function for buyer count
    buyer_count = ticket_logic(20)
    # Display final summary
    display_summary(buyer_count)

# Start the program
if __name__ == "__main__":
    main()