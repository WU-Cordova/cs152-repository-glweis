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

        for item in sequence:
            llist.append(item)
        return llist

    def append(self, item: T) -> None:
        # check that all the items in sequence are of the same type
        if not isinstance(item, self.data_type):
            raise TypeError("Incorrect item type")
        
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
        # check that all the items in sequence are of the same type
        if not isinstance(item, self.data_type):
            raise TypeError("Incorrect item type")

        node = LinkedList.Node(data=item)

        if self.empty:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
        self.count += 1

    def insert_before(self, target: T, item: T) -> None:
        # raise TypeError if the target is not the right type (done)
        # raise TypeError if the item is not the right type (done)
        # raise ValueError if the target does not exist (done)
        if not isinstance(target, type(self.head.data)) or not isinstance(item, type(self.head.data)):
            raise TypeError("Both target and item must match the data type used in the linked list.")

        travel = self.head
        while travel:

            if travel.data == target:
                break

            travel = travel.next

        if travel == None:
            raise ValueError(f'The target value {target} was not found in the linked list.')
        # head = tail
        if travel == self.head:
            self.prepend(item)
            self.count += 1
            return
        # Travel != head
        new_node = LinkedList.Node(data=item)
        travel.previous.next = new_node
        new_node.next = travel
        new_node.previous = travel.previous
        travel.previous = new_node
        self.count += 1

    def insert_after(self, target: T, item: T) -> None:
        # raise TypeError if the target is not the right type (done)
        # raise TypeError if the item is not the right type (done)
        # raise ValueError if the target does not exist (done)
        if not isinstance(target, type(self.head.data)) or not isinstance(item, type(self.head.data)):
            raise TypeError("Both target and item must match the data type used in the linked list.")

        travel = self.head
        while travel:

            if travel.data == target:
                break

            travel = travel.next

        if travel == None:
            raise ValueError(f'The target value {target} was not found in the linked list.')
        # head = tail
        if travel == self.head:
            self.append(item)
            self.count += 1
            return
        # Travel != head
        new_node = LinkedList.Node(data=item)
        travel.next.previous = new_node
        new_node.next = travel.next
        new_node.previous = travel
        travel.next = new_node
        self.count += 1

    def remove(self, item: T) -> None:
        # TypeError: If the item is not of the correct type (done)
        # ValueError: If the item is not in the list (done)
        if not isinstance(item, type(self.head.data)):
            raise TypeError("Incorrect item type.")
        
        travel = self.head
        while travel:

            if travel.data == item:
                break

            travel = travel.next

        if travel == None:
            raise ValueError(f'{item} was not found in the linked list.')
        # Travel = head = tail
        if travel == self.head and travel == self.tail:
            self.clear()
            return
        
        # Travel = head
        if travel == self.head:
            self.head = travel.next
            self.head.previous = None
        # Travel = tail
        elif travel == self.tail:
            self.tail = travel.previous
            self.tail.next = None
        # middle
        else:
            travel.previous.next = travel.next
            travel.next.previous = travel.previous
        
        self.count -= 1

    def remove_all(self, item: T) -> None:
        # TypeError: If the item is not of the correct type (done)
        # ValueError: If the item is not in the list (done)
        if not isinstance(item, type(self.head.data)):
            raise TypeError("Incorrect item type.")
        
        travel = self.head
        found = False
        while travel:

            if travel.data == item:
                found = True

                # Travel = head = tail
                if travel == self.head and travel == self.tail:
                    self.clear()
                    return

                # Travel = head
                if travel == self.head:
                    self.head = travel.next
                    self.head.previous = None
                # Travel = tail
                elif travel == self.tail:
                    self.tail = travel.previous
                    self.tail.next = None
                # middle
                else:
                    travel.previous.next = travel.next
                    travel.next.previous = travel.previous

                self.count -= 1

            travel = travel.next

        if found == False:
            raise ValueError(f'{item} was not found in the linked list.')

    def pop(self) -> T:
        if self.empty:
            raise IndexError("LinkedList is empty.")
        data = self.tail.data

        if self.tail is self.head:
            self.clear()
            return data
        
        self.tail = self.tail.previous
        self.tail.next = None
        self.count -= 1
        return data

    def pop_front(self) -> T:
        if self.empty:
            raise IndexError("LinkedList is empty.")
        data = self.head.data

        if self.tail is self.head:
            self.clear()
            return data
        
        self.head = self.head.next
        self.head.previous = None
        self.count -= 1
        return data

    @property
    def front(self) -> T:
        # check that head is not None first
        if self.head:
            return self.head.data
        raise IndexError("LinkedList is empty.")

    @property
    def back(self) -> T:
        # check that tail is not None first
        if self.tail:
            return self.tail.data
        raise IndexError("LinkedList is empty.")

    @property
    def empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        self.head = self.tail = None
        self.count = 0

    def __contains__(self, item: T) -> bool:
        if not isinstance(item, self.data_type):
            raise TypeError("Incorrect item type.")
        
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def __iter__(self) -> ILinkedList[T]:
        self.travel_node = self.head
        return self

    def __next__(self) -> T:
        if self.travel_node is None:
            raise StopIteration
        data = self.travel_node.data
        self.travel_node = self.travel_node.next
        return data
    
    def __reversed__(self) -> ILinkedList[T]:
        reversed_list = LinkedList(data_type=self.data_type)

        while self.tail:
            reversed_list.append(self.tail.data)
            self.tail = self.tail.previous
        
        return reversed_list
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        if len(self) != len(other):
            return False
        
        while self.head:
            if self.head.data != other.head.data:
                return False
            self.head = self.head.next
            other.head = other.head.next
        
        return True

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
