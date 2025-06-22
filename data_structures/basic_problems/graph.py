# Problem: Given a graph, find all connected components.
# Example:
# Code
# A -> B
# B -> C
# D -> E
# Output: [['A', 'B', 'C'], ['D', 'E']]

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def _dfs(self, node, visited, component):
        visited.add(node)
        component.append(node)
        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                self._dfs(neighbor, visited, component)

    def connected_components(self):
        visited = set()
        components = []
        for node in self.graph:
            if node not in visited:
                component = []
                self._dfs(node, visited, component)
                components.append(component)
        return components


# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('D', 'E')

    components = g.connected_components()
    print("Connected Components:", components)  # Output: [['A', 'B', 'C'], ['D', 'E']]