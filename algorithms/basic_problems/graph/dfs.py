'''
Implement DFS to traverse a graph and detect cycles.
'''

def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()  # To keep track of visited nodes
    if path is None:
        path = []  # To keep track of the current path

    visited.add(start)  # Mark the current node as visited
    path.append(start)  # Add the current node to the path

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)
        elif neighbor in path:
            print(f"Cycle detected: {' -> '.join(path + [neighbor])}")

    path.pop()  # Remove the current node from the path after exploring all neighbors

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
    print("DFS traversal starting from node A:")
    dfs(graph, 'A')
    # Output should show the path and any cycles detected