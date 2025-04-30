from datastructures.deque import Deque
from datastructures.liststack import ListStack
from projects.project3.Customer_Order import Customer_Order

# Orderqueue = dequeue (linkedlist)
# Open order queue = dequeue

class Order_Queue:
    def __init__(self):
        self._queue = Deque(data_type = Customer_Order) # an active orders queue
        self._complete = ListStack(data_type = Customer_Order) # a completed order liststack
        
    def add_order(self, customer_order: Customer_Order) -> None:  
        self._queue.enqueue(customer_order) # adds an order to the end of the queue

    def get_front_order(self) -> Customer_Order:
        return self._queue.front() # returns the order at the front of the active queue (next to be completed)
    
    def complete_order(self) -> None:  
        done = self._queue.dequeue() # assigns the top returned value from the active order queue to done
        self._complete.push(done) # pushes the complete order to the completed liststack
        return
        
    def end_of_day_report(self):
        drink_summary = {}
        total_revenue = 0.0
        while not self._complete.empty:
            order = self._complete.pop()
            for drink in order._order: # linkedlist
                name = drink.name
                drink_summary[name] = drink_summary.get(name, {'count': 0, 'revenue': 0.0})
                drink_summary[name]["count"] += 1
                drink_summary[name]["revenue"] += drink.price
                total_revenue += drink.price

        print("\nEnd-of-Day Report:")
        for drink, stats in drink_summary.items():
            print(f"{drink}: {stats["count"]} sold, ${stats["revenue"]:.2f}")
        print(f"Total Revenue: ${total_revenue:.2f}")

    # Dequeue of open orders

    def __str__(self):
        if self._queue._list.empty:
            return "🕒 No Open Orders."

        result = ["\n🕒 Open Orders:"]
        temp_queue = Deque(data_type=Customer_Order)
        count = 1

        while not self._queue._list.empty:
            order = self._queue.dequeue()
            drink_list = []
            for drink in order._order:
                line = f"{drink.name} ({drink.size})"
                if drink.customization:
                    line += f" - {drink.customization}"
                drink_list.append(line)
            result.append(f"{count}. {order.name}: " + ", ".join(drink_list))
            temp_queue.enqueue(order)
            count += 1

        # Restore original queue state
        while not temp_queue._list.empty:
            self._queue.enqueue(temp_queue.dequeue())

        return "\n".join(result)

    

    '''def view_open_orders(self):
        if self._queue._list.empty:
            print("No open orders.")
            return
        
        print("\n🕒 Open Orders:")
        temp_queue = Deque(data_type = Customer_Order) #??? preserve order?

        while not self._queue._list.empty:
            order = self._queue.dequeue()
            print(f"- {order.name}:")
            order.repeat_order()
            temp_queue.enqueue(order)

        # original queue
        while not temp_queue._list.empty:
            self._queue.enqueue(temp_queue.dequeue())'''
