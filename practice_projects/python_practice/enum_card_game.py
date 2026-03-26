# This game draws 5 random cards from a deck of cards to practices enum. 

from enum import Enum
import random 

class Suit(Enum):
    hearts = "♥"
    spades = "♠"
    clubs = "♣"
    diamonds = "♦"

class Rank(Enum):
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    six = "6"
    seven = "7" 
    eight = "8"
    nine = "9"
    ten = "10"
    jack = "J"
    queen = "Q"
    king = "K"
    ace = "A"


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"Card( {self.suit.value}, {self.rank.value})"
    

# create deck of cards
deck = [Card(suit, rank) for suit in Suit for rank in Rank]
random.shuffle(deck)

# pull five cards from the deck
hand = deck[:5]
print("Your hand: ", ",".join(str(card) for card in hand))