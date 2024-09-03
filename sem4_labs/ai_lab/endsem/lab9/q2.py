def DFS(cur_jug1,cur_jug2,target,path,visited,is_solveable):
    global jug1_cap,jug2_cap
    if cur_jug1 > jug1_cap or cur_jug2 > jug2_cap or cur_jug1<0 and cur_jug2<0:
        return 
    if(cur_jug1,cur_jug2)in visited:
        return
    path.append((cur_jug1,cur_jug2))
    visited.append((cur_jug1,cur_jug2))
    if cur_jug1==target or cur_jug2==target:
        is_solveable=True
        if cur_jug1==target and cur_jug2!=0:
            path.append((cur_jug1,0))
        if cur_jug2==target and cur_jug1!=0:
            path.append((0,cur_jug2))
            