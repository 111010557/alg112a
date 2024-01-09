def is_valid(state):
    if state['wolf'] == state['sheep'] and state['farmer'] != state['wolf']:
        return False
    if state['sheep'] == state['cabbage'] and state['farmer'] != state['sheep']:
        return False
    return True

def dfs(current_state, visited, path):
    visited.append(current_state.copy())
    path.append(current_state.copy())

    if len(visited) == (2 ** 4):
        return path

    for next_state in generate_next_states(current_state):
        if next_state not in visited and is_valid(next_state):
            result = dfs(next_state, visited, path)
            if result is not None:
                return result

    path.pop()
    return None

def generate_next_states(current_state):
    next_states = []
    for animal in ['wolf', 'sheep', 'cabbage']:
        if current_state[animal] == current_state['farmer']:
            next_state = current_state.copy()
            next_state['farmer'] = 1 - current_state['farmer']
            next_state[animal] = 1 - current_state[animal]
            next_states.append(next_state)
    return next_states

def print_solution(solution):
    for i, state in enumerate(solution):
        print(f"Step {i + 1}: Farmer is on {['left', 'right'][state['farmer']]} side. Wolf is on {['left', 'right'][state['wolf']]} side. Sheep is on {['left', 'right'][state['sheep']]} side. Cabbage is on {['left', 'right'][state['cabbage']]} side.")
    print("Mission accomplished!")

# 初始狀態: {'farmer': 0, 'wolf': 0, 'sheep': 0, 'cabbage': 0}
initial_state = {'farmer': 0, 'wolf': 0, 'sheep': 0, 'cabbage': 0}

# 開始深度優先搜尋
visited_states = []
solution_path = dfs(initial_state, visited_states, [])

# 顯示解決方案
if solution_path is not None:
    print_solution(solution_path)
else:
    print("No solution found.")
