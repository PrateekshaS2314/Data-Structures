from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, v, w):
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[v].append(w)

        # If undirected, also add the reverse edge
        if w not in self.adj_list:
            self.adj_list[w] = []
        self.adj_list[w].append(v)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])

        print("BFS traversal order:")
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                for neighbor in self.adj_list.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

g.bfs(0)
