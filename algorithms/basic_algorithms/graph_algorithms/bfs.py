'''
Breadth-First Search (BFS): Explore all nodes at the current depth before moving to the next depth level.

'''


def bfs(graph, start):
    """
    Perform a breadth-first search on the graph starting from the given node.

    :param graph: A dictionary representing the adjacency list of the graph.
    :param start: The starting node for the BFS.
    :return: A list of nodes in the order they were visited.
    """
    visited = set()  # Set to keep track of visited nodes
    queue = [start]  # Initialize a queue with the starting node
    order_of_visit = []  # List to record the order of visit

    while queue:
        current_node = queue.pop(0)  # Dequeue a node from the front of the queue
        if current_node not in visited:
            visited.add(current_node)  # Mark the node as visited
            order_of_visit.append(current_node)  # Record the visit
            # Enqueue all unvisited neighbors
            queue.extend(neighbor for neighbor in graph[current_node] if neighbor not in visited)

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
    visited_order = bfs(graph, start_node)
    print("Order of visit:", visited_order)
    # Output: Order of visit: ['A', 'B', 'C', 'D', 'E', 'F']