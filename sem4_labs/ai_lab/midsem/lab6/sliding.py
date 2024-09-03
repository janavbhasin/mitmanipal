import random
def ini():
    a=[[1,2,3],[4,5,6],[7,8,0]]
    for _ in range(50):
        a=randmov(a)
    return a
def print_p(a):
    for row in a:
        print(row)
def randmov(p):
    pm=[]
    poss_x,poss_y=possibility(p)
    if poss_x>0:
        pm.append((poss_x-1,poss_y))
    if poss_x<2:
        pm.append((poss_x+1,poss_y))
    if poss_y>0:
        pm.append((poss_x,poss_y-1))
    if poss_y<2:
        pm.append((poss_x,poss_y+1))
    if len(pm) == 0:
        return p
    x,y=random.choice(pm)
    p[x][y],p[poss_x][poss_y]=p[poss_x][poss_y],p[x][y]
    return p
def possibility(a):
    for i in range(3):
        for j in range(3):
            if a[i][j]==0:
                return i,j
    return 0,0
def calc(a,goal):
    count=0
    for i in range(3):
        for j in range(3):
            if a[i][j]!=goal[i][j]and a[i][j]!=0:
                count+=1
            elif a[i][j] == 0 and goal[i][j] != 0:  # Count empty space in wrong position
                count += 1
    return count
def hc():
    ac=ini()
    goal=[[1,2,3],[4,5,6],[7,8,0]]
    an=calc(ac,goal)
    while True:
        a=ac.copy()
        nc=randmov(a)
        nn=calc(nc,goal)
        if nn<=an:
            an=nn
            ac=nc
        else:
            break
    print_p(goal)
    return ac,an
print("goal")
sp, sc = hc()
print("Initial p:")
print_p(ini())
print("Final Solution:")
print_p(sp)
print(f"Total number of misplaced tiles: {sc}")