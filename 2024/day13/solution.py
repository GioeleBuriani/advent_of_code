import numpy as np


def parse_input_file(file_combo):
    """
    Parse the input file and return a set of tuples representing the machines data.

    Parameters:
    file_combo (str): The combo to the input file.

    Returns:
    machines_data (set): A set of tuples representing the machines data.
    """

    with open(file_combo, 'r') as file:

        lines = [line.strip() for line in file if line.strip()]

        machines_data = set()
        for i in range(0, len(lines), 3):

            button_a_line = lines[i]
            button_a_coordinates = extract_coordinates(button_a_line)

            button_b_line = lines[i + 1]
            button_b_coordinates = extract_coordinates(button_b_line)

            prize_line = lines[i + 2]
            prize_coordinates = extract_coordinates(prize_line)
            new_prize_coordinates = (prize_coordinates[0] + 10000000000000, prize_coordinates[1] + 10000000000000)

            entry = (
                button_a_coordinates,
                button_b_coordinates,
                prize_coordinates,
                new_prize_coordinates)
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


def calculate_tokens(machines_data, version):

    total_tokens = 0
    counter = 0

    for machine in machines_data:

        A_coord, B_coord, prize_coord, new_prize_coord = machine

        if version == "old":
            limit = 100
            prize_x = prize_coord[0]
        else:
            limit = 10000000000000
            prize_x = new_prize_coord[0]
            print(f"Checking machine {counter}/{len(machines_data)}")

        combo = find_combos(A_coord[0], B_coord[0], prize_x, limit)

        filtered_combos = filter_combos(combo, A_coord[1], B_coord[1], prize_coord[1])

        best_price = find_best_price(filtered_combos)
        total_tokens += best_price

        counter += 1

    return total_tokens


def find_combos(A_x, B_x, prize_x, limit):

    combos = set()

    big = max(A_x, B_x)
    small = min(A_x, B_x)

    small_pushes = min(prize_x // small, limit)
    big_pushes = 0

    while small_pushes >= 0 and big_pushes <= limit:

        if small_pushes % 10000000 == 0:
            print(f"Checking small_pushes {small_pushes} and big_pushes {big_pushes}")

        if small * small_pushes + big * big_pushes == prize_x:
            if A_x > B_x:
                combos.add((big_pushes, small_pushes))
            else:
                combos.add((small_pushes, big_pushes))
            small_pushes -= 1
        elif small * small_pushes + big * big_pushes < prize_x:
            big_pushes += 1
        else:
            small_pushes -= 1

    return combos


def filter_combos(combos, A_y, B_y, prize_y):

    filtered_combos = set()

    for combo in combos:
        if combo[0] * A_y + combo[1] * B_y == prize_y:
            filtered_combos.add(combo)

    return filtered_combos


def find_best_price(combos):

    if not combos:
        return 0

    prices = []

    for combo in combos:
        price = combo[0] * 3 + combo[1]
        prices.append(price)

    return min(prices)
        

######################### ALTERNATIVE SOLUTION (PART 1) #########################

def calculate_tokens_alt(machines_data):

    total_tokens = 0

    for machine in machines_data:

        A_coord, B_coord, prize_coord = machine

        memory = (0, 0)
        memories = set()
        combos = set()
        combos_x = push_button(0, A_coord[0], B_coord[0], prize_coord[0], memory, memories, combos)

        filtered_combos = filter_combos(combos_x, A_coord[1], B_coord[1], prize_coord[1])

        best_price = find_best_price(filtered_combos)
        total_tokens += best_price

    return total_tokens


def push_button (sum, A, B, goal, memory, memories, combos):

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
        combo_a = push_button(sum_a, A, B, goal, memory_a, memories, combos)
        if isinstance(combo_a, tuple):
            combos.add(combo_a)
        elif isinstance(combo_a, set):
            combos.update(combo_a)
        
        combo_b = push_button(sum_b, A, B, goal, memory_b, memories, combos)
        if isinstance(combo_b, tuple):
            combos.add(combo_b)
        elif isinstance(combo_b, set):
            combos.update(combo_b)

    return combos

#################################################################################


def main():

    file_combo = '2024/day13/input.txt'

    machines_data = parse_input_file(file_combo)

    total_tokens = calculate_tokens(machines_data, "old")
    print("Total tokens:", total_tokens)

    new_total_tokens = calculate_tokens(machines_data, "new")
    print("New total tokens:", new_total_tokens)

if __name__ == '__main__':
    main()
