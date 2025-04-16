class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self.insert_recursive(self.root, new_node)

    def insert_recursive(self, current, new_node):
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
            else:
                self.insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self.insert_recursive(current.right, new_node)

    def in_order_traversal(self, node):
        if node: 
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)

bt = BinaryTree()
bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)
bt.insert(50)

print("In-order traversal:")
bt.in_order_traversal(bt.root)
