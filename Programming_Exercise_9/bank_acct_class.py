# Joe Botelle
# Programming Exercise 9

# This program showcases a mock bank account class and sample output



class BankAcct:
    def __init__(self, name, acct_num, amount=0.0, interest_rate=0.01):
        self.name = name
        self.acct_num = acct_num
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)

    # Adjust the annual interest rate
    def adjust_interest_rate(self, new_rate):
        if new_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self.interest_rate = new_rate

    # Deposit money into the account
    def deposit(self, amt):
        if amt <= 0:
            raise ValueError("Deposit must be positive.")
        self.amount += amt

    # Withdraw money from the account
    def withdrawl(self, amt):
        if amt <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amt > self.amount:
            raise ValueError("Insufficient funds.")
        self.amount -= amt

    # Apply interest for a given number of days and update the balance
    def apply_interest(self, days):
        if days < 0:
            raise ValueError("Days cannot be negative.")
        interest = self.amount * self.interest_rate * (days / 365)
        self.amount += interest
        return interest

    # Return a string representation of the account
    def __str__(self):
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.acct_num}\n"
                f"Balance: ${self.amount:,.2f}\n"
                f"Interest Rate: {self.interest_rate * 100:.2f}%")



def test_bank_acct():
    acct = BankAcct("Reagan Wilson", "147953", 986.47, 0.05)

    # Opening state
    print("Opening Account State:")
    print(acct, "\n")
    input("Press Enter to continue...")

    # Deposit and withdrawl at 5%
    print("Depositing $488.14...")
    acct.deposit(488.14)
    print(acct, "\n")
    input("Press Enter to continue...")

    print("Withdrawing $200...")
    acct.withdrawl(200)
    print(acct, "\n")
    input("Press Enter to continue...")

    # Period close at 5%
    print("Closing period at 5% interest...")
    interest = acct.apply_interest(30)
    print(f"Interest accrued: ${interest:,.2f}")
    print("Final Balance for the Period:")
    print(acct, "\n")
    input("Press Enter to continue...")

    # Change interest rate
    print("Interest rate has changed from 5% to 7%.\n")
    acct.adjust_interest_rate(0.07)
    input("Press Enter to continue...")

    # Deposit and withdrawl at 7%
    print("Depositing $781.22...")
    acct.deposit(781.22)
    print(acct, "\n")
    input("Press Enter to continue...")

    print("Withdrawing $389.35...")
    acct.withdrawl(389.35)
    print(acct, "\n")
    input("Press Enter to continue...")

    # Period close at 7%
    print("Closing period at 7% interest...")
    interest = acct.apply_interest(30)
    print(f"Interest accrued: ${interest:,.2f}")
    print("Final Balance for the Period:")
    print(acct, "\n")

# Run test if file is executed directly
if __name__ == "__main__":
    test_bank_acct()