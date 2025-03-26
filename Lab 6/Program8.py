class CircularNode:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        new_node = CircularNode(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr.next = new_node
                new_node = self.head
                self.head = new_node
    def traverse(self):
        if self.head is None:
            print("CLL is empty")
            return
        else:
            curr = self.head
            while True:
                print(curr.data, end="->")
                curr = curr.next
                if curr == self.head:
                    break
            print()
cll = CircularLinkedList()
cll.insert_at_beginning(10)
cll.traverse()
