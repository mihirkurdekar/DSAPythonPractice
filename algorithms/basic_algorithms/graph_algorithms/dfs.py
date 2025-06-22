'''
Depth-First Search (DFS): Explore as far as possible along each branch before backtracking.

'''

def dfs(graph, start, visited=None):
    """
    Perform a depth-first search on the graph starting from the given node.

    :param graph: A dictionary representing the adjacency list of the graph.
    :param start: The starting node for the DFS.
    :param visited: A set to keep track of visited nodes (used for recursion).
    :return: A list of nodes in the order they were visited.
    """
    if visited is None:
        visited = set()  # Initialize visited set if not provided

    visited.add(start)  # Mark the current node as visited
    order_of_visit = [start]  # Record the visit

    # Recur for all unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            order_of_visit.extend(dfs(graph, neighbor, visited))

    return order_of_visit

# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    start_node = 'A'
    visited_order = dfs(graph, start_node)
    print("Order of visit:", visited_order)
    # Output: Order of visit: ['A', 'B', 'D', 'E', 'F', 'C']