from dataclasses import dataclass
from enum import Enum
import random

#windows key + period + semi-colon
#♠️ ♥️ ♦️ ♣️
#🃏🎮🏆

class CardSuit(Enum):
    #constant name for the card suits
    HEARTS = "♥️"
    SPADES = "♠️"
    CLUBS = "♣️"
    DIAMONDS = "♦️"

class CardFace(Enum):
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"

    def face_value(self) -> int:
        match self:
            case CardFace.JACK | CardFace.QUEEN | CardFace.KING:
                return 10
            case CardFace.ACE:
                return 11
            case _:
                return int(self.value)
   
@dataclass
class Card:
    card_face: CardFace
    card_suit: CardSuit

    def __hash__(self) -> int:
        return hash(self.card_face.name) * hash(self.card_suit.name)

    def __str__(self) -> str:
        return f"[{self.card_face.value}{self.card_suit.value}]"