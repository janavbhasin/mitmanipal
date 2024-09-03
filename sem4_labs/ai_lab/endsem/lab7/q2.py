import random
def init_b():
    return [random.randint(0,7)for _ in range(8)]
def calc_b(b):
    cost=0
    for i in range(8):
        for j in range(i+1,8):
            if b[i]==b[j] and abs(i-j)==abs(b[i]-b[j]):
                cost+=1
    return cost
def pr_b(b):
    for i in range(8):
        for j in range(8):
            if b[i]==j:
                print('Q ',end='')
            else:
                print('. ',end='')
        print()
def hc_q():
    cur_b=init_b()
    cur_c=calc_b(cur_b)
    while cur_c>0:
        nb=[]
        for i in range(8):
            for j in range(8):
                if cur_b[i]!=j:
                    nb_b=cur_b.copy()
                    nb_b[i]=j
                    nb.append((calc_b(nb_b),nb_b))
        best_n,best_c=min(nb,key=lambda x:x[0])
        if best_n<cur_c:
            cur_c=best_n
            cur_b=best_c
        else:
            break
    return cur_b,cur_c
sol_b, sol_c = hc_q()
print("Final Solution:")    
pr_b(sol_b)
print(f"Total number of conflicts: {sol_c}")