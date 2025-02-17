from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.items_counts = {}

    def add(self, item: T) -> None:
        if item in self.items_counts:
            self.items_counts[item] += 1
        elif item == None:
            raise TypeError("None is not an item")
        else:
            self.items_counts[item] = 1

    def remove(self, item: T) -> None:
        if item in self.items_counts:
            count_before = self.items_counts[item]
            count_after = count_before - 1
            self.items_counts[item] = count_after
        else:
            raise ValueError("Item not in bag")

    def count(self, item: T) -> int:
        counter = 0
        if item in self.items_counts:
            counter += self.items_counts[item]
            return counter
        else:
            return counter

    def __len__(self) -> int:
        length = 0
        for item in self.items_counts:
            length += self.items_counts[item]
        return length

    def distinct_items(self) -> int:
        distincts = set()
        for item in self.items_counts:
            distincts.add(item)
        return distincts

    def __contains__(self, item) -> bool:
        if item in self.items_counts:
            return True
        else:
            return False

    def clear(self) -> None:
        self.items_counts.clear()