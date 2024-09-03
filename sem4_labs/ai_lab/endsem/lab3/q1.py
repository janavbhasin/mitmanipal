class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph={}
        for i in range(self.vertices):
            self.graph[i]=[]
    def add_edge(self,u,v):
        self.graph[u].append(v)
    def topological_sort(self,v,visited,stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topological_sort(i,visited,stack)
        stack.append(v)
    def topo(self):
        visited=[]
        stack=[]
        for i in range(self.vertices):
            if i not in visited:
                self.topological_sort(i,visited,stack)
        return stack[::-1]
g=Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

result = g.topo()
print("Topological ordering:", result)