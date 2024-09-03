class BestFirstSearch:
    def __init__(self, graph, heuristics):
        self.graph = graph
        self.heuristics = heuristics
    def search(self, start, goals):
        open_list = [(0, start, [start], 0)]
        min_cost = 1e9
        min_path = []
        while open_list:
            min_f=1e9
            min_index=-1
            for i,(f,node,path,leng)in enumerate(open_list):
                if f<min_f:
                    min_f=f
                    min_index=i
            f,node,path,leng=open_list.pop(min_index)
            if node in goals:
                return path,leng
            for dest,cost in self.graph[node]:
                if dest not in path:
                    open_list.append((self.heuristics[dest],dest,path+[dest],leng+cost))
        return None
heuristics = {
            'A': 1,
            'B': 4,
            'C': 2,
            'G': 0,
            'S': 5
        }

graph = {
    'A': [('S', 5), ('G', 1)],
    'B': [('S', 1), ('C', 2)],
    'C': [('B', 2), ('G', 2)],
    'G': [('A', 1), ('C', 2)],
    'S': [('A', 5), ('B', 1)]    
}

print(BestFirstSearch(graph, heuristics).search('S', ['G']))