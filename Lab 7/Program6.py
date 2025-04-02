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
q = Queue()
q.Enqueue(30)
q.Enqueue(20)
q.Enqueue(10)
q.Dequeue()
q.Dequeue()
q.Dequeue()
q.Dequeue()
