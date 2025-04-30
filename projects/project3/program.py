from projects.project3.Menu import Menu
from projects.project3.Customer_Order import Customer_Order
from projects.project3.Order_Queue import Order_Queue

# CURRENT ISSUES
# end-of-day-report needs to be worked on.
# I need to use datastructures for certain components (check this!!)

def main():
    order_queue = Order_Queue()
    while True:
        print("\n📋 Main Menu")
        print("1. Display Menu")
        print("2. Take New Order")
        print("3. View Open Orders")
        print("4. Mark Next Order as Complete")
        print("5. End-of-Day Report")
        print("6. Exit")

        choice = input("\nChoose an Option (1-6): ")

        if choice == "1":
            print(Menu())
            #Menu().print_menu()
            input("\nPress enter to return to Main Menu: ").strip().upper()
        elif choice == "2":
            name = input("\nCustomer name: ")
            customer_order = Customer_Order(name)

            '''order = customer_order.take_order()
            print(order)
            confirm = input("\nConfirm this order with (Y)es or (N)o: ").strip().upper()
            if confirm == "Y" or confirm == "YES":
                order_queue.add_order(order)
                print("\n✅ Order placed successfully!")
            else:
                if confirm == "N" or confirm == "NO":
                    print("\nOrder canceled.")
                else:
                    print("\nWe're just gonna...uh...cancel your order.") # want logic to make you type y or n
            input("\nPress enter to return to Main Menu: ").strip().upper()'''

            order = customer_order.take_order()
            if order:  # Only returns order if confirmed
                order_queue.add_order(order)
                print("\n✅ Order placed successfully!")
            else:
                print("\nOrder canceled.")
            input("\nPress enter to return to Main Menu: ")

        elif choice == "3":
            #order_queue.view_open_orders()
            print(order_queue)
            input("\nPress enter to return to Main Menu: ").strip().upper()
        elif choice == "4":
            order_queue.complete_order()
            print(f"\n✅ Completed Order for {customer_order.name}!")
            input("\nPress enter to return to Main Menu: ").strip().upper()
        elif choice == "5":
            order_queue.end_of_day_report() # hmmmm
            input("\nPress enter to return to Main Menu: ").strip().upper()
        elif choice == "6":
            print("\nExiting system. Goodbye!")
            break
        else:
            print("\nInvalid option. Try again.")

if __name__ == '__main__':
    main()