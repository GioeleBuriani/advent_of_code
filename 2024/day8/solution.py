import numpy as np
from itertools import combinations


def parse_input_file(file_path):
    """
    Parse the input file and return a numpy array representing the map.

    Parameters:
    file_path (str): The path to the input file.

    Returns:
    map (np.ndarray): A numpy array representing the map.
    """

    with open(file_path, 'r') as file:

        lines = [list(line.strip()) for line in file.readlines()]
        map = np.vstack(lines)

    return map


def find_antinodes(map, mode):
    """
    Find the antinodes of the antennas in the map.

    Parameters:
    map (np.ndarray): A numpy array representing the map.
    mode (int): The mode to use when finding the antinodes. mode=1 uses the first mode, mode=2 uses the second mode.

    Returns:
    antinode_map (np.ndarray): A numpy array representing the map with the antinodes.
    """

    antinode_map = map.copy()

    frequencies = np.unique(map)
    frequencies = frequencies[frequencies != '.']

    for frequency in frequencies:

        antennas = np.stack(np.where(map == frequency), axis=1)

        for antenna1, antenna2 in combinations(antennas, 2):

            antinodes = calculate_antinodes(map, antenna1, antenna2, mode)

            for antinode in antinodes:
                if 0 <= antinode[0] < map.shape[0] and 0 <= antinode[1] < map.shape[1]:
                    antinode_map[antinode[0], antinode[1]] = '#'

    return antinode_map


def calculate_antinodes(map, antenna1, antenna2, mode):
    """
    Calculate the antinodes of the antennas.

    Parameters:
    map (np.ndarray): A numpy array representing the map.
    antenna1 (np.ndarray): The first antenna.
    antenna2 (np.ndarray): The second antenna.
    mode (int): The mode to use when finding the antinodes. mode=1 uses the first mode, mode=2 uses the second mode.

    Returns:
    antinodes (np.ndarray): A numpy array representing the antinodes.
    """

    distance = antenna1 - antenna2

    if mode == 1:
        antinode1 = antenna1 + distance
        antinode2 = antenna2 - distance
        return np.stack([antinode1, antinode2])

    if mode == 2:
        antinodes = []

        antinode = antenna1
        while True:
            antinode = antinode - distance
            if np.any(antinode < 0) or np.any(antinode >= map.shape):
                break
            antinodes.append(antinode)

        antinode = antenna2
        while True:
            antinode = antinode + distance
            if np.any(antinode < 0) or np.any(antinode >= map.shape):
                break
            antinodes.append(antinode)
        return np.stack(antinodes)


def main():

    file_path = '2024/day8/input.txt'

    map = parse_input_file(file_path)

    antinode_map = find_antinodes(map, mode=1)
    n_antinodes = np.sum(antinode_map == '#')
    print("Number of antinodes:", n_antinodes)

    antinode_map = find_antinodes(map, mode=2)
    n_antinodes = np.sum(antinode_map == '#')
    print("Number of antinodes:", n_antinodes)


if __name__ == '__main__':
    main()
