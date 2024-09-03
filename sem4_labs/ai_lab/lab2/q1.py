class undirectedgraph:
    def __init__(self):
        self.graph={}
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 not in self.graph[vertex1]:
                self.graph[vertex1].append(vertex2)
            if vertex1 not in self.graph[vertex2]:
                self.graph[vertex2].append(vertex1)
        else:
            print("error")
    def display_graph(self):
        for vertex in self.graph:
            print(f"{vertex} —> {' '.join(map(str, self.graph[vertex]))}")
graph=undirectedgraph()
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