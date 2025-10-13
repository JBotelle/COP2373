# Joe Botelle
# Programming Exercise 7

# This program takes users paragraph, breaks them into individual sentences,
# then displays them and gives user the total count.

import re

COMMON_ABBREVIATIONS = {"Mr.", "Mrs.", "Ms.", "Dr.", "Prof.", "etc.", "e.g.", "i.e."}

# Prompts user to enter paragraph, ensures input isn't empty before returning it.
# If user enters less than a sentence three times, return None
def get_paragraph():
    attempts = 0
    while attempts < 3:
        paragraph = input("\nPlease enter a paragraph:\n").strip()
        if paragraph:
            return paragraph
        else:
            attempts += 1
            print("Invalid input. Please type at least one sentence.")

    # If we reach here, user failed three times
    print("\nToo many invalid attempts. Please try again later.")
    return None


# Split paragraph into sentences and display with a count regardless of letters or numbers.
def process_sentences(paragraph):

    try:
        # Regex: split after punctuation (.!?), followed by whitespace,
        # and ensure the next sentence starts with a capital letter or a digit.
        sentence_pattern = r'(?<=[.!?])\s+(?=[A-Z0-9])'
        raw_sentences = re.split(sentence_pattern, paragraph.strip())

        sentences = []
        for part in raw_sentences:
            part = part.strip()
            if sentences:
                last = sentences[-1]
                # If the last sentence ends with a known abbreviation, merge
                if any(last.endswith(abbrev) for abbrev in COMMON_ABBREVIATIONS):
                    sentences[-1] = last + " " + part
                    continue
            sentences.append(part)

        print("\nHere are the sentences I found:")
        for i, sentence in enumerate(sentences, start=1):
            print(f"{i}. {sentence}")

        print(f"\nTotal number of sentences: {len(sentences)}")

    except Exception as e:
        print(f"An error occurred while processing: {e}")


# Main Function
def main():
    # Welcome user and setup loop for main function
    print("Hello, welcome to the Sentence Analyzer.")
    print("This program will break your paragraph into individual sentences and give you a count.\n")

    # Setup loop and call functions
    while True:
        paragraph = get_paragraph()
        if paragraph is None:
            break # Exit after too many invalid attempts


        process_sentences(paragraph)

        # Retry system with three try rule before force exit.
        attempts = 0
        while attempts < 3:
            choice = input("\nWould you like to try another paragraph? (y/n): ").strip().lower()
            if choice in ("y", "yes"):
                break
            if choice in ("n", "no"):
                print("\nThank you for using the Sentence Splitter. Goodbye.")
                return
            attempts += 1
            print("Invalid input. Please type 'y' or 'n'.")

        if attempts == 3:
            print("\nToo many invalid responses. Please try again later.")
            return


if __name__ == "__main__":
    main()
