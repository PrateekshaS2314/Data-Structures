class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    def display_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
linked_list = SinglyLinkedList()
linked_list.append_node(1)
linked_list.append_node(2)
linked_list.append_node(3)

print("List:")
linked_list.display_list()

print("Search for 2:", linked_list.search_node(2))
print("Search for 4:", linked_list.search_node(4))
