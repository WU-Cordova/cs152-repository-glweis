from projects.project1.bagjack import Bag
from projects.project1.card import Card, CardFace, CardSuit
from projects.project1.game_logic import Game
import random
import copy

def main():

    while True:
        game = Game()

        deck = [Card(face, suit) for suit in CardSuit for face in CardFace]
        num_decks = random.choice([2,4,6,8])
        compiled_deck = [card for _ in range(num_decks) for card in copy.deepcopy(deck)]
        deck_bag = Bag(*compiled_deck)

        player_hand = random.sample(list(deck_bag.distinct_card()),2)
        dealer_hand = random.sample(list(deck_bag.distinct_card()),2)
        dealer_upcard = dealer_hand[0]

        player_score = game.calculate_hand(player_hand)
        dealer_score = game.calculate_hand([dealer_upcard])

        # Starting messages
        print("🎮 Welcome to BlackJack!")
        print()
        print("🃏 Initial Deal:")
        print(f"Player's Hand: {player_hand[0]}{player_hand[1]} | Score: {player_score}")
        print(f"Dealer's Hand: {dealer_upcard}[Hidden] | Score: {dealer_score}")

        # Player busts
        player_busted = not game.hit_or_stay(player_hand, deck_bag)

        # Check for blackjack:
        # hit_or_stay() returns either True or False, and one of these True cases corresponds to blackjack
        if player_busted == False:
            if game.calculate_hand(player_hand) == 21:
                # New game?
                print()
                play_again = input("Do you want to play again? (Y)es or (N)o: ").strip().upper()
                if play_again == "N":
                    print("Game over! Thanks for playing!")
                    break
                elif play_again == "Y":
                    print()
                    print("Starting new Game.")
                    print()
                    continue
                else:
                    print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

        # Dealer logic
        dealer_score = game.calculate_hand(dealer_hand)
        player_score = game.calculate_hand(player_hand)

        while dealer_score < 17:
            card = random.choice(list(deck_bag.deck_bag.keys()))
            dealer_hand.append(card)
            dealer_score = game.calculate_hand(dealer_hand)
            print(f"\nDealer's Hand: {"".join(str(card) for card in dealer_hand)} | Score: {dealer_score}")
        
        # Determine winner
        game.determine_winner(dealer_score, player_score, player_busted, dealer_hand)

        # New game?
        print()
        play_again = input("Do you want to play again? (Y)es or (N)o: ").strip().upper()
        if play_again == "N":
            print("Game over! Thanks for playing!")
            break
        elif play_again == "Y":
            print()
            print("Starting new Game.")
            print()
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

if __name__ == '__main__':
    main()