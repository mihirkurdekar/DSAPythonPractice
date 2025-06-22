'''
Given a graph, find the shortest path between two nodes using Dijkstra's algorithm.
'''

import heapq

def dijkstra(graph, start, end):
    # Priority queue to store (distance, node)
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph}  # Initialize distances
    distances[start] = 0  # Distance to the start node is 0
    previous_nodes = {node: None for node in graph}  # To reconstruct the path

    while queue:
        current_distance, current_node = heapq.heappop(queue)  # Get the node with the smallest distance

        if current_distance > distances[current_node]:
            continue  # Skip if we have already found a better path

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:  # Found a shorter path to neighbor
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Reconstruct the shortest path from start to end
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    
    path.reverse()  # Reverse the path to get it from start to end
    return path, distances[end]  # Return the shortest path and its distance

# Example usage:
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 2, 'E': 5},
        'C': {'A': 4, 'F': 1},
        'D': {'B': 2, 'E': 3},
        'E': {'B': 5, 'D': 3, 'F': 2},
        'F': {'C': 1, 'E': 2}
    }
    start_node = 'A'
    end_node = 'F'
    path, distance = dijkstra(graph, start_node, end_node)
    print(f"Shortest path from {start_node} to {end_node}: {path} with distance {distance}")
    # Output should be: Shortest path from A to F: ['A', C, 'F'] with distance 5