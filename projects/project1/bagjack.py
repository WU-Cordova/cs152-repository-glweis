from typing import Iterable, Optional
from random import random
from projects.project1.card import Card

class Bag():
    '''A version of the original 'bag' class, manipulated to recieve and deal with cards instead of items.'''

    def __init__(self, *cards: Optional[Iterable[Card]]) -> None:
        self.deck_bag = {}
        if cards:
            for card in cards:
                self.add(card)

    def add(self, card: Card) -> None:
        if card in self.deck_bag:
            self.deck_bag[card] += 1
        elif card == None:
            raise TypeError("None is not a card")
        else:
            self.deck_bag[card] = 1

    def remove(self, card: Card) -> None:
        if card in self.deck_bag:
            count_before = self.deck_bag[card]
            count_after = count_before - 1
            self.deck_bag[card] = count_after
        else:
            raise ValueError("card not in bag")

    def count(self, card: Card) -> int:
        counter = 0
        if card in self.deck_bag:
            counter += self.deck_bag[card]
            return counter
        else:
            return counter

    def __len__(self) -> int:
        length = 0
        for card in self.deck_bag:
            length += self.deck_bag[card]
        return length

    def distinct_card(self) -> int:
        '''Used to select distinct cards at the initialization of every bagjack game/round.'''
        distincts = set()
        for card in self.deck_bag:
            distincts.add(card)
        return distincts

    def __contains__(self, card) -> bool:
        if card in self.deck_bag:
            return True
        else:
            return False

    def clear(self) -> None:
        self.deck_bag.clear()