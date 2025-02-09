from projects.project1.bagjack import Bag
from projects.project1.card import Card, CardFace, CardSuit
from projects.project1.game_logic import Game
import random
import copy

def main():

    deck = [Card(face, suit) for suit in CardSuit for face in CardFace]
    #print("".join(str(card) for card in deck))

    num_decks = random.choice([2,4,6,8])
    compiled_deck = [card for _ in range(num_decks) for card in copy.deepcopy(deck)]
    #print("".join(str(card) for card in compiled_deck))

    deck_bag = Bag(*compiled_deck)

    two_cards = random.sample(list(deck_bag.distinct_card()),2)
    #print(f"Two cards: {"".join(str(card) for card in two_cards)} with a face value of: {sum(card.card_face.face_value() for card in two_cards)}")
    



    '''num_decks = random.choice([2,4,6,8])

    deck = Game.create_deck()
    compiled_deck = deck * num_decks

    random.shuffle(compiled_deck)
    
    player_hand = [compiled_deck.pop(), compiled_deck.pop()]
    dealer_hand = [compiled_deck.pop(), compiled_deck.pop()]
    dealer_upcard = dealer_hand[0]

    player_hand_value = Game.calculate_hand(player_hand)
    dealer_hand_value = Game.calculate_hand([dealer_upcard])

    print(player_hand_value, dealer_hand_value)'''

if __name__ == '__main__':
    main()