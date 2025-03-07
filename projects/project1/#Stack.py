#Stack
from datastructures.array import Array

class Stack:

    def __init__(self):
        self.Array = Array()
        self.top_item_index = int
    
    def push(self, item):
        self.Array.append(item)
        self.top_item_index += 1

    def top(self):
        return self.Array[self.top_item_index]

    def size(self):
        return len(self.Array)
    
    def remove(self, top_item_index):
        pass
    
    def pop(self):
        self.top()
        self.Array.remove(self.top_item_index)
        self.top_item_index -= 1