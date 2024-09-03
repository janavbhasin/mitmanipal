class graph:
	def __init__(self,vertices):
		self.graph={}
		self.V=vertices
		for i in range(vertices):
			self.graph[i]=[]
	def add_edge(self,u,v):
		self.graph[u].append(v)
	def topological_sort(self):
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
			node=queue.pop(0)
			for neighbour in self.graph[node]:
				in_degree[neighbour]-=1
				if in_degree[neighbour]==0:
					queue.append(neighbour)
			result.append(node)
		print(result)
if __name__ == '__main__':
    g = graph(6)
    g.add_edge(5, 2)
    g.add_edge(3, 1)
    g.add_edge(2, 3)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    
    print("Topological Sort is:")
    g.topological_sort()