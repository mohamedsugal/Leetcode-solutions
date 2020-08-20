from collections import defaultdict

class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list)

    def addEdge(self, u, v): 
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def printGraph(self): 
        for i in self.graph.keys():
            print(i, '->', ' -> '.join([str(j) for j in self.graph[i]]))

    def BFS(self, start): 
        explored = set()
        queue = [start]
        explored.add(start)
        while queue: 
            v = queue.pop(0)
            print(v, end=" ")
            for w in self.graph[v]: 
                if w not in explored: 
                    explored.add(w)
                    queue.append(w)
            
    def DFS(self, start): 
        explored = set()
        stack = [start]
        while stack: 
            v = stack.pop()
            if v in explored: 
                continue
            explored.add(v)
            print(v, end=" ")
            for w in self.graph[v]:
                if w not in explored: 
                    stack.append(w)

graph = Graph()
graph.addEdge(1, 2)
graph.addEdge(1, 4)
graph.addEdge(4, 3)
graph.addEdge(3, 9)
graph.addEdge(3, 10)
graph.addEdge(2, 3)
graph.addEdge(2, 5)
graph.addEdge(2, 7)
graph.addEdge(2, 8)
graph.addEdge(5, 8)
graph.addEdge(5, 6)
graph.addEdge(5, 7)
graph.addEdge(7, 8)

# graph.printGraph()

print("Breadth First Search: ")
graph.BFS(5)
print("\n")
print("Depth First Search: ")
graph.DFS(5)
print()
