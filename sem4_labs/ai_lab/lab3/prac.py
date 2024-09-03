Maze = {
    1: [2, 6],
    2: [1, 3],
    3: [2, 8],
    4: [5],
    5: [4, 10],
    6: [1, 11],
    7: [8],
    8: [3, 7],
    9: [10, 14],
    10: [5, 9, 15],
    11: [6, 12],
    12: [11, 17],
    13: [14],
    14: [ 9,13, 19],
    15: [10, 20],
    16: [17],
    17: [12, 18,16],
    18: [17, 19],
    19: [14, 18],
    20: [15],
    0: [2, 5]
}

stack = []

def DFSFnc(vertex, visited):
    visited.add(vertex)
    print(vertex, end=' ')
    if vertex == 5:
        return True
    for n in Maze[vertex]:
        if n not in visited:
            stack.append(n)
            if DFSFnc(n, visited):
                return True
            stack.pop()
    return False

def DFS(v):
    visited = set()
    stack.append(v)
    DFSFnc(v, visited)

def main():
    DFS(2)

if __name__ == "__main__":
    main()
