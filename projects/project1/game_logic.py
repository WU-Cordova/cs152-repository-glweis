from enum import Enum
from projects.project1.card import Card, CardFace, CardSuit

class Game:

    '''def create_deck():

        card_suits = [suit for suit in CardSuit]
        #print(card_suits)
        card_faces = [face.name for face in CardFace]
        print(card_faces)

        cards = []

        for suit in card_suits:
            for face in card_faces:
                cards.append((Card(card_face=face, card_suit=suit)))

            # Add face cards (Jack, Queen, King) as rank 10
            for face in [CardFace.JACK, CardFace.QUEEN, CardFace.KING]:
                cards.append(Card(card_face=face, card_suit=suit))

            # Add Ace (A)
            cards.append(Card(card_face=CardFace.ACE.value, card_suit=suit))
            
            #for card in cards:
                #print(f"{card.card_face}{card.card_suit}")\
        
        print(cards)
        return cards'''

    def calculate_hand(hand: list) -> int:
        total_value = 0
        ace_count = 0

        for card in hand:
            print(card.card_face)
            total_value += int(card.card_face)
            if card.card_face == CardFace.ACE:
                ace_count += 1
        
        while total_value > 21 and ace_count:
            total_value -= 10
            ace_count -= 1
        
        #print(total_value)
        return total_value


'''# Example of creating and printing cards
card1 = Card(CardFace.JACK, CardSuit.HEARTS)
card2 = Card(CardFace.TEN, CardSuit.SPADES)
card3 = Card(CardFace.FIVE, CardSuit.CLUBS)

# Print cards in the desired format
print(card1)  # Output: J♥️
print(card2)  # Output: 10♠️
print(card3)  # Output: 5♣️'''