from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):
        for node in self.graph:
            print(f'{node} -> {self.graph[node]}')

    def BFS(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def DFS(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            print(node, end=" ")
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


graph = Graph()
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(3, 5)
graph.addEdge(2, 4)
graph.addEdge(2, 5)
graph.addEdge(5, 6)
graph.addEdge(6, 7)


# graph.printGraph()

print("Breadth First Search: ")
graph.BFS(1)
print("\n")
print("Depth First Search: ")
graph.DFS(1)
print()
