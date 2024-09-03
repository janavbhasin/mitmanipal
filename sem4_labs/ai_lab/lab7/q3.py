class Board:
    def __init__(self, positions):
        self.pos = positions
        self.g = float('inf')
        self.parent = None
        self.goal = None
    def h(self, goal):
        return sum(1 for i, j in zip(self.pos, goal) if i != j)
    def f(self, goal):
        return self.g + self.h(goal)
    def copy(self):
        return Board(self.pos.copy())
    def to_print(self):
        return [self.pos[i:i+3] for i in range(0, len(self.pos), 3)]
    def __eq__(self, other):
        return self.pos == other.pos
    def __lt__(self, other):
        return self.f(self.goal) < other.f(other.goal)
class AStar:
    def __init__(self):
        self.open = []
        self.closed = set()
    def get_neighbours(self, board):
        empty_idx = board.pos.index(0)
        possible_swaps = [empty_idx+i for i in range(-3,5,2) if 0 <= empty_idx+i <= 8]
        neighbours = []
        for idx in possible_swaps:
            n = board.copy()
            n.pos[idx], n.pos[empty_idx] = n.pos[empty_idx], n.pos[idx]
            neighbours.append(n)
        return neighbours
    def best_path(self, goal):
        n = goal
        path = []
        while n is not None:
            path.append(n.to_print())
            n = n.parent
        return path[::-1]
    def search(self, start, goal):
        start_state = Board(start)
        start_state.g = 0
        start_state.goal = goal
        self.open.append(start_state)
        while self.open:
            node = min(self.open, key=lambda x: x.f(goal))
            self.open.remove(node)
            if node.pos == goal:
                return self.best_path(node)
            if tuple(node.pos) in self.closed:
                continue
            self.closed.add(tuple(node.pos))
            for n in self.get_neighbours(node):
                if tuple(n.pos) not in self.closed:
                    tentative_g = node.g + 1
                    if tentative_g < n.g:
                        n.g = tentative_g
                        n.parent = node
                        self.open.append(n)
        return False
start = [2, 8, 3, 1, 6, 4, 7, 0, 5]
goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
best_path = AStar().search(start, goal)
if best_path:
    for arr in best_path:
        print(arr, '\n')