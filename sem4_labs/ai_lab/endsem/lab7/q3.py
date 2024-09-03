import random
def ini():
    p=[[1,2,3],[4,5,6],[7,8,0]]
    for _ in range(8):
        p=randmov(p)
    return p
def print_b(b):
    for row in b:
        print(row)
    print()
def randmov(p):
    er,ec=emp(p)
    pm=[]
    if er>0:
        pm.append((er-1,ec))
    if er<2:
        pm.append((er+1,ec))
    if ec>0:
        pm.append((er,ec-1))
    if ec<2:
        pm.append((er,ec+1))
    nr,nc=random.choice(pm)
    p[er][ec],p[nr][nc]=p[nr][nc],p[er][ec]
    return p
def emp(b):
    for i in range(3):
        for j in range(3):
            if b[i][j]==0:
                return i,j
def calc_b(p,goal):
    cost=0
    for i in range(3):
        for j in range(3):
            if p[i][j]!=goal[i][j]:
                cost+=1
    return cost
def hc():
    cp=ini()
    goal_p=[[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    cc=calc_b(cp,goal_p)
    while True:
        a=cp.copy()
        np=randmov(a)
        nc=calc_b(a,goal_p)
        if nc>=cc:
            break
        else:
            cc=nc
            cp=np
    return cp,cc
sp, sc = hc()
print("Initial p:")
print_b(ini())
print("Final Solution:")
print_b(sp)
print(f"Total number of misplaced tiles: {sc    }")