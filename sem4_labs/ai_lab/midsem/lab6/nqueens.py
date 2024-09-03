import random
def init_b():
    return [random.randint(0,7) for _ in range(8)]
def calc(b):
    cost = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if b[i] == b[j] or abs(b[i] - b[j]) == abs(i - j):
                cost += 1
    return cost
def pr_b(b):
    for i in range(8):
        for j in range(8):
            if b[i]==j:
                print('Q',end=' ')
            else:
                print('.',end=' ')                
        print()
def hc_q():
    cur_b=init_b()
    cur_c=calc(cur_b)
    while cur_c>0:
        nb=[]
        for i in range(8):
            for j in range(8):
                if cur_b[i]!=j:
                    nb_b=cur_b.copy()
                    nb_b[i]=j
                    nb.append([nb_b,calc(nb_b)])
        new_b,new_c=min(nb,key=lambda x:x[1])
        if new_c<cur_c:
            cur_c=new_c
            cur_b=new_b
        else:
            break
    return cur_b,cur_c
sol_b, sol_c = hc_q()   
print("Final Solution:")
pr_b(sol_b)
print(f"Total number of conflicts: {sol_c}")