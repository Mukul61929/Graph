class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbors):
        self.graph[vertex] = neighbors

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start, end=" ")
    visited.add(start)

    for neighbor in graph.graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Construct a simple graph
#   0 -- 1
#   |    |
#   3 -- 2
graph = Graph()
graph.add_edge(0, [1, 3])
graph.add_edge(1, [0, 2])
graph.add_edge(2, [1, 3])
graph.add_edge(3, [0, 2])

# Perform DFS starting from vertex 0
print("Depth-First Traversal:")
dfs(graph, 0)
