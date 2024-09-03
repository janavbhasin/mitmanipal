class graph():
    def __init__(self,vertices):
        self.v=vertices
        self.graph={}
        for i in vertices:
            self.graph[i]=[]
    def add_edge(self,u,v):
        self.graph[u].append(v)
    def iscyclic(self,v,visited,recstack):
        visited[v]=True
        recstack[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                if self.iscyclic(i,visited,recstack)==True:
                    return True
            elif recstack[i]==True:
                return True
        recstack[v]=False
        return False
    def cyclic(self):
        visited=[False]*len(self.v)
        recstack=[False]*len(self.v)
        for i in self.graph:
            if  visited[i]==False:
                if self.iscyclic(i,visited,recstack)==True:
                    return True
        return False
g=graph([0,1,2,3])
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,0)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,3)
if g.cyclic()==True:
	print("graph contains cycle")
else:
	print("graph doesnt have cycles")