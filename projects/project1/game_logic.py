from enum import Enum
from projects.project1.card import Card, CardFace, CardSuit
import random


class Game:

    @staticmethod
    def calculate_hand(hand: list) -> int:
        total_value = 0
        ace_count = 0

        for card in hand:
            total_value += int(card.card_face.face_value())
            if card.card_face == CardFace.ACE:
                ace_count += 1
        
        while total_value > 21 and ace_count:
            total_value -= 10
            ace_count -= 1
            # print out ace = 1 instead somehow
        
        #print(total_value)
        return total_value
    

    def hit_or_stay(self, player_hand, deck_bag) -> bool:

        while True:
            player_score = self.calculate_hand(player_hand)
            print()
            print(f"Player's Hand: {"".join(str(card) for card in player_hand)} | Score: {player_score}")

            if player_score > 21:
                print("Bust! You went over 21.")
                return False
            
            elif player_score == 21:
                print()
                print()
                print("🏆 You have Blackjack! You win!")
                return True
                # does not exit the game fully when player has blackjack

            else:
                action = input("Do you want to (H)it or (S)tay? ").strip().upper()

                if action == "H":
                    card = random.choice(list(deck_bag.deck_bag.keys()))
                    player_hand.append(card)
                    player_score = Game.calculate_hand(player_hand)
                    if player_score > 21:
                        print("Bust! You went over 21.")
                        return False
                elif action == "S":
                    return True
                else:
                    print("Invalid input. Please enter 'H' for Hit or 'S' for Stay.")