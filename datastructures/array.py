# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        if starting_sequence is None:
            starting_sequence = []

        # Ensure it's a sequence
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("The starting sequence must be a valid sequence type.")
        
        # Check that each element in the sequence matches the specified data_type
        for item in starting_sequence:
            if not isinstance(item, data_type):
                raise TypeError(f"Element {item} is not of type {data_type}.")
    
        # Check if data_type is a valid type
        if not isinstance(data_type, type):
            raise ValueError("Data_type should be a valid type (e.g., int, str, float, etc.).")
        
        self.__data_type = data_type
        self.__capacity = len(starting_sequence)  # Initial capacity
        self.__element_count = len(starting_sequence)
        
        # Initialize the elements array with the required capacity
        self.__elements = np.empty(self.__capacity, dtype=self.__data_type)
        
        # Copy elements from the starting_sequence to the internal elements array
        for i in range(self.__element_count):
            self.__elements[i] = starting_sequence[i]

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        # If slice
        if isinstance(index, slice):
            start = index.start if index.start is not None else 0
            stop = index.stop if index.stop is not None else self.__element_count
            step = index.step if index.step is not None else 1
            # Check slice range
            if start >= self.__element_count or stop > self.__element_count:
                raise IndexError("Index out of range.")
            # Sliced items and array return
            sliced_items = self.__elements[start:stop:step]
            return Array(starting_sequence=sliced_items.tolist(), data_type=self.__data_type)
        # If single index
        if -self.__element_count < index < self.__element_count:
            item = self.__elements[index]
            return item.item() if isinstance(item, np.generic) else item
        else:
            raise IndexError("Index out of range.")
    
    def __setitem__(self, index: int, item: T) -> None:
        if -self.__element_count < index < self.__element_count:
            if isinstance(item, self.__data_type):
                self.__elements[index] = item
            else:
                raise TypeError("Item is not the same data type as the elements contained in the array.")
        else:
            raise IndexError("Index out of range.")

    def append(self, data: T) -> None:
        # If the array has reached its capacity
        if self.__element_count >= self.__capacity:
            self.__grow((self.__capacity * 2) + 1)
        # Append
        self.__elements[self.__element_count] = data
        # Update logical size
        self.__element_count += 1

    def append_front(self, data: T) -> None:
        # If the array has reached its capacity
        if self.__element_count >= self.__capacity:
            self.__grow(self.__capacity * 2)
        # Shift all elements one position to the right
        for i in range(self.__element_count, 0, -1):
            self.__elements[i] = self.__elements[i - 1]
        # Insert the new data at the front
        self.__elements[0] = data
        self.__element_count += 1

    def pop(self) -> None:
        if self.__element_count == 0:
            raise IndexError("Empty array.")
        # Last element
        last_element = self.__elements[self.__element_count - 1]
        # Update logical size
        self.__element_count -= 1
        # Update array size if needed
        if self.__element_count <= self.__capacity // 4:
            self.__capacity = self.__capacity // 2
            self.__elements = np.empty(self.__capacity, dtype=self.__data_type)
            # Recopy the items to the new array
            for i in range(self.__element_count):
                self.__elements[i] = self.__elements[i]
        return last_element
    
    def pop_front(self) -> None:
        if self.__element_count == 0:
            raise IndexError("Empty array.")
        # First element
        first_element = self.__elements[0]
        # Shift all elements one position to the left
        for i in range(1, self.__element_count):
            self.__elements[i - 1] = self.__elements[i]
        # Update logical size
        self.__element_count -= 1
        # Update array size if needed
        if self.__element_count <= self.__capacity // 4:
            self.__capacity = self.__capacity // 2
            self.__elements = np.empty(self.__capacity, dtype=self.__data_type)
            # Recopy the items to the new array
            for i in range(self.__element_count):
                self.__elements[i] = self.__elements[i]
        return first_element

    def __len__(self) -> int: 
        return self.__element_count

    def __eq__(self, other: object) -> bool:
        # If not an array
        if not isinstance(other, Array):
            return False
        # If the lengths are not equal
        if len(self) != len(other):
            return False
        # If any of the elements do not match
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True
    
    def __iter__(self) -> Iterator[T]:
        return iter(self.__elements)

    def __reversed__(self) -> Iterator[T]:
        reversed_elements = self.__elements[:self.__element_count][::-1]
        return iter(reversed_elements)

    def __delitem__(self, index: int) -> None:
        if not -self.__element_count < index < self.__element_count:
            raise IndexError("Index out of range.")
        # Shift all elements one position to the left
        for i in range(index, self.__element_count - 1):
            self.__elements[i] = self.__elements[i + 1]
        # Update logical size
        self.__element_count -= 1
        # Update array size if needed
        if self.__element_count <= self.__capacity // 4:
            self.__capacity = self.__capacity // 2
            self.__elements = np.empty(self.__capacity, dtype=self.__data_type)
            # Recopy the items to the new array
            for i in range(self.__element_count):
                self.__elements[i] = self.__elements[i]

    def __contains__(self, item: Any) -> bool:
        return any(x == item for x in self.__elements[:self.__element_count])

    def clear(self) -> None:
        # Reset logical size
        self.__element_count = 0
        # Empty array
        self.__elements = np.empty(0, dtype=self.__data_type)

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__element_count}, Physical: {len(self.__elements)}, type: {self.__data_type}'
    

    def __grow(self, new_size: int) -> None:
        """Private method to grow the array when the capacity is reached."""
        # Check if the new size is larger than the current capacity
        if new_size <= self.__capacity:
            return
        # Create a new NumPy array with the new size
        new_array = np.empty(new_size, dtype=self.__data_type)
        # Copy over the existing elements from the old array to the new array
        for i in range(self.__element_count):
            new_array[i] = self.__elements[i]
        # Set the current elements array to the new array
        self.__elements = new_array
        self.__capacity = new_size
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')