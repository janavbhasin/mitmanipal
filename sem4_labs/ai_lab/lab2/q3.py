class undirectedweightedgraph:
    def __init__(self):
        self.graph={}
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]={}
    def add_edge(self,vertex1,vertex2,weight):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1][vertex2] = weight
            self.graph[vertex2][vertex1] = weight
    def display_adjacency_list(self):
        print("adjacenecy list:")
        for vertex,neighbours in self.graph.items():
            print(f"{vertex}:[{''.join(neighbours.keys())}]")
    def display_adjacency_matrix(self):
        print("adjacency matrix")
        vertices=sorted(list(self.graph.keys()))
        matrix_size=len(vertices)
        matrix = [[0] * matrix_size for _ in range(matrix_size)]
        for i, vertex1 in enumerate(vertices):
            for j, vertex2 in enumerate(vertices):
                if vertex2 in self.graph[vertex1]:
                    print(i,' ',j,' ',vertex1,' ',vertex2)
                    matrix[i][j] = self.graph[vertex1][vertex2]
        for row in matrix:
            print(row)
graph = undirectedweightedgraph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_edge("A", "B", 1)
graph.add_edge("A", "C", 1)
graph.add_edge("A", "E", 1)
graph.add_edge("B", "C", 1)
graph.add_edge("B", "D", 1)
graph.add_edge("C", "D", 1)
graph.add_edge("C", "E", 1)
graph.display_adjacency_matrix()
graph.display_adjacency_list()