class graph():
	def __init__(self,vertices):
		self.graph={}
		self.v=vertices
		for i in range(vertices):
			self.graph[i]=[]
	def add_edge(self,u,v):
		self.graph[u].append(v)
	def iscyclic(self,v,visited,recstack):
		visited[v]=True
		recstack[v]=True
		for neighbour in self.graph[v]:
			if visited[neighbour]==False:
				if self.iscyclic(neighbour,visited,recstack)==True:
					return True
			elif recstack[neighbour]==True:
				return True
		recstack[v]=False
		return False
	def cyclic(self):
		visited=[False]*(self.v+1)
		recstack=[False]*(self.v+1)
		for node in range(self.v):
			if visited[node]==False:
				if self.iscyclic(node,visited,recstack):
					return True
		return False
g=graph(4)
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