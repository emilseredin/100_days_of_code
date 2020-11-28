import random
from card import Card


class Player:
    shoe = [
        Card('2'),
        Card('3'),
        Card('4'),
        Card('5'),
        Card('6'),
        Card('7'),
        Card('8'),
        Card('9'),
        Card('10'),
        Card('J'),
        Card('Q'),
        Card('K'),
        Card('A')
    ]

    def __init__(self, dealer=False):
        self.cards = []
        self.score = 0
        if dealer:
            self.deal()
        else:
            self.deal(2)

    def deal(self, num=1):
        for i in range(num):
            new_card = random.choice(Player.shoe)
            self.cards.append(new_card)
            self.calculate_score()

    def calculate_score(self):
        cards = sorted(self.cards, key=lambda card: card.value)
        score = 0
        for card in cards:
            if card.value == 11 and score + card.value > 21:
                score = score + 1
            else:
                score = score + card.value
        self.score = score

    def get_cards(self):
        return [card.face for card in self.cards]
