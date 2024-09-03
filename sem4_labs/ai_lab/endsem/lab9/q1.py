def waterjugproblem(jug1_cap,jug2_cap,target):
    jug1=0
    jug2=0
    visited=[]
    actions=[('fill',1),('fill',2),('empty',1),('empty',2),('pour',1,2),('pour',2,1)]
    queue=[(jug1,jug2,[])]
    while queue:
        cur_jug1,cur_jug2,seq=queue.pop(0)
        if cur_jug1==target:
            return seq
        for action in actions:
            if action[0]=='fill':
                if action[1]==1:
                    next=(jug1_cap,cur_jug2)
                else:
                    next=(cur_jug1,jug2_cap)
            elif action[0]=='empty':
                if action[1]==1:
                    next=(0,cur_jug2)
                else:
                    next=(cur_jug1,0)
            else:
                if action[1]==1:
                    amount=min(cur_jug1,jug2_cap-cur_jug2)
                    next=(cur_jug1-amount,amount+cur_jug2)
                else:
                    amount=min(cur_jug2,jug1_cap-cur_jug1)
                    next=(cur_jug1+amount,cur_jug2-amount)
            if next not in visited:
                visited.append(next)
                nex_seq=seq+[action]
                queue.append((next[0],next[1],nex_seq))
result = waterjugproblem(4, 3, 2)
print(result)