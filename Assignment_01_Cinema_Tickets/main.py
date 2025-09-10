# Joe Botelle COP2373 PROGRAMMING EXERCISE 1
# This application allows pre-sell of 20 tickets and
# maximum purchase of 4 tickets per transaction

# Handles purchase logic
def ticket_logic(tickets):
    # Set ticket count to 20 and create accumulator for buyers
    buyer_counter = 0

    # Loop until tickets are sold
    while tickets > 0:
        try:
            # Ask how many tickets
            purchase = int(input(f"You looking for tickets?  I got some... (max 4)? "))
            # Validate purchase request
            if purchase < 1 or purchase > 4:
                # User input out of range
                print("Don't be greedy. Please enter a number between 1 and 4.")
                continue
            if purchase <= tickets:
                # Valid purchase. Subtract and confirm
                tickets -= purchase
                print(f"{tickets} tickets remaining. Who else wants to buy some tickets?")
                # If successful, increase buyer count
                buyer_counter += 1
            else:
                # User asked for more than available
                print(f"Sorry my dude... There's only {tickets} tickets remaining. Please try a smaller number.")
        except ValueError:
            # User entered not a number.
            print("Please enter a valid number.")

    # return buyer count after loop ends
    return buyer_counter

# Displays final summary
def display_summary(buyer_counter):
    # Print total number of buyers after all tickets are sold
    print(f"\nAll tickets sold.")
    print(f"Total number of buyers: {buyer_counter}")

# Main Function
def main():
    # Call purchase function for buyer count
    buyer_counter = ticket_logic(10)
    # Display final summary
    display_summary(buyer_counter)

# Start the program
if __name__ == "__main__":
    main()