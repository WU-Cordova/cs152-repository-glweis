from projects.project1.bagjack import Bag
from projects.project1.card import Card, CardFace, CardSuit
from projects.project1.game_logic import Game
import random
import copy

def main():

    while True:
        game = Game()

        deck = [Card(face, suit) for suit in CardSuit for face in CardFace]
        #print("".join(str(card) for card in deck))

        num_decks = random.choice([2,4,6,8])
        compiled_deck = [card for _ in range(num_decks) for card in copy.deepcopy(deck)]
        #print("".join(str(card) for card in compiled_deck))

        deck_bag = Bag(*compiled_deck)

        #two_cards = random.sample(list(deck_bag.distinct_card()),2)
        #print(f"Two cards: {"".join(str(card) for card in two_cards)} with a face value of: {sum(card.card_face.face_value() for card in two_cards)}")

        player_hand = random.sample(list(deck_bag.distinct_card()),2)
        dealer_hand = random.sample(list(deck_bag.distinct_card()),2)
        dealer_upcard = dealer_hand[0]

        player_score = game.calculate_hand(player_hand)
        dealer_score = game.calculate_hand([dealer_upcard])

        # Starting the game
        print("🎮 Welcome to BlackJack!")
        print()
        print("🃏 Initial Deal:")
        print(f"Player's Hand: {player_hand[0]}{player_hand[1]} | Score: {player_score}")
        print(f"Dealer's Hand: {dealer_upcard}[Hidden] | Score: {dealer_score}")

        player_busted = not game.hit_or_stay(player_hand, deck_bag)

        # Check for blackjack
        if player_busted == False:
            if game.calculate_hand(player_hand) == 21:
                # New game?
                print()
                play_again = input("Do you want to play again? (Y)es or (N)o: ").strip().upper()
                if play_again == "N":
                    print("Game over! Thanks for playing!")
                    break
                elif play_again == "Y":
                    print("Starting new Game.")
                    print()
                    continue
                else:
                    print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

        # Dealer logic
        dealer_score = game.calculate_hand(dealer_hand)
        while dealer_score < 17:
            card = random.choice(list(deck_bag.deck_bag.keys()))
            dealer_hand.append(card)
            dealer_score = game.calculate_hand(dealer_hand)

            print(f"\nDealer's Hand: {"".join(str(card) for card in dealer_hand)} | Score: {dealer_score}")

        player_score = game.calculate_hand(player_hand)

        # Determine winner
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

        #bug when player busts but there is no win message for dealer

        # New game?
        print()
        play_again = input("Do you want to play again? (Y)es or (N)o: ").strip().upper()
        if play_again == "N":
            print("Game over! Thanks for playing!")
            break
        elif play_again == "Y":
            print("Starting new Game.")
            print()
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

if __name__ == '__main__':
    main()