# Node class to represent each element in the queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class using singly linked list
class Queue:
    def __init__(self):
        self.front = None 
        self.rear = None

    # Enqueue operation
    def enqueue(self, data):
         new_node = Node(data)
         if self.rear is None:
             self.front = self.rear = new_node
             print(f"new node: {new_node.data}")
             return
         else:
             self.rear.next = new_node
             self.rear = new_node

    # Return front node data without removing
    def Front(self):
        if self.front is None:
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None


    # Dequeue operation
    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

# Function to simulate customer service
q=Queue()
print("is queue empty?\n",q.is_empty())
def serve_customers():
    # Enqueue 5 customers
    customer_ids = [101, 102, 103, 104, 105]
    print("Enqueuing customers...")
    for cid in customer_ids:
        print(f"Customer {cid} added to the queue.")
        q.enqueue(cid)
    print("is the queue empty?\n",q.is_empty())
    print("\nServing customers:")
    while not q.is_empty():
        current_customer = q.dequeue()
        print(f"Serving customer with ID: {current_customer}")

    # Check if queue is empty
    if q.is_empty():
        print("is the queue empty?\n",q.is_empty())
        print("\nAll customers have been served. Queue is now empty.")
    else:
        print("There are still customers in the queue.")

# Run the simulation
serve_customers()
