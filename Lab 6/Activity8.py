class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newnode
            newnode.next = self.head

    def deleteBeginning(self):
        if self.head is None:
            print("Empty")
        elif self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            self.head = self.head.next
            current.next = self.head
cll = CircularLinkedList()
cll.insertEnd(10)
cll.insertEnd(20)
cll.insertEnd(30)
cll.deleteBeginning()
