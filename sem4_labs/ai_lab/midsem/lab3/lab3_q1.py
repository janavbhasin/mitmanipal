class Graph:
    def __init__(self, vertices):
        self.graph = {}
        self.V = vertices
        for i in range(vertices):
            self.graph[i]=[]
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i]==False:
                self.topological_sort_util(i, visited, stack)
        stack.append(v)
    def topological_sort(self):
        stack = []
        visited = [False] * self.V
        for i in range(self.V):
            if visited[i]==False:
                self.topological_sort_util(i, visited, stack)
        print(stack[::-1])
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

result = g.topological_sort()