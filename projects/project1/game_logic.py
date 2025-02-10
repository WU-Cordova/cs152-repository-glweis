from enum import Enum
from projects.project1.card import CardFace
import random

class Game:
    '''Handles score calculation, hit or stay logic, and win logic for the dealer and player.'''

    @staticmethod
    def calculate_hand(hand: list) -> int:
        '''Handles score calculation for either the dealer or the player, depending which hand is passed in.'''

        total_value = 0
        ace_count = 0

        for card in hand:
            total_value += int(card.card_face.face_value())
            if card.card_face == CardFace.ACE:
                ace_count += 1
        
        while total_value > 21 and ace_count:
            total_value -= 10
            ace_count -= 1
            
        return total_value

    def hit_or_stay(self, player_hand, deck_bag) -> bool:
        '''Handles logic for player hitting and staying.'''

        while True:
            player_score = self.calculate_hand(player_hand)
            print()
            print(f"Player's Hand: {"".join(str(card) for card in player_hand)} | Score: {player_score}")

            if player_score > 21:
                print()
                print(f"Player's Hand: {"".join(str(card) for card in player_hand)} | Score: {player_score}")
                print("Bust! You went over 21.")
                return False
            
            elif player_score == 21:
                print()
                print()
                print("🏆 You have Blackjack! You win!")
                return True

            else:
                action = input("Do you want to (H)it or (S)tay? ").strip().upper()

                if action == "H":
                    card = random.choice(list(deck_bag.deck_bag.keys()))
                    player_hand.append(card)
                    player_score = Game.calculate_hand(player_hand)
                    if player_score > 21:
                        print()
                        print(f"Player's Hand: {"".join(str(card) for card in player_hand)} | Score: {player_score}")
                        print("Bust! You went over 21.")
                        return False
                elif action == "S":
                    return True
                else:
                    print("Invalid input. Please enter 'H' for Hit or 'S' for Stay.")
    
    def determine_winner(self, dealer_score, player_score, player_busted, dealer_hand):
        '''Helps determine winner if not already determined via the hit_or_stay() function.'''

        if dealer_score == 21:
            print(f"\nDealer's Hand: {"".join(str(card) for card in dealer_hand)} | Score: {dealer_score}")
            print("Dealer has Backjack! Dealer wins!") # test logic for dealer blackjack
        elif dealer_score > 21 and not player_busted:
            print("Dealer busts! You win!")
        elif dealer_score > 21 and player_busted:
            print("Dealer busts! It's a tie!") 
        elif dealer_score > player_score and dealer_score < 21 or player_busted and dealer_score < 21:
            print(f"\nDealer's Hand: {"".join(str(card) for card in dealer_hand)} | Score: {dealer_score}")
            print("Dealer wins!")
        elif dealer_score < player_score and not player_busted:
            print(f"\nDealer's Hand: {"".join(str(card) for card in dealer_hand)} | Score: {dealer_score}")
            print("You win!")
        elif dealer_score == player_score:
            print(f"\nDealer's Hand: {"".join(str(card) for card in dealer_hand)} | Score: {dealer_score}")
            print("It's a tie!")