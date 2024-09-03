class Astar:
    def __init__(self,graph,heuristics):
        self.graph=graph
        self.heuristics=heuristics
    def search(self,start,goals):
        open_list=[(0,start,[start],0)]
        closed_set=set()
        while open_list:
            open_list.sort()
            _,node,path,length=open_list.pop(0)
            if node in goals:
                return path,length
            elif node not in closed_set:
                closed_set.add(node)
                for neighbour,leng in self.graph[node]:
                    if neighbour not in closed_set:
                        new_length=length+leng
                        new_path=path+[neighbour]
                        h=new_length+self.heuristics[neighbour]
                        open_list.append((h,neighbour,new_path,new_length))
        return None,None
heuristics = {
            'A': 10,
            'B': 8,
            'C': 5,
            'D': 7,
            'E': 3,
            'F': 6,
            'G': 5,
            'H': 3,
            'I': 1, 
            'J': 0
        }
graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('E', 8)],
    'E': [('J', 5), ('I', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('J', 3)]    
}
print(Astar(graph, heuristics).search('A', ['J']))