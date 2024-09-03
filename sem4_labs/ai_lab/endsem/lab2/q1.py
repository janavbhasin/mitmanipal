class UndirectedGraph:
    def __init__(self):
        self.graph={}
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def add_edge(self,v1,v2):
        if v1 in self.graph and v2 in self.graph:
            if v1 not in self.graph[v2]:
                self.graph[v2].append(v1)
            if v2 not in self.graph[v1]:
                self.graph[v1].append(v2)
    def display_graph(self):
        for vertex in self.graph:
            print(vertex,'->',self.graph[vertex])
graph=UndirectedGraph()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2,1)
graph.add_edge(2,0)
graph.add_edge(3,2)
graph.add_edge(4,5)
graph.add_edge(5,4)
graph.display_graph()