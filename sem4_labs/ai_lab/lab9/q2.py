def DFS(current_jug1, current_jug2, target, path, visited, is_solvable):
    global jug1_capacity, jug2_capacity
    if current_jug1 > jug1_capacity or current_jug2 > jug2_capacity or current_jug1 < 0 or current_jug2 < 0:
        return
    if (current_jug1, current_jug2) in visited:
        return
    path.append([current_jug1, current_jug2])
    visited.append((current_jug1, current_jug2))
    if current_jug1 == target or current_jug2 == target:
        is_solvable = True
        if current_jug1 == target:
            if current_jug2 != 0:
                path.append([current_jug1, 0])
        if current_jug2 == target:
            if current_jug1 != 0:
                path.append([0, current_jug2])
    DFS(current_jug1, jug2_capacity, target, path, visited, is_solvable)
    DFS(jug1_capacity, current_jug2, target, path, visited, is_solvable)
    for i in range(max(jug1_capacity, jug2_capacity) + 1):
        next_jug1 = current_jug1 + i
        next_jug2 = current_jug2 - i
        if next_jug1 == jug1_capacity or (next_jug2 == 0 and next_jug2 >= 0):
            DFS(next_jug1, next_jug2, target, path, visited, is_solvable)
        next_jug1 = current_jug1 - i
        next_jug2 = current_jug2 + i
        if (next_jug1 == 0 and next_jug1 >= 0) or next_jug2 == jug2_capacity:
            DFS(next_jug1, next_jug2, target, path, visited, is_solvable)
    DFS(jug1_capacity, 0, target, path, visited, is_solvable)
    DFS(0, jug2_capacity, target, path, visited, is_solvable)
    if not is_solvable:
        return  

if __name__ == "__main__":
    jug1_capacity, jug2_capacity, target = 4, 3, 2
    path = []
    visited = []
    is_solvable = False
    DFS(0, 0, target, path, visited, is_solvable)
    for i in path:
        print(f"( {i[0]}, {i[1]} )")
