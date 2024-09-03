class undirectedweightedgraph():
    def __init__(self,vertices):
        self.graph= {}
        self.vertices=vertices
        for vertex in vertices:
            self.graph[vertex] = []
        self.adj_matrix=[[0]*len(vertices) for _ in range(len(vertices))]
    def add_edge(self,vertex1,vertex2,weight):
        self.graph[vertex1].append([vertex2,weight])
        self.graph[vertex2].append([vertex1,weight])
        idx=self.vertices.index(vertex1)
        idy=self.vertices.index(vertex2)
        self.adj_matrix[idx][idy]=weight
        self.adj_matrix[idy][idx]=weight
    def adjacencylist(self):
        for i in self.graph:
            print(i,end="")
            for j in self.graph[i]:
                print(j,end="")
            print()
    def adjacencymatrix(self):
        for row in self.adj_matrix:
            print(row)
graph = undirectedweightedgraph(['A', 'B', 'C', 'D', 'E'])
graph.add_edge("A", "B", 1)
graph.add_edge("A", "C", 1)
graph.add_edge("A", "E", 1)
graph.add_edge("B", "C", 1)
graph.add_edge("B", "D", 1)
graph.add_edge("C", "D", 1)
graph.add_edge("C", "E", 1)
graph.adjacencylist()
graph.adjacencymatrix()