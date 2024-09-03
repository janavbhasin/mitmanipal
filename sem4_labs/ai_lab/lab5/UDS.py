class UniformCostSearch:
    def __init__(self, graph):
        self.graph = graph
    def search(self, start, goal):
        queue = [(0, start, [start])]
        min_cost = 1e9
        min_path = []
        while queue:
            queue.sort()
            cost, node, path = queue.pop()  
            if cost > min_cost:
                continue
            if node == goal:
                min_cost = cost
                min_path = path
            for next_node, money in self.graph[node]:
                if next_node not in path:
                    queue.append((money + cost, next_node, path + [next_node]))  
        return min_cost, min_path
    def multiple_goals(self, start, goals):
        return sorted([self.search(start, goal) for goal in goals])[0]