def water_jug_problem(jug1_capacity, jug2_capacity, target_amount):
    jug1 = 0
    jug2 = 0
    possible_actions = [("fill", 1), ("fill", 2), ("empty", 1), ("empty", 2), ("pour", 1, 2), ("pour", 2, 1)]
    visited_states = set()
    exploration_queue = [(jug1, jug2, [])]
    while exploration_queue:
        current_jug1, current_jug2, current_sequence = exploration_queue.pop(0)
        if (current_jug1, current_jug2) not in visited_states:
            visited_states.add((current_jug1, current_jug2))
            if current_jug1 == target_amount:
                return current_sequence
            for action in possible_actions:
                if action[0] == "fill":
                    if action[1] == 1:
                        next_state = (jug1_capacity, current_jug2)
                    else:
                        next_state = (current_jug1, jug2_capacity)
                elif action[0] == "empty":
                    if action[1] == 1:
                        next_state = (0, current_jug2)
                    else:
                        next_state = (current_jug1, 0)
                else:
                    if action[1] == 1:
                        amount_to_pour = min(current_jug1, jug2_capacity - current_jug2)
                        next_state = (current_jug1 - amount_to_pour, current_jug2 + amount_to_pour)
                    else :
                        amount_to_pour = min(current_jug2, jug1_capacity - current_jug1)
                        next_state = (current_jug1 + amount_to_pour, current_jug2 - amount_to_pour)
                if next_state not in visited_states:
                    next_sequence = current_sequence + [next_state]
                    exploration_queue.append((next_state[0], next_state[1], next_sequence))
    return None
result = water_jug_problem(4, 3, 2)
print(result)