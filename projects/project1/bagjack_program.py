from datastructures.bag import Bag
from projects.project1.card import Card, CardFace, CardSuit, create_deck
from projects.project1.game_logic import calculate_hand
import random

def main():

    num_decks = random.choice([2,4,6,8])

    deck = create_deck()
    compiled_deck = deck * num_decks

    random.shuffle(compiled_deck)
    
    player_hand = [compiled_deck.pop(), compiled_deck.pop()]
    dealer_hand = [compiled_deck.pop(), compiled_deck.pop()]
    dealer_upcard = dealer_hand[0]

    player_hand_value = calculate_hand(player_hand)
    dealer_hand_value = calculate_hand([dealer_upcard])

    #print(player_hand_value, dealer_hand_value)

main()