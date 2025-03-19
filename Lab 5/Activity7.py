class DoublyNode:
    def __init__(self, data):
        self.data = data  
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None  

    def append(self, data):
       
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            new_node.prev = last_node

    def delete_node(self, data):
       
        current = self.head
       
       
        if not current:
            print("List is empty.")
            return
       
        if current.data == data:
            if current.next:  
                self.head = current.next
                self.head.prev = None
            else:
                self.head = None
            current = None
            return
       
        while current:
            if current.data == data:
                if current.next:  
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else:
                    current.prev.next = None
                current = None
                return
            current = current.next
       
        print(f"Node with data {data} not found.")

    def traverse_backward(self):
        """Method to traverse the list backward and print the data"""
        current = self.head
       
        if not current:
            print("List is empty.")
            return
       
        while current.next:
            current = current.next
       
        while current:
            print(current.data, end=" <-> " )
            current = current.prev
        print()


# Example usage:
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Original List (backward traversal):")
dll.traverse_backward()

# Deleting a node
dll.delete_node(20)

print("\nList after deleting 20 (backward traversal):")
dll.traverse_backward()

dll.delete_node(50)  
