import numpy as np
import matplotlib.pyplot as plt


def parse_input_file(file_path):
    """
    Function to parse the input file and return the data in a structured format

    Parameters:
    file_path (str): Path to the input file

    Returns:
    robots_data (list): List of dictionaries containing the position and velocity of each robot
    """

    with open(file_path, 'r') as file:

        lines = [line.strip() for line in file if line.strip()]

        robots_data = []

        for line in lines:

            parts = line.split(" ")
            # Extract position (x, y)
            pos = tuple(map(int, parts[0][2:].split(",")))
            # Extract velocity (dx, dy)
            vel = tuple(map(int, parts[1][2:].split(",")))

            robots_data.append({'p': pos, 'v': vel})

    return robots_data


def change_locations(robots_data, map_size, steps):
    """
    Function to calculate the new locations of the robots after a given number of steps

    Parameters:
    robots_data (list): List of dictionaries containing the position and velocity of each robot
    map_size (tuple): Size of the map (width, height)
    steps (int): Number of steps to simulate

    Returns:
    locations (list): List of tuples containing the new location of each robot
    """

    locations = []

    for robot in robots_data:

        location = tuple(
            (np.array(
                robot["p"]) +
                np.array(
                robot["v"]) *
                steps) %
            map_size)
        locations.append(location)

    return locations


def get_safety_factor(locations, map_size):
    """
    Function to calculate the safety factor of the robots,
    calculated as the product of the number of robots in each quadrant of the map

    Parameters:
    locations (list): List of tuples containing the new location of each robot
    map_size (tuple): Size of the map (width, height)

    Returns:
    safety_factor (int): Safety factor of the robots
    """

    quads = np.array([0, 0, 0, 0])

    for location in locations:

        if location[0] < map_size[0] // 2 and location[1] < map_size[1] // 2:
            quads[0] += 1
        elif location[0] >= map_size[0] // 2 + 1 and location[1] < map_size[1] // 2:
            quads[1] += 1
        elif location[0] < map_size[0] // 2 and location[1] >= map_size[1] // 2 + 1:
            quads[2] += 1
        elif location[0] >= map_size[0] // 2 + 1 and location[1] >= map_size[1] // 2 + 1:
            quads[3] += 1

    safety_factor = np.prod(quads)

    return safety_factor


def simulate_robots(robots_data, map_size, max_steps, pause_time=0.1):
    """
    Function to simulate the robots moving in the map

    Parameters:
    robots_data (list): List of dictionaries containing the position and velocity of each robot
    map_size (tuple): Size of the map (width, height)
    max_steps (int): Number of steps to simulate
    pause_time (float): Time to pause between steps
    """

    plt.figure(figsize=(8, 8))

    for step in range(max_steps):

        locations = change_locations(robots_data, map_size, step)

        map = np.zeros(map_size, dtype=int).T
        for location in locations:
            map[location[1], location[0]] += 1

        plt.clf()
        plt.imshow(map, cmap="gray", interpolation="nearest")
        plt.title(f"Step {step}")
        plt.pause(pause_time)

        input("Press ENTER to continue")

    plt.show()


def main():

    file_path = '2024/day14/input.txt'

    robots_data = parse_input_file(file_path)

    map_size = (101, 103)
    steps = 7383
    locations = change_locations(robots_data, map_size, steps)

    safety_factor = get_safety_factor(locations, map_size)
    print("Safety factor: ", safety_factor)

    simulate_robots(robots_data, map_size, max_steps=10000, pause_time=0.1)


if __name__ == '__main__':
    main()
