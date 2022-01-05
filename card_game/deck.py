import random
from .card import Card


class Deck:
    row = 12  # constant class variable

    def __init__(self):
        self.cards = []
        self.ranks = ["5", "6", "7", "8", "9", "J", "Q", "K", "A"]
        self.suits = ["♦", "♥", "♠", "♣"]

    def initial_deck_setup(self):
        temp_cards = []
        for rank in self.ranks:
            for suit in self.suits:
                temp_cards.append(Card(rank, suit))
        new_deck = list(map(lambda card: card.create(), temp_cards))
        self.set(new_deck)

    def shuffle_deck(self):
        random.shuffle(self.cards)

    @staticmethod
    def get_row(arr, start, end):
        return [arr[i] for i in range(start, end)]

    @staticmethod
    def display_row(arr):
        current = 0
        while current < len(arr[0]):  # this is the length of a single card list (7)
            for el in arr:
                print(el[current][0], end="")
            print()
            current += 1

    def display_deck(self):
        Deck.display_row(self.get_row(self.cards, 0, Deck.row))
        Deck.display_row(self.get_row(self.cards, Deck.row, Deck.row * 2))
        Deck.display_row(self.get_row(self.cards, Deck.row * 2, Deck.row * 3))

    def get(self):
        return self.cards

    def set(self, new_deck):
        self.cards = new_deck

    # TODO: Mix cards up logic
    def mix_cards(self, input_row_number):
        temp_arr = []
        if input_row_number == "1":
            temp_arr.append(Deck.get_row(self.cards, Deck.row, Deck.row * 2))
            temp_arr.append(Deck.get_row(self.cards, 0, Deck.row))
            temp_arr.append(Deck.get_row(self.cards, Deck.row * 2, Deck.row * 3))
        elif input_row_number == "2":
            temp_arr.append(Deck.get_row(self.cards, 0, Deck.row))
            temp_arr.append(Deck.get_row(self.cards, Deck.row, Deck.row * 2))
            temp_arr.append(Deck.get_row(self.cards, Deck.row * 2, Deck.row * 3))
        else:
            temp_arr.append(Deck.get_row(self.cards, 0, Deck.row))
            temp_arr.append(Deck.get_row(self.cards, Deck.row * 2, Deck.row * 3))
            temp_arr.append(Deck.get_row(self.cards, Deck.row, Deck.row * 2))

        flat_list = [item for sublist in temp_arr for item in sublist]
        new_deck = []

        for i in range(0, 34, 3):
            new_deck.append(flat_list[i])
        for i in range(1, 35, 3):
            new_deck.append(flat_list[i])
        for i in range(2, 36, 3):
            new_deck.append(flat_list[i])

        self.set(new_deck)

    def reveal_card(self, index):
        for row in self.cards[index]:
            print(row[0])
