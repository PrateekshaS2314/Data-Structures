class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, v, w):
        # Add edge from v to w
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[v].append(w)

        # If it's an undirected graph, add edge from w to v as well
        if w not in self.adj_list:
            self.adj_list[w] = []
        self.adj_list[w].append(v)

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} -> {' -> '.join(map(str, self.adj_list[vertex]))}")

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

g.print_graph()
