class Graph():
    def __init__(self,vertices):
        self.V=vertices
        self.graph={}
        for i in range(self.V):
            self.graph[i]=[]
    def add_edge(self,u,v):
        self.graph[u].append(v)
    def toposort(self):
        in_degree=[0]*self.V
        for i in range(self.V):
            for j in self.graph[i]:
                in_degree[j]+=1
        queue=[]
        for i in range(self.V):
            if in_degree[i]==0:
                queue.append(i)
        result=[]
        while queue:
            node=queue.pop()
            for i in self.graph[node]:
                in_degree[i]-=1
                if in_degree[i]==0:
                    queue.append(i)
            result.append(node)
        print(result)
if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(3, 1)
    g.add_edge(2, 3)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    
    print("Topological Sort is:")
    g.toposort()