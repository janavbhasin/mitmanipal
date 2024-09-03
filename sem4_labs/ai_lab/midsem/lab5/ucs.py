class UniformCostSearch:
    def __init__(self, graph):
        self.graph = graph
    def search(self,start,goal):
        queue=[(0,(start,[start]))]
        min_cost=1e9
        min_path=[]
        while queue:
            queue.sort()
            cost,(node,path)=queue.pop()
            if cost>min_cost:
                continue
            if node==goal:
                min_cost=cost
                min_path=path
            for next,money in self.graph[node]:
                if next not in path:
                    queue.append((money+cost,(next,path+[next])))
        return min_cost,min_path
    def multiple_goals(self, start, goals):
        return sorted([self.search(start, goal) for goal in goals])[0]
graph = {
        	'S': [('A', 5), ('B', 9), ('D', 6)],
        	'A': [('B', 3), ('G1', 9)],
        	'B': [('A', 2), ('C', 1)],
        	'C': [('S', 6), ('F', 7), ('G2', 5)],
        	'D': [('C', 2), ('E', 2)],
        	'E': [('G3', 7)],
        	'F': [('D', 2), ('G3', 8)],
        	'G1': [],
        	'G2': [],
        	'G3': [],
            }
uc_search = UniformCostSearch(graph)
print(uc_search.multiple_goals('S', ['G2','G1','G3']))  # Output: (3, ['A', 'B', 'C', 'D'])
