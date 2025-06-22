'''
Problem: Given a graph, find the shortest path between two nodes using Dijkstra's algorithm.
Example:
Code
A -> B (weight 2)
A -> C (weight 4)
B -> D (weight 1)
C -> D (weight 3)
Output: A -> B -> D (shortest path from A to D)
'''

import heapq
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # For undirected graph

    def dijkstra(self, start, end):
        # Priority queue to store (distance, node)
        pq = [(0, start)]
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        previous_nodes = {node: None for node in self.graph}

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        # Reconstruct the shortest path
        path = []
        current_node = end
        while current_node is not None:
            path.append(current_node)
            current_node = previous_nodes[current_node]
        path.reverse()

        return path if distances[end] != float('inf') else None

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'D', 1)
    g.add_edge('C', 'D', 3)

    start = 'A'
    end = 'D'

    # print graph
    print("Graph edges:")
    for node, edges in g.graph.items():
        for edge in edges:
            print(f"{node} -> {edge[0]} (weight {edge[1]})")

    shortest_path = g.dijkstra(start, end)

    if shortest_path:
        print("Shortest path from", start, "to", end, "is:", " -> ".join(shortest_path))
    else:
        print("No path found from", start, "to", end)