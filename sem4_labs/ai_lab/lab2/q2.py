class DirectedWeightedGraphgraph:
    def __init__(self):
        self.graph={}
    def add_vertex(self,vertex):
        self.graph[vertex]={}
    def add_edge(self,source,destination,weight):
        if source in self.graph and destination in self.graph:
            self.graph[source][destination]=weight
    def display_graph(self):
        for source in self.graph:
            for destination, weight in self.graph[source].items():
                print(f"{source} -> {destination},{weight}")
graph=DirectedWeightedGraphgraph()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_edge(0,1,6)
graph.add_edge(1,2,7)
graph.add_edge(2,1,4)
graph.add_edge(2,0,5)
graph.add_edge(3,2,10)
graph.add_edge(4,5,1)
graph.add_edge(5,4,3)
graph.display_graph()