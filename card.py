# ------------------------------------- This is Created by Darshan R Kheni ------------------------------------- #

# ---------------------------------------------------- Enjoy --------------------------------------------------- #

import random


class Card(object):

    def __init__(self, shape, val):
        self.shape = shape
        self.value = val

    def show(self):
        return f'{self.value} of {self.shape}'

class Deck(object):

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ['Spades', 'Clubs', 'Diamond', 'Hearts']:
            for v in range(1,14):
                self.cards.append(Card(s,v).show())

    def show(self):
        for c in self.cards:
            print(c.show())

    def shuffle(self):
        for i in range(len(self.cards)):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    # it is temporary         
    def drawcard(self):
        return self.cards.pop()

    def draw(self, deck):
        self.hand.append(deck.drawcard())
        return self

class Player(object):

    def __init__(self, name):
        self.name = name
        self.hand = []
        print("My Name is :: "+self.name)

    def draw(self, shuffled, num = 1):
        # self.hand.append(deck.drawcard())
        for i in range(num):
            card = deck.drawcard()
            if card:
                self.hand.append(card)

    def showHand(self):
        return (f'{self.name}\'s hand :: {self.hand}')





deck = Deck()  # creating object of Deck class
shuffled = deck.shuffle()

name = str(input("Enter Gamer Name :: "))
# deck.show()
player = Player(name)
player.draw(shuffled, 5)
print((player.showHand()))