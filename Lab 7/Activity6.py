class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def Enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            print(f"new node: {new_node.data}")
            return
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueue item is {self.rear.data}")

    def Dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            self.front = temp.next
            deleted_item = temp.data
            del(temp)
            temp = None
            print(f"Dequeued item from the queue is {deleted_item}")

    def is_empty(self):
        return self.front is None

    def get_front(self):
        if self.front:
            return self.front.data
        return None

# Example usage:
q = Queue()
print("Is queue empty?\n", q.is_empty())
print("Front element is:", q.get_front())
q.Enqueue(30)
q.Enqueue(20)
q.Enqueue(10)
print("Is queue empty?\n", q.is_empty())
q.Dequeue()
q.Dequeue()
q.Dequeue()
q.Dequeue()
print("Is queue empty?\n", q.is_empty())
