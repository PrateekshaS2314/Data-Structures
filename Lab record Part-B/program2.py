class TreeNode: 
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None 

class BinaryTree: 
    def __init__(self): 
        self.root = None 

    def find_lca(self, node1, node2): 
        # Check if both nodes are in the tree 
        if not self._find_node(self.root, node1) or not self._find_node(self.root, node2):  
            return None 
        return self._find_lca_recursive(self.root, node1, node2) 

    def _find_lca_recursive(self, current, node1, node2): 
        if current is None: 
            return None 
        
        # If current node is one of the nodes we are looking for, return it 
        if current.data == node1 or current.data == node2: 
            return current
        
        # Recursively search in the left and right subtrees 
        left_lca = self._find_lca_recursive(current.left, node1, node2) 
        right_lca = self._find_lca_recursive(current.right, node1, node2) 
        
        # If both sides return non-null, current is the LCA
        if left_lca and right_lca: 
            return current 
        
        # Otherwise, return the non-None value (either left_lca or right_lca)
        return left_lca if left_lca is not None else right_lca 

    def _find_node(self, current, target): 
        if current is None: 
            return False 
        if current.data == target: 
            return True 
        return self._find_node(current.left, target) or self._find_node(current.right, target) 

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

# Finding the Lowest Common Ancestor (LCA) of nodes
lca_node = bt.find_lca(4, 5) 
print(f"LCA of nodes 4 and 5: {lca_node.data if lca_node else 'Not found'}") 

lca_node = bt.find_lca(4, 6)
print(f"LCA of nodes 4 and 6: {lca_node.data if lca_node else 'Not found'}") 

lca_node = bt.find_lca(3, 7) 
print(f"LCA of nodes 3 and 7: {lca_node.data if lca_node else 'Not found'}") 
