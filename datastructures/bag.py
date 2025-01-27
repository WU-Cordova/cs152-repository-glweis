from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.items_counts = {}

    def add(self, item: T) -> None:
        if item in self.items_counts:
            self.items_counts[item] += 1
        else:
            self.items_counts[item] = 1

    def remove(self, item: T) -> None:
        raise NotImplementedError("remove method not implemented")

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