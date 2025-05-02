# 🐾 Bearcat Bistro Ordering System

For this mini-project, I worked with Jerrick Little and Kendall Brown.


## 1. Data Structure Choices for Each Component (Minimum 5):

### * 🍹 Menu - Array

Becuase the Menu is a fixed list of 5 Bistro drinks, it made sense to implement it as a fixed-size `Array` of `Drink` objects. This allows for easy indexing when taking a new order based on user input of a number between 1 and 5, which results in a low cost complexity of O(1).

Trade-offs:
- Pros: fast access time due to its static size.
- Cons: has a fixed size and requires a cost complexity resize of O(n), which would be inefficient if the menu was consistently increasing in size.

### * 📝 Customer Order - LinkedList

Each customer's drink order is stored in a `LinkedList`. This allows for efficient drink insertion when adding drinks to the tail of an order (cost complexity of O(1)). Removing a specific drink (if I was to implement it) would involve a higher cost complexity of O(n) because the list must be traversed in order to find the target drink. Also, because the list is not fixed (unlike the menu `Array`), its size increases linearly with every drink added. This results in a cost complexity of O(n).

Trade-offs:
- Pros: efficient drink insertion to the tail of an order.
- Cons: does not allow indexing and is slower/less efficient with search-based drink access or removals.

### * 🕒 Order Confirmation & Open Orders Queue - Deques

Order Confirmation:
Order confirmation logic pushes confirmed orders into the open orders `Deque` (double ended queue). If the order is not confirmed, it is not added and is instead canceled/discarded. When an order is added to the `Deque`, it is appended to the end, resulting in a low cost complexity of O(1). The cost complexity for rejection is also O(1).

Open Orders Queue:
The open orders queue is the `Deque` that takes in new orders based on order confirmation logic. Orders are enqued when confirmed and dequed when completed (FIFO behavior). Enqueue has a cost complexity of O(1) and dequeue has one of O(1).

Trade-offs:
- Pros: very low cost operations (enqueue and dequeue) and FIFO order processing.
- Cons: no recovery of cancelled orders and no indexing (difficult order modification once an order is in the dequeue, which I did not implement).

Open Orders temporary Deque:
To iterate over the open orders and print them (when called from the Main Menu) open order also uses a temporary `Deque` in the `__str__` operator to safely save the contents of its main `Deque`. This way, the data in open orders can be dequeued and printed off, but safely restored by the temporary `Deque` afterwards. The cost complexity between transfers is O(n x m) and the space complexity is O(n).

Trade-offs:
- Pros: allows safe storage of the original `Deque` and its orders (especially their ordering).
- Cons: may take up excessive space/memory if the order is large/complex enough, and requires use in every open orders printout.

### * ✅ Completed Orders - ListStack

A `ListStack` is used to handle all completed orders. Orders are pushed to the `ListStack` when completed and popped off later when an end-of-day report is called. Both its push() and pop() operations have a cost complexity of O(1). The `ListStack` has a space complexity of O(n).

Trade-offs:
- Pros: low cost for operations, simple implementation, and efficient for end-of-day report calculation.
- Cons: limited order access (since it's a stack).

## 2. 🖥️ Program Running Instructions:

To run the program, you must first enter the correct password! This is an add-on from the potential bonus extensions. The program will prompt you with "Please enter password," to which you should type in "meow." The program will then provide you with a display of the Main Menu, from which you can navigate further.

## 3. 📋 Sample Runs:

Basic system functions:
### **EXAMPLE OUTPUT BEGINS HERE**

Please enter password: mew

Incorrect password.

Please enter password: meow

Password correct! Welcome!

📋 Main Menu
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. End-of-Day Report
6. Exit

Please choose an option (1-6): 1

🍹 Available Drinks:
1. Hot Cocoa - $4.00
2. Americano - $4.25
3. Latte - $5.00
4. Lemonade - $4.00
5. Iced Coffee - $3.50

Press enter to return to Main Menu:

📋 Main Menu
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. End-of-Day Report
6. Exit

Please choose an option (1-6): 2

Customer name: gabby

What drink would you like? (enter number): 2

Do you want customization? (Y)es or (N)o: y

Please type customization request: cold foam

✅ Customized order placed successfully!

Would you like to order another drink? (Y)es or (N)o?: y

What drink would you like? (enter number): 4

Do you want customization? (Y)es or (N)o: n

✅ Drink added without customization!

Would you like to order another drink? (Y)es or (N)o?: n

📝 Order Summary for gabby:
- Americano (Medium) - cold foam
- Lemonade (Medium)

Confirm this order with (Y)es or (N)o: y

✅ Order placed successfully!

Press enter to return to Main Menu:

📋 Main Menu
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. End-of-Day Report
6. Exit

Please choose an option (1-6): 3

🕒 Open Orders:
1. gabby: Americano (Medium) - cold foam, Lemonade (Medium)

Press enter to return to Main Menu:

📋 Main Menu
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. End-of-Day Report
6. Exit

Please choose an option (1-6): 4

✅ Completed Order for gabby!

Press enter to return to Main Menu:

📋 Main Menu
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. End-of-Day Report
6. Exit

Please choose an option (1-6): 5

📊 End-of-Day Report:
----------------------------------------
Drink Name            Qty Sold    Total Sales
Americano                    1          $4.25
Lemonade                     1          $4.00

Total Revenue:                          $8.25

Press enter to return to Main Menu:

📋 Main Menu
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. End-of-Day Report
6. Exit

Please choose an option (1-6): 6

Exiting system. Goodbye!

### **EXAMPLE OUTPUT ENDS HERE**

Below is an example of what happens if you enter the incorrect password too many times:
### **EXAMPLE OUTPUT BEGINS HERE**

Please enter password: frog

Incorrect password.

Please enter password: bee

Incorrect password.

Please enter password: bugs

Incorrect password.
Too many incorrect attempts. Please try again later.

### **EXAMPLE OUTPUT ENDS HERE**

## 4. 🐛 Known Bugs and Limitations:

Bugs:
- When taking multiple orders, it returns them in the wrong order.
- Does not save end-of-day report once viewed once.

## 5. 🔧 What I'd Add With More Time:

If I'd had more time on this project, I definitely would've added a way to remove drinks once they'd been ordered and a way to cancel orders. I think this is very realistic and happens all the time; we've all change our minds when ordering things before! I also would've liked to add different costs for differnt drink sizes and made the menu larger. It would've been really cool to have things other than drinks!