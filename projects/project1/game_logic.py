from enum import Enum
from projects.project1.card import Card, CardFace, CardSuit

def calculate_hand(hand: list) -> int:
    total_value = 0
    ace_count = 0

    for card in hand:
        total_value += card.card_face.value
        if card.card_face == CardFace.ACE:
            ace_count += 1
    
    while total_value > 21 and ace_count:
        total_value -= 10
        ace_count -= 1
    
    return total_value



'''class Players():
    def __init__(self):
        player_count = 0
        dealer_count = 0'''