from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)
        self.adjacency_list[w].append(v)  # Assuming it's an undirected graph

    def bfs_shortest_path(self, start_vertex, target_vertex):
        if start_vertex == target_vertex:
            return 0
        queue = deque([(start_vertex, 0)])  # (vertex, distance)
        visited = set([start_vertex])

        while queue:
            vertex, distance = queue.popleft()
            for neighbor in self.adjacency_list[vertex]:
                if neighbor == target_vertex:
                    return distance + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return -1  # No path found

class SocialNetwork:
    def __init__(self):
        self.graph = Graph()

    def add_friendship(self, user1, user2):
        self.graph.add_edge(user1, user2)

    def degrees_of_separation(self, user1, user2):
        return self.graph.bfs_shortest_path(user1, user2)

# Example usage:
network = SocialNetwork()

# Adding friendships:
network.add_friendship('A', 'B')
network.add_friendship('B', 'C')
network.add_friendship('C', 'D')
network.add_friendship('D', 'E')
network.add_friendship('E', 'F')
network.add_friendship('F', 'G')
network.add_friendship('G', 'H')
network.add_friendship('H', 'I')
network.add_friendship('I', 'J')

# Finding degrees of separation
print("Degrees of separation between 'A' and 'E':", network.degrees_of_separation('A', 'E'))
print("Degrees of separation between 'A' and 'J':", network.degrees_of_separation('A', 'J'))
print("Degrees of separation between 'A' and 'Z':", network.degrees_of_separation('A', 'Z'))  # Non-existent user

# Additional example with numeric users:
numeric_network = SocialNetwork()
numeric_network.add_friendship(0, 1)
numeric_network.add_friendship(0, 2)
numeric_network.add_friendship(1, 3)
numeric_network.add_friendship(2, 4)
numeric_network.add_friendship(3, 5)
numeric_network.add_friendship(4, 5)

print("Degrees of separation between users 0 and 5:", numeric_network.degrees_of_separation(0, 5))
