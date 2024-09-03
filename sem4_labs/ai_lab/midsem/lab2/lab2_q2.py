class DirectedWeightedGraphgraph():
    def __init__(self,vertices):
        self.graph={}
        self.vertices=vertices
        for i in range(vertices):
            self.graph[i]=[]
    def add_edge(self,source,destination,weight):
        if source in self.graph and destination in self.graph:
            self.graph[source].append([destination,weight])
    def display_graph(self):
        for x in self.graph:
            print(x,'->',end="")
            for y in self.graph[x]:
                print(y,end="")
            print()
    def adjacenecy_matrix(self):
        matrix=[[0]*self.vertices for a in range(self.vertices)]
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
graph.adjacenecy_matrix()