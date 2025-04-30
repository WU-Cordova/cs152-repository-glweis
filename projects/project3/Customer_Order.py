from datastructures.linkedlist import LinkedList
from projects.project3.Drink import Drink
from projects.project3.Menu import Menu
import __future__

# Customer Order = Linkedlist

class Customer_Order:
    def __init__(self, name: str) -> None:
        self._order = LinkedList(data_type = Drink)
        self.name = name
        self._count = 0
    
    def add_drink(self, drink) -> None:
        # create new instance to avoid shared references
        drink_copy = Drink(name=drink.name, price=drink.price, size=drink.size)
        
        # customization
        customize = input('\nDo you want customization? (Y)es or (N)o: ')
        if customize.upper() == 'Y' or customize.upper() == 'YES':
            customize_description = input('\nPlease type customization request: ')
            drink_copy.customization = customize_description
            print("\n✅ Customized order placed successfully!")
        elif customize.upper() == 'N' or customize.upper() == 'NO':
            print("\n✅ Drink added without customization!")
        else:
            print("\nWe would love to customize your drink if we knew what that meant! \nInvalid request. Please try again!")
            return self.add_drink(drink)
        
        # add newly created drink object to the order
        self._order.append(drink_copy)

    def remove_drink(self, drink) -> None:
        self._order.remove(drink)

    def restart(self) -> None:
        self._order.clear()

    def repeat_order(self) -> Drink:
        for order in self._order:
            print(order)

    def total_price(self) -> float:
        sum = 0
        for order in self._order:
            sum += order.price
        return sum
    
    def total_sold(self) -> int:
        return len(self._order)
    
    def take_order(self) -> 'Customer_Order':
        menu_obj = Menu()
        menu = menu_obj.return_items()
        more = 'Y' or 'YES'
        while more.upper() == 'Y' or more.upper() == 'YES' :
            try:
                start = int(input(f'\nWhat drink would you like? (enter number): '))
                if 1 <= start <= 5:
                    self.add_drink(menu[start - 1])
                else:
                    print("\nWe don't have that drink, sorry!")
                    continue
            except ValueError:
                print("\nPlease enter a valid number for the drink.")
                continue
            more = input('\nWould you like to order another? (Y)es or (N)o?: ')

        self._count += 1
        print(self)

        while True:
            confirm = input("\nConfirm this order with (Y)es or (N)o: ").strip().upper()
            if confirm == "Y" or confirm == "YES":
                return self
            elif confirm == "N" or confirm == "NO":
                return None
            else:
                print("Invalid input. Please type (Y)es or (N)o.")

    def __repr__(self):
        drinks = ", ".join(str(drink) for drink in self._order)
        return f"Order for {self.name}: [{drinks}] with {len(self._order)} drink(s)."
    
    def __str__(self):
        output = [f"\n📝 Order Summary for {self.name}:"]
        for drink in self._order:
            line = f"- {drink.name} ({drink.size})"
            if drink.customization:
                line += f" - {drink.customization}"
            output.append(line)
        return "\n".join(output)
    

# Unused stuff

    '''def add_drink(self, drink) -> None:
        customize = input('\nDo you want customization? (Y)es or (N)o: ')
        if customize.upper() == 'Y' or customize.upper() == 'YES':
            customize_description = input('\nPlease type customization request: ')
            drink.customization = customize_description
            print("\n✅ Customized order placed successfully!")
            self._order.append(drink)
        else:
            if customize.upper() == 'N' or customize.upper() == 'NO':
                print("\n✅ Drink added without customization!")
                self._order.append(drink)
            else:
                print("\nWe would love to customize your drink if we knew what that meant! \nInvalid request. Please try again!")
                self.add_drink(drink)'''
    
    '''def take_order(self) -> Drink:
        menu_obj = Menu()
        menu = menu_obj.return_items()
        #print(menu_obj.print_name())
        more = 'Y'
        while more.upper() == 'Y':
            start = int(input(f'\nWhat drink would you like? (enter number): '))
            if start == 1:
                self.add_drink(menu[0])
            elif start == 2:
                self.add_drink(menu[1])
            elif start == 3:
                self.add_drink(menu[2])
            elif start == 4:
                self.add_drink(menu[3])
            elif start == 5:
                self.add_drink(menu[4])
            elif not start == 1 or start == 2 or start == 3 or start == 4 or start == 5:
                print("\nWe don't have that drink, sorry!")
            more = input('\nWould you like to order another? (Y)es or (N)o?: ')
        self._count += 1
        return self'''
    