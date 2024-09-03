class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph={}
        for i in range(vertices):
            self.graph[i]=[]
    def add_edge(self,u,v):
        self.graph[u].append(v)
    def iscycle(self):
        in_degree=[0]*self.vertices
        for i in range(self.vertices):
            for j in self.graph[i]:
                in_degree[j]+=1
        queue=[]
        for i in range(self.vertices):
            if in_degree[i]==0:
                queue.append(i)
        cnt=0
        while queue:
            node=queue.pop()
            for i in self.graph[node]:
                in_degree[i]-=1
                if in_degree[i]==0:
                    queue.append(i)
            cnt+=1
        if cnt==self.vertices:
            return False
        else:
            return True
if __name__=='__main__':
    g=Graph(4)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,0)
    g.add_edge(0,2)
    g.add_edge(2,3)
    if g.iscycle():
        print("Yes")
    else:
        print("No")