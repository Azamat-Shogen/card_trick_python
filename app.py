import time
from card_game.deck import Deck


def valid_input_check(input_val):
    try:
        if int(input_val) < 1 or int(input_val) > 3:
            return False
    except ValueError:
        print("Invalid input")
    else:
        return True


# TODO: GAME LOOP
def play_game():
    deck = Deck()
    deck.initial_deck_setup()
    deck.shuffle_deck()

    print("\nHello adventurer! Please pick one card, and I'm going to try to guess it.\n"
          "But i need a little help from you.")

    time.sleep(1)
    deck.display_deck()

    # todo: run 3 rounds
    for i in range(1, 4):
        while True:
            print(f"Round {i}")
            input_value = input(f"Please enter the row number your card is in. 1 or 2 or 3: ")
            if valid_input_check(input_value):
                break
            print("Please enter an integer value only (1, 2, 3) for corresponding row\n")

        deck.mix_cards(input_value)
        deck.display_deck()

    # Todo: reveal guessed card
    while True:
        print("_" * 40)
        deck.reveal_card(29)
        card_guessed = input("Found your card! Is this your card? Y/N ").lower()

        if card_guessed == "y":
            break
        elif card_guessed == "n":
            deck.reveal_card(6)
            print("Here is your card then!")
            break
        else:
            print("Invalid Input. Please type Y for yes , N for no ")

    print("-" * 40)
    print(f"Thanks for playing adventurer.")
    time.sleep(1)
    print("*** Game Over ***")


play_game()