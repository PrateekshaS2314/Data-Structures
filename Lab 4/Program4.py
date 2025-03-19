class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
            return
        
        # Traverse to the end of the list
        last = self.head
        while last.next:
            last = last.next
        
        # Insert the new node at the end
        last.next = new_node

    # Delete a node
    def delete_node(self, data):
        current = self.head

        # If the node to be deleted is the head node
        if current and current.data == data:
            self.head = current.next  # Change the head to the next node
            current = None
            return

        prev = None
        # Traverse the list to find the node to delete
        while current and current.data != data:
            prev = current
            current = current.next
        
        # If the node isn't found
        if current is None:
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None

    # Traverse the list
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()

# Example usage
linked_list = LinkedList()

# Insert elements at the beginning
linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
print("Linked list after inserting 20, 10 at the beginning:")
linked_list.traverse()

# Insert elements at the end
linked_list.insert_at_end(30)
linked_list.insert_at_end(40)
print("\nLinked list after inserting 30, 40 at the end:")
linked_list.traverse()

# Delete a node
linked_list.delete_node(20)
print("\nLinked list after deleting node with data 20:")
linked_list.traverse()

# Traverse the list
print("\nTraversing the linked list:")
linked_list.traverse
