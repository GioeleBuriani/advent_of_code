import numpy as np


def parse_input_file(file_path):
    """
    Parse the input file and return a set of tuples representing the machines data.

    Parameters:
    file_path (str): The path to the input file.

    Returns:
    machines_data (set): A set of tuples representing the machines data.
    """

    with open(file_path, 'r') as file:

        lines = [line.strip() for line in file if line.strip()]

        machines_data = set()
        for i in range(0, len(lines), 3):

            button_a_line = lines[i]
            button_a_coordinates = extract_coordinates(button_a_line)

            button_b_line = lines[i + 1]
            button_b_coordinates = extract_coordinates(button_b_line)

            prize_line = lines[i + 2]
            prize_coordinates = extract_coordinates(prize_line)

            entry = (
                button_a_coordinates,
                button_b_coordinates,
                prize_coordinates)
            machines_data.add(entry)

    return machines_data


def extract_coordinates(line):
    """
    Extract the coordinates from a line of the input file.

    Parameters:
    line (str): A line of the input file.

    Returns:
    coordinates (tuple): A tuple representing the coordinates.
    """

    parts = line.split(": ")[1]  # Get part after "Button A: " or "Prize: "
    x_part, y_part = parts.split(", ")  # Split "X+94, Y+34"

    x_value = int(x_part[2:])  # Extract numeric part (skip "X+" or "X=")
    y_value = int(y_part[2:])  # Extract numeric part (skip "Y+")

    return (x_value, y_value)


def calculate_tokens(machines_data):

    total_tokens = 0

    for machine in machines_data:

        A_coord, B_coord, prize_coord = machine

        memory = (0, 0)
        memories = set()
        paths = set()
        paths_x = push_button(0, A_coord[0], B_coord[0], prize_coord[0], memory, memories, paths)

        filtered_paths = filter_paths(paths_x, A_coord[1], B_coord[1], prize_coord[1])

        best_price = find_best_price(filtered_paths)
        total_tokens += best_price

    return total_tokens


def push_button (sum, A, B, goal, memory, memories, paths):

    if memory[0] == 100 or memory[1] == 100:
        return False

    if memory in memories:
        return False
    memories.add(memory)

    sum_a = sum + A
    memory_a = (memory[0] + 1, memory[1])
    sum_b = sum + B
    memory_b = (memory[0], memory[1] + 1)

    if sum_a == goal:
        return memory_a
    elif sum_b == goal:
        return memory_b
    elif sum_a > goal and sum_b > goal:
        return False
    else:
        path_a = push_button(sum_a, A, B, goal, memory_a, memories, paths)
        if isinstance(path_a, tuple):
            paths.add(path_a)
        elif isinstance(path_a, set):
            paths.update(path_a)
        
        path_b = push_button(sum_b, A, B, goal, memory_b, memories, paths)
        if isinstance(path_b, tuple):
            paths.add(path_b)
        elif isinstance(path_b, set):
            paths.update(path_b)

    return paths


def filter_paths(paths, A_y, B_y, prize_y):

    filtered_paths = set()

    for path in paths:
        if path[0] * A_y + path[1] * B_y == prize_y:
            filtered_paths.add(path)

    return filtered_paths


def find_best_price(paths):

    if not paths:
        return 0

    prices = []
    
    for path in paths:
        price = path[0] * 3 + path[1]
        prices.append(price)

    return min(prices)


def main():

    file_path = '2024/day13/input.txt'

    machines_data = parse_input_file(file_path)

    total_tokens = calculate_tokens(machines_data)
    print("Total tokens:", total_tokens)


if __name__ == '__main__':
    main()
