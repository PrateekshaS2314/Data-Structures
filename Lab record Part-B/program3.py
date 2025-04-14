class TreeNode: 
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None 

class BinaryTree: 
    def __init__(self): 
        self.root = None 

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left:
                self._insert_recursive(current.left, data)
            else:
                current.left = TreeNode(data)
        else:
            if current.right:
                self._insert_recursive(current.right, data)
            else:
                current.right = TreeNode(data)

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

# Helper function to find a node by its value
def find_node(current, node_value): 
    if current is None: 
        return None 
    if current.data == node_value: 
        return current 
    left_node = find_node(current.left, node_value) 
    if left_node: 
        return left_node 
    return find_node(current.right, node_value) 

# Function to find grandchildren of a node by its value
def find_grandchildren_values(bt, node_value): 
    node = find_node(bt.root, node_value) 
    if node: 
        return bt.find_grandchildren(node) 
    else: 
        return [] 

# Example usage
bt = BinaryTree()

# Insert the specified nodes
nodes_to_insert = [50, 30, 70, 20, 40, 60, 80, 15, 25, 35, 45, 65, 75, 85]
for value in nodes_to_insert:
    bt.insert(value)

# Find and print grandchildren of node 30
grandchildren_30 = find_grandchildren_values(bt, 30)
print("Grandchildren of node 30:", grandchildren_30)
