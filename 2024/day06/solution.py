import numpy as np


def parse_input_file(file_path):
    """
    Parse the input file and return a numpy array with the map.

    Parameters:
    file_path (str): The path to the input file.

    Returns:
    map (numpy array): The map as a numpy array.
    """

    with open(file_path, 'r') as file:

        lines = [list(line.strip()) for line in file.readlines()]
        map = np.vstack(lines)

    return map


def calculate_path(map):
    """
    Calculate the path of the robot and the number of obstacles.

    Parameters:
    map (numpy array): The map as a numpy array.

    Returns:
    steps (int): The number of steps the robot took.
    n_obstacles (int): The number of obstacles the robot encountered.
    """

    states = []
    obstacles = []

    position = np.array(np.where(map == '^')).flatten()
    direction = 1
    state = np.hstack([position, direction])

    while True:

        state_copy = state.copy()
        map_copy = map.copy()

        states.append(state.copy())

        if check_end(map, state):
            break

        obstacle = np.array(move(map, state_copy)[0:2])
        map_copy[obstacle[0], obstacle[1]] = '#'
        loop_states = []
        if find_loop(map_copy, state, loop_states):
            if not np.any([np.array_equal(obstacle, st[0:2])
                          for st in states]):
                obstacles.append(obstacle.copy())

        state = move(map, state)

    steps = len(np.unique(np.vstack(states)[:, 0:2], axis=0))
    n_obstacles = len(np.unique(np.vstack(obstacles), axis=0))

    return steps, n_obstacles


def check_end(map, state):
    """
    Check if the robot has reached the end of the map.

    Parameters:
    map (numpy array): The map as a numpy array.
    state (numpy array): The current state of the robot.

    Returns:
    bool: True if the robot has reached the end of the map, False otherwise.
    """

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


def move(map, state):
    """
    Move the robot to the next position.

    Parameters:
    state (numpy array): The current state of the robot.

    Returns:
    state (numpy array): The new state of the robot.
    """

    if check_obstacle(map, state):
        if state[2] == 4:
            state[2] = 1
        else:
            state[2] += 1
        if check_obstacle(map, state):
            if state[2] == 4:
                state[2] = 1
            else:
                state[2] += 1

    if state[2] == 1:
        state[0] -= 1
    elif state[2] == 2:
        state[1] += 1
    elif state[2] == 3:
        state[0] += 1
    elif state[2] == 4:
        state[1] -= 1

    return state


def check_obstacle(map, state):
    """
    Check if the robot has encountered an obstacle.

    Parameters:
    map (numpy array): The map as a numpy array.
    state (numpy array): The current state of the robot.

    Returns:
    bool: True if the robot has encountered an obstacle, False otherwise
    """

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


def find_loop(map, state, loop_states):
    """
    Find a loop in the path of the robot.

    Parameters:
    map (numpy array): The map as a numpy array.
    state (numpy array): The current state of the robot.
    loop_states (list): A list of states the robot has been in.

    Returns:
    bool: True if a loop is found, False otherwise.
    """

    if not np.any([np.array_equal(state, st) for st in loop_states]):
        loop_states.append(state.copy())
    else:
        return True

    if state[2] == 1:

        if '#' in map[state[0], state[1]:]:

            new_state = state.copy()
            new_state[1] = state[1] + \
                np.where(map[state[0], state[1]:] == '#')[0][0] - 1
            new_state[2] += 1

            if find_loop(map, new_state, loop_states):
                return True

    elif state[2] == 2:

        if '#' in map[state[0]:, state[1]]:

            new_state = state.copy()
            new_state[0] = state[0] + \
                np.where(map[state[0]:, state[1]] == '#')[0][0] - 1
            new_state[2] += 1

            if find_loop(map, new_state, loop_states):
                return True

    elif state[2] == 3:

        if '#' in map[state[0], :state[1]]:

            new_state = state.copy()
            new_state[1] = np.where(map[state[0], :state[1]] == '#')[0][-1] + 1
            new_state[2] += 1

            if find_loop(map, new_state, loop_states):
                return True

    elif state[2] == 4:
        
        if '#' in map[:state[0], state[1]]:

            new_state = state.copy()
            new_state[0] = np.where(map[:state[0], state[1]] == '#')[0][-1] + 1
            new_state[2] = 1

            if find_loop(map, new_state, loop_states):
                return True

    return False


def main():

    file_path = '2024/day6/input.txt'

    map = parse_input_file(file_path)

    steps, n_obstacles = calculate_path(map)

    print("The number of steps is", steps)
    print("The number of obstacles is", n_obstacles)


if __name__ == '__main__':
    main()
