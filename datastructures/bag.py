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
        for item in self.items_counts:
            counter += self.items_counts[item]
        return counter

    def __len__(self) -> int:
        raise NotImplementedError("__len__ method not implemented")

    def distinct_items(self) -> int:
        raise NotImplementedError("distinct_items method not implemented")

    def __contains__(self, item) -> bool:
        raise NotImplementedError("__contains__ method not implemented")

    def clear(self) -> None:
        raise NotImplementedError("clear method not implemented")