class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        new_node = DoublyNode(data)  
        new_node.prev = None
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        return self.head
    def insert_at_end(self,data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
    def traverse_forward(self):
        current = self.head
        while current is not None:
            print(current.data, end =" ")
            current = current.next
        print()
dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
print("Doubly linked list after inserting 20, 10 at the beginning:")
dll.traverse_forward()

dll.insert_at_end(30)
dll.insert_at_end(40)
print("\nDoubly linked list after inserting 30, 40 at the end:")
dll.traverse_forward()

print("\nTraversing the doubly linked list forward:")
dll.traverse_forward() 
