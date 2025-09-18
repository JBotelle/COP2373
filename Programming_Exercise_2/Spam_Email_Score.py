
# Joe Botelle
# Programming Exercise 2: Spam Email Score Calculator

# This program analyzes email messages to detect potential spam. It utilizes a fixed list
# containing 30 common spam keywords and phrases. Program asks the user for to either type a message or
# open a .txt file to scan the message. Program then counts the keyword matches, and calculates a score.
# The score and matched keywords are then displayed for the user.

import string
import os


# Count number of keywords in message and return list
def calculate_spam_score(message, spam_keywords):

    # initialize accumulator for score
    score = 0
    # list to store keywords found in the message
    matched_keywords = []

    # Loop through each keyword and check if it's in message
    for keyword in spam_keywords:
        if keyword in message:
            score += 1
            matched_keywords.append(keyword)
    return score, matched_keywords


# Calculate the spam score
def rate_spam(score):
    # Rate likelihood message is spam based on score.
    if score == 0:
        return "Low"
    elif score <= 5:
        return "Medium"
    elif score <= 10:
        return "High"
    else:
        return "Very High"


# Let user select .txt file from current folder
def get_message_from_file():

    # Scan current directory for .txt files
    txt_files = [f for f in os.listdir() if f.endswith(".txt")]

    # exit if no .txt files are found
    if not txt_files:
        print("No text files found ")
        return None

    while True:
        # Display numbered list of files available
        print("\nAvailable .txt files found in this folder ")
        for i, filename in enumerate(txt_files, start=1):
            print(f"{i}. {filename}")
        print("0. Cancel and return to main menu ")

        choice = input("Select a file by number: ")
        if choice == "0":
            return None

        try:
            index = int(choice)
            selected_file = txt_files[index - 1]
            with open(selected_file, "r", encoding="utf-8") as file:
                return file.read()
        except (ValueError, IndexError):
            print("Invalid input. Try again.")



# User message selection and manual entry
def get_message_input():

    # Prompt user to read for files or type in message.
    while True:
        print("\nChoose input method by number: ")
        print("1. Type message manually")
        print("2. Select a .txt file from this folder")

        # If 1, prompt user for message. If 2, call get_message_from_file.
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            return input("\nEnter your message:\n")
        elif choice == "2":
            message = get_message_from_file()

            if message is not None:
                return message
        else:
            print("Invalid input. Please enter 1 or 2. ")

# Main Function
def main():

    # Create spam keyword list
    spam_keywords = ["Prize", "Miracle", "Guaranteed", "Giveaway", "Passwords",
                     "Be your own boss", "Unsolicited", "Million", "Billion", "Notspam",
                     "Cents on the dollar", "Consolidate debt", "Promise", "Earn extra cash",
                     "Earn money", "Eliminate bad credit", "Extra cash", "Extra income",
                     "Expect to earn", "Cash", "Financial freedom", "Free access", "Free consultation",
                     "Gift", "Free", "Instant", "Urgent", "Winner",
                     "Free money"]

    # Get message from user or file
    message = get_message_input()

    #remove punctuation and make lower
    normalized = message.lower().translate(str.maketrans('', '', string.punctuation))
    normalized_keywords = [kw.lower().translate(str.maketrans('', '', string.punctuation)) for kw in spam_keywords]

    # Calculate score
    score, matched_keywords = calculate_spam_score(normalized, normalized_keywords)

    # Rate spam likelihood
    rating = rate_spam(score)

    # Display results
    print("_" * 25)
    print("\n---Spam Grading---\n")
    print("Zero matches is low\n"
          "1-5 matches is moderate\n"
          "6-10 matches is high\n"
          "Above 10 is very high\n")
    print("_" * 25)
    print("\n---Spam Analysis")
    print(f"Your message came back with a score of {score} \n"
          f"and the likelihood of spam is {rating}")
    print("Matched keywords are: ")
    for kw in matched_keywords:
        print(f"\t{kw}")

if __name__ == "__main__":
    main()