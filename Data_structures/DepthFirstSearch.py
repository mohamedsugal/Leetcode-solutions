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


g = Graph()
# g.addEdge(1, 2)
# g.addEdge(1, 3)
# g.addEdge(2, 4)
# g.addEdge(2, 5)
# g.addEdge(3, 5)
# g.addEdge(4, 6)
# g.addEdge(5, 6)
# g.addEdge(6, 7)

g.addEdge('A', 'F')
g.addEdge('F', 'C')
g.addEdge('C', 'B')
g.addEdge('C', 'E')
g.addEdge('B', 'H')
g.addEdge('H', 'E')
g.addEdge('E', 'D')
g.addEdge('D', 'G')
g.addEdge('G', 'I')
g.addEdge('I', 'A')


g.printGraph()

print("Depth First Search Traversal:")
g.DFS('D')
print()

#               1
#             /  \
#            2    3
#           | \  /
#           4  5
#           \ /
#            6 -- 7
# https://www.koderdojo.com/media/default/articles/directed-acyclic-graph-computer-science.png

# def DFS(self, start):
#     stack = []
#     visited = [False] * self.E
#     visited[start] = True
#     stack.append(start)
#     while stack:
#         current = stack.pop()
#         print(current, end=' ')
#         for i in self.graph[current]:
#             if not visited[i]:
#                 stack.append(i)
#                 visited[i] = True
