from dataclasses import dataclass
from enum import Enum
#from players import Players

#windows key + period + semi-colon
#♠️ ♥️ ♦️ ♣️
#🃏🎮🏆
'''Ace logic: 
    if 21 - current card value >= 11:
        Ace value = 11
    else:
        Ace value = 1'''

class CardSuit(Enum):
    #constant name for the card suits
    HEARTS = "♥️"
    SPADES = "♠️"
    CLUBS = "♣️"
    DIAMONDS = "♦️"

class CardFace(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE = 11

@dataclass
class Card:
    card_face: CardFace
    card_suit: CardSuit

    def __str__(self):
        # Special handling for face cards (Jack, Queen, King) and Ace
        if self.card_face == CardFace.JACK:
            face = "J"
        elif self.card_face == CardFace.QUEEN:
            face = "Q"
        elif self.card_face == CardFace.KING:
            face = "K"
        elif self.card_face == CardFace.ACE:
            face = "A"
        else:
            face = str(self.card_face.value)  # For numbered cards, display the value
        
        # Return a formatted string for the card, combining face and suit
        return f"{face}{self.card_suit.value}"
     
def create_deck():

    #card_suits = [CardSuit.HEARTS, CardSuit.SPADES, CardSuit.CLUBS, CardSuit.DIAMONDS]
    #card_faces = [CardFace.TWO, CardFace.THREE, CardFace.FOUR, CardFace.FIVE, CardFace.SIX, CardFace.SEVEN, CardFace.EIGHT, CardFace.NINE, CardFace.TEN, CardFace.JACK, CardFace.QUEEN, CardFace.KING, CardFace.ACE]
    card_suits = [suit.value for suit in CardSuit]
    card_faces = [face.value for face in CardFace]

    cards = []

    for suit in card_suits:
        for face in card_faces[:9]:
            cards.append((Card(card_face=face, card_suit=suit)))

        # Add face cards (Jack, Queen, King) as rank 10
        for face in [CardFace.JACK, CardFace.QUEEN, CardFace.KING]:
            cards.append(Card(card_face=face, card_suit=suit))

        # Add Ace (A)
        cards.append(Card(card_face=CardFace.ACE.value, card_suit=suit))
        
    return cards

    #for card in cards:
        #print(f"{card.card_face}{card.card_suit}")

# Example of creating and printing cards
card1 = Card(CardFace.JACK, CardSuit.HEARTS)
card2 = Card(CardFace.TEN, CardSuit.SPADES)
card3 = Card(CardFace.FIVE, CardSuit.CLUBS)

# Print cards in the desired format
print(card1)  # Output: J♥️
print(card2)  # Output: 10♠️
print(card3)  # Output: 5♣️