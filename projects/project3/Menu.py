from datastructures.array import Array
from projects.project3.Drink import Drink

# Menu = Array

class Menu:
    def __init__(self):
        self._menu = Array(starting_sequence = [Drink(name= 'Hot Cocoa', price= 4.00, size= 'Medium'), \
                                                Drink(name= 'Americano', price= 4.25, size= 'Medium'), \
                                                Drink(name= 'Latte', price= 5.00, size= 'Medium'), \
                                                Drink(name= 'Lemonade', price= 4.00, size= 'Medium'), \
                                                Drink(name= 'Iced Coffee', price= 3.50, size= 'Medium')], data_type = Drink)

    def print_menu(self): # don't need
        print("\n🍹 Available Drinks:")
        for index, item in enumerate(self._menu, start=1):
            print(f"{index}. {item.name} - ${item.price:.2f}")

    def get_drink(self, num: int) -> Drink:
        return self._menu[num - 1]
    
    def print_name(self):
        for item in self._menu:
            print(item.name)

    def return_items(self) -> Array[Drink]:
        return self._menu
    
    def __str__(self):
        """Returns a string version of the menu."""
        lines = ["\n🍹 Available Drinks:"]
        for index, item in enumerate(self._menu, start=1):
            lines.append(f"{index}. {item.name} - ${item.price:.2f}")
        return "\n".join(lines)