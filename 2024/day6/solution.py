import numpy as np


def parse_input_file(file_path):

    with open(file_path, 'r') as file:

        lines = [list(line.strip()) for line in file.readlines()]
        map = np.vstack(lines)
        
    return map


def calculate_path(map):

    states = []
    obstacles = []
    
    position = np.array(np.where(map == '^')).flatten()
    direction = 1
    state = np.hstack([position, direction])

    while True:

        state_copy = state.copy()
        map_copy = map.copy()

        if not np.any([np.array_equal(state[0:2], st[0:2]) for st in states]):
            states.append(state.copy())

        if check_end(map, state):
            break

        loop_states = []
        obstacle = np.array(move(state_copy)[0:2])
        map_copy[obstacle[0], obstacle[1]] = '#'

        if find_loop(map_copy, state, loop_states):
            obstacles.append(obstacle)
            break
        
        if check_obstacle(map, state):
            if state[2] == 4:
                state[2] = 1
            else:
                state[2] += 1

        state = move(state)

    steps = len(states)
    n_obstacles = len(np.unique(obstacles))

    return steps, n_obstacles


def find_loop(map, state, loop_states):

    if not np.any([np.array_equal(state, st) for st in loop_states]):
        loop_states.append(state.copy())
    else:
        return True

    if state[2] == 1:

        if '#' in map[state[0], state[1]:]:

            new_state = state.copy()
            new_state[1] = state[1] + np.where(map[state[0], state[1]:] == '#')[0][0] - 1
            new_state[2] += 1

            find_loop(map, new_state, loop_states)

    elif state[2] == 2:
        if '#' in map[state[0]:, state[1]]:

            new_state = state.copy()
            new_state[0] = state[0] + np.where(map[state[0]:, state[1]] == '#')[0][0] - 1
            new_state[2] += 1

            find_loop(map, new_state, loop_states)

    elif state[2] == 3:
        if '#' in map[state[0], :state[1]]:

            new_state = state.copy()
            new_state[1] = np.where(map[state[0], :state[1]] == '#')[0][0] + 1
            new_state[2] += 1

            find_loop(map, new_state, loop_states)

    elif state[2] == 4:
        if '#' in map[:state[0], state[1]]:

            new_state = state.copy()
            new_state[0] = np.where(map[:state[0], state[1]] == '#')[0][0] + 1
            new_state[2] = 1

            find_loop(map, new_state, loop_states)

    return False


def check_end(map, state):
    
    limit = map.shape

    if state[2] == 1 and state[0] == 0:
        return True
    elif state[2] == 2 and state[1] == limit[1] - 1:
        return True
    elif state[2] == 3 and state[0] == limit[0] - 1:
        return True
    elif state[2] == 4 and state[1] == 0:
        return True
    
    return False


def check_obstacle(map, state):

    if state[2] == 1:
        if map[state[0] - 1, state[1]] == '#':
            return True
    elif state[2] == 2:
        if map[state[0], state[1] + 1] == '#':
            return True
    elif state[2] == 3:
        if map[state[0] + 1, state[1]] == '#':
            return True
    elif state[2] == 4:
        if map[state[0], state[1] - 1] == '#':
            return True

    return False


def move(state):

    if state[2] == 1:
        state[0] -= 1
    elif state[2] == 2:
        state[1] += 1
    elif state[2] == 3:
        state[0] += 1
    elif state[2] == 4:
        state[1] -= 1

    return state


def main():

    file_path = '2024/day6/test_input.txt'

    map = parse_input_file(file_path)

    steps, n_obstacles = calculate_path(map)

    print("The number of steps is", steps)
    print("The number of obstacles is", n_obstacles)


if __name__ == '__main__':
    main()
