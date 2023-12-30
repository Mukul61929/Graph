class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {vertex: [] for vertex in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

def dfs(graph, node, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def count_trees(graph):
    vertices = graph.vertices
    visited = [False] * vertices
    tree_count = 0

    for node in range(vertices):
        if not visited[node]:
            dfs(graph.graph, node, visited)
            tree_count += 1

    return tree_count

# Construct a forest (disjoint trees)
#   0   3   5
#   |   |   |
#   1   2   4
forest_graph = Graph(6)
forest_graph.add_edge(0, 1)
forest_graph.add_edge(3, 2)
forest_graph.add_edge(5, 4)

# Count the number of trees in the forest
result = count_trees(forest_graph)
print("Number of trees in the forest:", result)
