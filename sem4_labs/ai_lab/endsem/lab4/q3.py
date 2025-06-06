def tsp_bfs(graph,start):
    queue=[(start,[start],0)]
    min_cost=1e9
    min_path=[]
    while queue:
        currentnode,path,cost=queue.pop(0)
        if len(path)==len(graph) and graph[currentnode][start]!=0:
            cost+=graph[currentnode][start]
            if min_cost>cost:
                min_cost=cost
                min_path=path+[start]
        else:
            for i in graph[currentnode]:
                if graph[currentnode][i]!=0 and i not in path:
                    queue.append((i,path+[i],cost+graph[currentnode][i]))
    return min_path,min_cost
def main():
    graph = {
            'A': {'B': 2, 'C': 3, 'D': 1},
            'B': {'A': 2, 'C': 4, 'D': 2},
            'C': {'A': 3, 'B': 4, 'D': 3},
            'D': {'A': 1, 'B': 2, 'C': 3}
        }
    start_node = 'A'
    min_path, min_cost = tsp_bfs(graph, start_node)
    print("Minimum path:", min_path)
    print("Minimum cost:", min_cost)    
if __name__ == "__main__":
    main()