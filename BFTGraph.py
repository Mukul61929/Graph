from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbors):
        self.graph[vertex] = neighbors

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        current_vertex = queue.popleft()
        print(current_vertex, end=" ")

        for neighbor in graph.graph[current_vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Example usage:
# Construct a simple graph
#   0 -- 1
#   |    |
#   3 -- 2
graph = Graph()
graph.add_edge(0, [1, 3])
graph.add_edge(1, [0, 2])
graph.add_edge(2, [1, 3])
graph.add_edge(3, [0, 2])

# Perform BFS starting from vertex 0
print("Breadth-First Traversal:")
bfs(graph, 0)
