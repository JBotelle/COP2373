import random  # Used to shuffle the deck and deal random cards

# Represents a playing card with a suit and rank
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # Returns a readable string
    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Builds and shuffles a full deck of 52 cards
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        # Shuffle the deck
        random.shuffle(self.cards)

    # Deals one card
    def deal_card(self):
        return self.cards.pop()

# Deals a hand of 5 cards
def deal_hand(deck, hand_size=5):
    return [deck.deal_card() for _ in range(hand_size)]

# Replace selected cards in the hand with new ones from the deck
def replace_cards(deck, hand, indices_to_replace):
    for index in indices_to_replace:
        hand[index] = deck.deal_card()
    return hand

# Gets and validates user input for which cards to replace
def get_valid_replacements():
    while True:
        raw = input("\nEnter up to 3 card numbers to replace (e.g., 1, 3, 5): ").strip()
        if not raw:
            # No input means no replacement cards
            return []

        parts = [x.strip() for x in raw.split(",")]
        if len(parts) > 3:
            print("You can only replace up to 3 cards.")
            continue

        try:
            # Prevent duplicate entries or entries out of range
            indices = []
            for part in parts:
                if not part.isdigit():
                    raise ValueError
                num = int(part)
                if num < 1 or num > 5:
                    raise ValueError
                if num - 1 in indices:
                    raise ValueError
                indices.append(num - 1)
            return indices
        except ValueError:
            print("Invalid input. Please enter up to 3 unique numbers between 1 and 5.")

# Builds a visual representation of a single card
def display_card(card):
    rank = card.rank
    suit = card.suit

    # Top label: left-aligned card number
    rank_top = f"{rank:<11}"[:11]

    # Center line: suit name centered
    suit_center = f"{suit:^11}"[:11]

    # Bottom label: right-aligned card number
    rank_bot = f"{rank:>11}"[-11:]

    return [
        "+-----------+",
        f"|{rank_top}|",
        "|           |",
        "|           |",
        f"|{suit_center}|",
        "|           |",
        "|           |",
        f"|{rank_bot}|",
        "+-----------+"
    ]

# Displays the full hand of cards with index numbers above each card
def print_hand(hand):
    card_lines = [display_card(card) for card in hand]

    # Width and spacing between cards
    card_width = 13
    spacing = 2
    total_width = (card_width + spacing) * len(hand) - spacing
    padding = max((80 - total_width) // 2, 0)
    pad = " " * padding

    # Print card index numbers
    index_line = [" "] * (padding + total_width)
    for i in range(len(hand)):
        column = padding + i * (card_width + spacing)
        index_line[column] = str(i + 1)
    print("".join(index_line))

    # Print each line of the card layout
    for line_index in range(9):
        print(pad + (" " * spacing).join(card[line_index] for card in card_lines))

# Main Loop
def main():
    print("""
 ____   ___    _  __  _____   ____  
|  _ \\ / _ \\  | |/ / | ____| |  _ \\ 
| |_) | | | | | ' /  |  _|   | |_) |
|  __/| |_| | | . \\  | |___  |  _ < 
|_|    \\___/  |_|\_\\ |_____| |_| \\_\\

    """)

    while True:
        deck = Deck()
        hand = deal_hand(deck)

        print("\nYour initial hand:")
        print_hand(hand)

        indices = get_valid_replacements()
        hand = replace_cards(deck, hand, indices)

        print("\nYour final hand:")
        print_hand(hand)

        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()