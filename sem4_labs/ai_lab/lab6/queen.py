import random
def init_b():
    return [random.randint(0, 7) for _ in range(8)]
def calc(b):
    cost = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if b[i] == b[j] or abs(b[i] - b[j]) == abs(i - j):
                cost += 1
    return cost
def pr_b(b):
    for row in range(8):
        for col in range(8):
            if b[row] == col :
                print("Q ",end="")
            else :
                print(". ",end="")
        print()
    print()
def hc_q():
    cur_b = init_b()
    cur_c = calc(cur_b) 
    while True:
        nb = []
        for i in range(8):
            for j in range(8):
                if cur_b[i] != j:
                    nb_b = cur_b.copy()
                    nb_b[i] = j
                    nb.append((nb_b, calc(nb_b)))
        best_n, best_c = min(nb, key=lambda x: x[1])
        if best_c < cur_c:
            cur_b = best_n
            cur_c = best_c
        else:
            break
    return cur_b, cur_c
sol_b, sol_c = hc_q()
print("Final Solution:")    
pr_b(sol_b)
print(f"Total number of conflicts: {sol_c}")