class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, source):
        distance = [float("inf")] * self.V
        predecessor = [None] * self.V
        distance[source] = 0

        # Relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if distance[u] != float("inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u

        # Check for negative weight cycles
        for u, v, w in self.graph:
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                print("Graph contains negative weight cycle")
                return

        return distance, predecessor

def print_shortest_paths(distance, predecessor, source):
    for i, dist in enumerate(distance):
        if dist == float("inf"):
            print(f"Shortest path from {source} to {i}: No path exists.")
        else:
            path = []
            j = i
            while j is not None:
                path.append(j)
                j = predecessor[j]
            path.reverse()
            print(f"Shortest path from {source} to {i}: {' -> '.join(map(str, path))}, Distance = {dist}")

# Example usage
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

source_vertex = 0
distance, predecessor = g.bellman_ford(source_vertex)
print_shortest_paths(distance, predecessor, source_vertex)
