from tests.test_array import Car
from datastructures.array2d import Array2D

# 2d array selection algorithim testing:

Array = [["a", "b", "c", "d"],
         ["e", "f", "g", "h"],
         ["i", "j", "k", "l"],
         ["m", "n", "o", "p"],
         ["q", "r", "s", "t"],
         ["u", "v", "w", "x"],
         ["y", "z", "&", "$"]]

num_cols = 4
row_requested = 4
col_requested = 3

let_2d = Array[row_requested][col_requested]

let_ind_1d = num_cols * row_requested + col_requested
length = len(Array[0]) * len(Array)
times = let_ind_1d // num_cols
spec_row = times - 1 #correct
spec_col = let_ind_1d #not correct

let_1d = Array[spec_row][spec_col]

print(let_2d)
print(let_1d)



# Stuff for array 2D
def main():

    data_type = Car

    rows_len, cols_len = 3, 2

    sequence = [[data_type() for _ in range(cols_len)] for _ in range(rows_len)]

    return Array2D(starting_sequence=sequence, data_type=data_type)