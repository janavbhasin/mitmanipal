import random
def ini():
    p = [[1, 2, 3],[4, 5, 6],[7, 8, 0]]    
    for _ in range(100):
        p = randmov(p)
    return p
def print_p(p):
    for row in p:
        print(row)
    print()
def randmov(p):
    er, ec = emp(p)
    pm = []
    if er > 0:
        pm.append((er - 1, ec))  
    if er < 2:
        pm.append((er + 1, ec))  
    if ec > 0:
        pm.append((er, ec - 1))  
    if ec < 2:
        pm.append((er, ec + 1))  
    nr, nc = random.choice(pm)
    p[er][ec], p[nr][nc] = p[nr][nc], p[er][ec]
    return p
def emp(p):
    for i in range(3):
        for j in range(3):
            if p[i][j] == 0:
                return i, j
def calc(p, goal):
    cost = 0
    for i in range(3):
        for j in range(3):
            if p[i][j] != goal[i][j]:
                cost += 1
    return cost
def hc():
    cp = ini()
    goal_p = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    cc = calc(cp, goal_p)
    while True:
        a=cp.copy()
        np = randmov(a)
        nc = calc(np, goal_p)
        if nc >= cc:
            break
        cp = np
        cc = nc
    return cp, cc
sp, sc = hc()
print("Initial p:")
print_p(ini())
print("Final Solution:")
print_p(sp)
print(f"Total number of misplaced tiles: {sc}")