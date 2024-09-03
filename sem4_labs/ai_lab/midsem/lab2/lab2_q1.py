class Undirectedgraph():
    def __init__(self,vertices):
        self.graph={}
        self.vertices=vertices
        for i in range(vertices):
            self.graph[i]=[]
    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 not in self.graph[vertex1]:
                self.graph[vertex1].append(vertex2)
            if vertex1 not in self.graph[vertex2]:
                self.graph[vertex2].append(vertex1)
    def display_graph(self):
        for i in self.graph:
            print(i,'->',self.graph[i])
    def adjacenecy_matrix(self):
        lis=[]
        for i in range(self.vertices):
            l=[]
            for vertex in range(self.vertices):
                if vertex in self.graph[i]:
                    l.append(1)
                else:
                    l.append(0)
            lis.append(l)
        for row in lis:
            print(row)
graph=Undirectedgraph(6)
graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2,1)
graph.add_edge(2,0)
graph.add_edge(3,2)
graph.add_edge(4,5)
graph.add_edge(5,4)
graph.display_graph()
graph.adjacenecy_matrix()