from projects.project3.Menu import Menu
from projects.project3.Customer_Order import Customer_Order
from projects.project3.Order_Queue import Order_Queue

def main():
    order_queue = Order_Queue()

    password = authorization()
    if password == True:
        print("\nPassword correct! Welcome!")
    else:
        print("Too many incorrect attempts. Please try again later.")
        return

    while True:
        print("\n📋 Main Menu")
        print("1. Display Menu")
        print("2. Take New Order")
        print("3. View Open Orders")
        print("4. Mark Next Order as Complete")
        print("5. End-of-Day Report")
        print("6. Exit")

        choice = input("\nPlease choose an option (1-6): ")

        if choice == "1":
            print(Menu())
            input("\nPress enter to return to Main Menu: ").strip().upper()
        elif choice == "2":
            name = input("\nCustomer name: ")
            customer_order = Customer_Order(name)
            order = customer_order.take_order()
            if order:  # Only returns order if confirmed
                order_queue.add_order(order)
                print("\n✅ Order placed successfully!")
            else:
                print("\nOrder canceled.")
            input("\nPress enter to return to Main Menu: ")
        elif choice == "3":
            print(order_queue)
            input("\nPress enter to return to Main Menu: ").strip().upper()
        elif choice == "4":
            if order_queue.complete_order():
                print(f"\n✅ Completed Order for {customer_order.name}!")
            input("\nPress enter to return to Main Menu: ").strip().upper()
        elif choice == "5":
            order_queue.end_of_day_report()
            input("\nPress enter to return to Main Menu: ").strip().upper()
        elif choice == "6":
            print("\nExiting system. Goodbye!")
            break
        else:
            print("\nInvalid option. Try again.")

def authorization():
        for i in range(3):
            enter = input("\nPlease enter password: ")
            if enter == "meow":
                return True
            else:
                print("\nIncorrect password.")
        return False

if __name__ == '__main__':
    main()