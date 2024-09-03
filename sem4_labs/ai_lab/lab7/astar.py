class AStar:
    def __init__(self, graph, heuristics):
        self.graph = graph
        self.heuristics = heuristics
    def search(self, start, goals):
        open_list = [(0, start, [start], 0)] 
        closed_set = set()
        while open_list:
            open_list.sort()
            _, node, path, length = open_list.pop(0)
            if node in goals:
                return path, length
            elif node not in closed_set:
                closed_set.add(node)
                for neighbor, dist in self.graph[node]:
                    if neighbor not in closed_set:
                        new_length = length + dist
                        new_path = path + [neighbor]
                        h = new_length + self.heuristics[neighbor]
                        open_list.append((h, neighbor, new_path, new_length))
        return None, None