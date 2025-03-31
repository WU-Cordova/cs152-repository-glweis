from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.count = 0
        self.head = None
        self.tail = None
        self.data_type = data_type

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        # check that all the items in sequence are of the same type
        llist = LinkedList(data_type=data_type)

        for item in Sequence:
            llist.append(item)
        return llist 

    def append(self, item: T) -> None:
        # check that all the items in sequence are of the same type
        node = LinkedList.Node(data=item)

        if self.empty:
            self.head = self.tail = node
        else:
            node.previous = self.tail
            if self.tail:
                self.tail.next = node
            self.tail = node
        self.count += 1

    def prepend(self, item: T) -> None:
        node = LinkedList.Node(data=item)

        if self.empty:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
        self.count += 1

    def insert_before(self, target: T, item: T) -> None:
        raise NotImplementedError("LinkedList.insert_before is not implemented")

    def insert_after(self, target: T, item: T) -> None:
        raise NotImplementedError("LinkedList.insert_after is not implemented")

    def remove(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove is not implemented")

    def remove_all(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove_all is not implemented")

    def pop(self) -> T:
        raise NotImplementedError("LinkedList.pop is not implemented")

    def pop_front(self) -> T:
        raise NotImplementedError("LinkedList.pop_front is not implemented")

    @property
    def front(self) -> T:
        # check that head is not None first
        if self.head:
            return self.head.data

    @property
    def back(self) -> T:
        # check that tail is not None first
        if self.tail:
            return self.tail.data

    @property
    def empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        raise NotImplementedError("LinkedList.clear is not implemented")

    def __contains__(self, item: T) -> bool:
        raise NotImplementedError("LinkedList.__contains__ is not implemented")

    def __iter__(self) -> ILinkedList[T]:
        raise NotImplementedError("LinkedList.__iter__ is not implemented")

    def __next__(self) -> T:
        raise NotImplementedError("LinkedList.__next__ is not implemented")
    
    def __reversed__(self) -> ILinkedList[T]:
        raise NotImplementedError("LinkedList.__reversed__ is not implemented")
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("LinkedList.__eq__ is not implemented")

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
