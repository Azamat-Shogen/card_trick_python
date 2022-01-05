class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.card = []

    def create(self):
        self.card.append(['┌─────────┐'])
        self.card.append([f'│ {self.rank}       │'])
        self.card.append(['│         │'])
        self.card.append([f'│    {self.suit}    │'])
        self.card.append(['│         │'])
        self.card.append([f'│       {self.rank} │'])
        self.card.append(['└─────────┘'])
        return self.card
