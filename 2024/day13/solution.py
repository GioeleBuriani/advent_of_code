import numpy as np


def parse_input_file(file_path):
    """
    Parse the input file and return a set of tuples representing the machines data.

    Parameters:
    file_path (str): The combo to the input file.

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
            new_prize_coordinates = (
                prize_coordinates[0] + 10000000000000,
                prize_coordinates[1] + 10000000000000)

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
    """
    Calculate the total tokens needed to solve the machines.

    Parameters:
    machines_data (set): A set of tuples representing the machines data.
    version (str): The version of the machine to solve.

    Returns:
    total_tokens (int): The total tokens needed to solve the machines.
    """

    total_tokens = 0

    for machine in machines_data:

        A_coord, B_coord, prize_coord, new_prize_coord = machine

        if version == "old":
            combo = solve_system(A_coord, B_coord, prize_coord)
        else:
            prize_coord = new_prize_coord
            combo = solve_system(A_coord, B_coord, prize_coord)

        price = calculate_price(combo)
        total_tokens += price

    return total_tokens


def solve_system(A_coord, B_coord, prize_coord):
    """
    Solve the system of equations Ax + By = Px and Cx + Dy = Py.

    Parameters:
    A_coord (tuple): A tuple representing the coordinates of button A.
    B_coord (tuple): A tuple representing the coordinates of button B.
    prize_coord (tuple): A tuple representing the coordinates of the prize.

    Returns:
    x, y (tuple): A tuple representing the solution to the system of equations.
    """

    Ax, Ay = A_coord
    Bx, By = B_coord
    Px, Py = prize_coord

    y = (Ax * Py - Ay * Px) / (Ax * By - Ay * Bx)
    x = (Px - Bx * y) / Ax

    if x % 1 != 0 or y % 1 != 0:
        x = 0
        y = 0

    return x, y


def calculate_price(combo):
    """
    Calculate the price of the combo.

    Parameters:
    combo (tuple): A tuple representing the combo.

    Returns:
    price (int): The price of the combo.
    """

    return int(combo[0] * 3 + combo[1])


def main():

    file_path = '2024/day13/input.txt'

    machines_data = parse_input_file(file_path)

    total_tokens = calculate_tokens(machines_data, "old")
    print("Total tokens:", total_tokens)

    new_total_tokens = calculate_tokens(machines_data, "new")
    print("New total tokens:", new_total_tokens)


if __name__ == '__main__':
    main()
