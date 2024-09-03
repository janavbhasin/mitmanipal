class UniformCostSearch():
    def __init__(self,graph):
        self.graph=graph
    def solve(self,start,goal):
        queue=[(0,start,[start])]
        min_cost=1e9
        min_path=[]
        while queue:
            queue.sort()
            cost,node,path=queue.pop()
            if cost>min_cost:
                continue
            if node==goal:
                min_cost=cost
                min_path=path
            for dest,money in self.graph[node]:
                if dest not in path:
                    queue.append((cost+money,dest,path+[dest]))
        return min_cost,min_path
    def multiple_goals(self,start,goals):
        return sorted([self.solve(start,goal)for goal in goals])[0]
def main():
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
	print('Goal with the least cost: ', end='')
	print(UniformCostSearch(graph).multiple_goals('S',['G1','G2','G3']))
if __name__ == '__main__':
	main()