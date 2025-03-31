from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type: type) -> None:
            self.row_index = row_index
            self.array = array
            self.num_columns = num_columns
            self.data_type = data_type

        def map_index(self, row_index: int, column_index: int) -> int:
            index = self.num_columns * row_index + column_index
            return index

        def __getitem__(self, column_index: int) -> T:
            if -self.num_columns < column_index < self.num_columns:
                index = self.map_index(self.row_index, column_index)
                return self.array[index]
            else:
                raise IndexError("Index out of range.")
        
        def __setitem__(self, column_index: int, value: T) -> None:
            index = self.map_index(self.row_index, column_index)
            self.array[index] = value
        
        def __iter__(self) -> Iterator[T]:
            for column_index in range(self.num_columns):
                yield self[column_index]
        
        def __reversed__(self) -> Iterator[T]:
            for column_index in range(self.num_columns - 1, -1, -1):
                yield self[column_index]

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        # Ensure it's a sequence of sequences
        if not isinstance(starting_sequence, list):
            raise ValueError("must be a sequence of sequences")
        for index, row in enumerate(starting_sequence):
            if not isinstance(row, list):
                raise ValueError("must be a sequence of sequences")
            
            # Ensure all items in the row are of the expected data type
            if not all(isinstance(item, data_type) for item in row):
                raise ValueError("All items must be of the same type")
        
        # Length check
        row_lengths = [len(row) for row in starting_sequence]
        if len(set(row_lengths)) != 1:
            raise ValueError("must be a sequence of sequences with the same length")
        
        self.data_type = data_type
        self.row_len = len(starting_sequence)
        self.col_len = len(starting_sequence[0])

        self.array2 = Array([data_type() for item in range(self.row_len * self.col_len)], data_type=data_type)
        
        index = 0
        for row_index in range(self.row_len):
            for col_index in range(self.col_len):
                self.array2[index] = starting_sequence[row_index][col_index]
                index += 1

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        starting_sequence = [[data_type() for _ in range(cols)] for _ in range(rows)]
        return Array2D(starting_sequence=starting_sequence, data_type=data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]:
        if -self.row_len < row_index < self.row_len:
            return Array2D.Row(row_index, self.array2, self.col_len, self.data_type)
        else:
            raise IndexError("Index out of bounds.")
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        for row_index in range(self.row_len):
            yield self[row_index]
    
    def __reversed__(self):
        for row_index in range(self.row_len - 1, -1, -1):
            yield self[row_index]
    
    def __len__(self): 
        return self.row_len
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.row_len} Rows x {self.col_len} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')