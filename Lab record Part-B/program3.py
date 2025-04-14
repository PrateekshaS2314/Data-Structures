class TreeNode: 
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None 

class BinaryTree: 
    def __init__(self): 
        self.root = None 

    def find_grandchildren(self, node): 
        if not node: 
            return [] 

        grandchildren = [] 
        if node.left: 
            grandchildren.extend(self._get_children_values(node.left)) 
        if node.right: 
            grandchildren.extend(self._get_children_values(node.right)) 
        return grandchildren 

    def _get_children_values(self, parent): 
        children_values = [] 
        if parent.left: 
            children_values.append(parent.left.data) 
        if parent.right: 
            children_values.append(parent.right.data)
        return children_values 

# Helper function to find a node by value
def find_node(current, node_value): 
    if current is None: 
        return None 
    if current.data == node_value: 
        return current 
    left_node = find_node(current.left, node_value) 
    if left_node: 
        return left_node 
    return find_node(current.right, node_value) 

# Function to find grandchildren of a node by value
def find_grandchildren_values(bt, node_value): 
    node = find_node(bt.root, node_value) 
    if node: 
        return bt.find_grandchildren(node) 
    else: 
        return [] 

# Example usage: 
bt = BinaryTree() 
# Constructing the binary tree 
bt.root = TreeNode(1) 
bt.root.left = TreeNode(2) 
bt.root.right = TreeNode(3) 
bt.root.left.left = TreeNode(4) 
bt.root.left.right = TreeNode(5) 
bt.root.right.left = TreeNode(6) 
bt.root.right.right = TreeNode(7) 

# Testing the function with various nodes
print("Grandchildren of node 1:", find_grandchildren_values(bt, 1))
print("Grandchildren of node 2:", find_grandchildren_values(bt, 2))
print("Grandchildren of node 3:", find_grandchildren_values(bt, 3))
print("Grandchildren of node 4:", find_grandchildren_values(bt, 4))
print("Grandchildren of node 5:", find_grandchildren_values(bt, 5))
print("Grandchildren of node 6:", find_grandchildren_values(bt, 6))
print("Grandchildren of node 7:", find_grandchildren_values(bt, 7))
