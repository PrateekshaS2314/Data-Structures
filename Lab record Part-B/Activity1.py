# Define the TreeNode class
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Define the BinaryTree class
class BinaryTree:
    def __init__(self):
        self.root = None

    # In-order traversal (Left, Root, Right)
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=' ')
            self.in_order_traversal(node.right)

    # Post-order traversal (Left, Right, Root)
    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=' ')

# Example usage
if __name__ == "__main__":
    # Create a binary tree manually
    tree = BinaryTree()
    tree.root = TreeNode(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    
    print("In-order Traversal:")
    tree.in_order_traversal(tree.root)

    print("\nPost-order Traversal:")
    tree.post_order_traversal(tree.root)
