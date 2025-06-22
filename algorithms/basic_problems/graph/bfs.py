'''
Given a graph, implement BFS to traverse the graph and print all nodes.
'''

def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = [start]  # Initialize the queue with the starting node

    while queue:
        node = queue.pop(0)  # Dequeue a node from the front of the queue
        if node not in visited:
            print(node)  # Process the node (e.g., print it)
            visited.add(node)  # Mark the node as visited
            # Enqueue all unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Example usage:
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print("BFS traversal starting from node A:")
    bfs(graph, 'A')
    # Output should be: A B C D E F