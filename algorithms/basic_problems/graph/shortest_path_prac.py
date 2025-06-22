'''
Given a graph, find the shortest path between two nodes using Dijkstra's algorithm.
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

    def dijkstra2(self,start,end):
        s= start
        queue = [(0,s)]
        distances = {}

        while queue:
            if end in distances:
                break
            w1,n1 = heapq.heappop(queue)
            if n1 in distances:
                continue
            distances[n1] = w1

            for n2,w2 in self.graph[n1]:
                heapq.heappush(queue, (w1 + w2, n2))
        
        return distances


    def dijkstra(self, start):

        s= start
        queue = [(0,s)]
        distances = {}

        while queue:
            w1,n1 = heapq.heappop(queue)
            if n1 in distances:
                continue
            distances[n1] = w1
            #print(self.graph[n1])
            for n2,w2 in self.graph[n1]:
                heapq.heappush(queue, [w1+w2, n2])         

        return distances    




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
    # for node, edges in g.graph.items():
    #     for edge in edges:
    #         print(f"{node} -> {edge[0]} (weight {edge[1]})")

    distances = g.dijkstra2(start,end)
    print(distances)
    print(distances[end])
    