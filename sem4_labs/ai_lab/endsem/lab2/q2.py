class DirectedWeightedGraphgraph:
    def __init__(self,vertices):
        self.graph={}
        self.vertices=vertices
        for i in range(vertices):
            self.graph[i]=[]
    def add_edge(self,u,v,w):
        if u in self.graph and v in self.graph:
            self.graph[u].append([v,w])
    def display_graph(self):
        for source in self.graph:
            print(source,'->',self.graph[source])
    def display_adjacencymatrix(self):
        matrix=[[0]*self.vertices for _ in range(self.vertices)]
        for i in self.graph:
            for destination,weight in self.graph[i]:
                matrix[i][destination]=weight
        for row in matrix:
            print(row)
graph=DirectedWeightedGraphgraph(6)
graph.add_edge(0,1,6)
graph.add_edge(1,2,7)
graph.add_edge(2,1,4)
graph.add_edge(2,0,5)
graph.add_edge(3,2,10)
graph.add_edge(4,5,1)
graph.add_edge(5,4,3)
graph.display_graph()
graph.display_adjacencymatrix()