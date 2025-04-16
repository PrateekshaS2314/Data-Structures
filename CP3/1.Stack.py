class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_item = self.top
        self.top = self.top.next
        return popped_item.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def __str__(self):
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        return "->".join(elements) if elements else "Stack is empty"

stack = Stack()
print("Is stack empty?", stack.is_empty())
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print("Top element of stack:", stack.peek())
print("Is stack empty?", stack.is_empty())
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print("Is stack empty?", stack.is_empty())
