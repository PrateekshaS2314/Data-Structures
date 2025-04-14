class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in range(vertices)}
    
    def add_edge(self, u, v):
        """Add a directed edge from vertex u to vertex v"""
        self.adjacency_list[u].append(v)
    
    def detect_cycle(self):
        """Detect if there's a cycle in the graph using DFS"""
        visited = [False] * self.vertices
        recursion_stack = [False] * self.vertices
        
        for vertex in range(self.vertices):
            if not visited[vertex]:
                if self._dfs_cycle_detect(vertex, visited, recursion_stack):
                    return True
        return False
    
    def _dfs_cycle_detect(self, vertex, visited, recursion_stack):
        """Helper function for DFS cycle detection"""
        visited[vertex] = True
        recursion_stack[vertex] = True
        
        for neighbor in self.adjacency_list[vertex]:
            if not visited[neighbor]:
                if self._dfs_cycle_detect(neighbor, visited, recursion_stack):
                    return True
            elif recursion_stack[neighbor]:
                return True
        
        recursion_stack[vertex] = False
        return False
# Create a graph with 4 vertices
g = Graph(4)

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)  # This creates a cycle: 0 → 2 → 0
g.add_edge(2, 3)
g.add_edge(3, 3)  # Self-loop, also a cycle

print("is a cycle detected?",g.detect_cycle())  # Output: True
