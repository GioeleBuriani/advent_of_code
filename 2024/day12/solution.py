import numpy as np


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


def get_total_price(map):
    """
    Get the total price of the plants in the map.

    Parameters:
    map (np.ndarray): A numpy array representing the map.

    Returns:
    price (int): The total price of the plants in the map.
    price_discounted (int): The total price of the plants in the map with a discount
    """

    plant_types = np.unique(map)
    price = 0
    price_discounted = 0

    for type in plant_types:

        regions = find_regions(map, type)

        for region in regions:

            area = len(region)

            perimeter = find_region_perimeter(region)
            sides = find_region_sides(region)

            price += area * perimeter
            price_discounted += area * sides

    return price, price_discounted


def find_regions(map, type):
    """
    Find the regions of a given type in the map.

    Parameters:
    map (np.ndarray): A numpy array representing the map.
    type (str): The type of plant to find.

    Returns:
    regions (list): A list of regions of the given type.
    """

    plants = np.array(np.where(map == type))

    regions = []
    while len(plants.T) != 0:

        plant = plants[:, 0]
        plants = np.delete(plants, 0, axis=1)

        region = [plant]
        for plant1 in region:

            for plant2 in plants.T:

                if is_adjacent(plant1, plant2):
                    region.append(plant2)
                    plants = np.delete(
                        plants, np.where(
                            np.all(
                                plants == plant2.reshape(
                                    2, 1), axis=0)), axis=1)

        regions.append(region)

    return regions


def is_adjacent(plant1, plant2):
    """
    Check if two plants are adjacent.

    Parameters:
    plant1 (tuple): The coordinates of the first plant.
    plant2 (tuple): The coordinates of the second plant.

    Returns:
    adjacent (bool): True if the plants are adjacent, False otherwise.
    """

    return abs(plant1[0] - plant2[0]) + abs(plant1[1] - plant2[1]) == 1


def find_region_perimeter(region):
    """
    Find the perimeter of a region.

    Parameters:
    region (list): A list of plants in the region.

    Returns:
    perimeter (int): The perimeter of the region.
    """

    perimeter = len(region) * 4

    for plant in region:

        for plant2 in region:
            if is_adjacent(plant, plant2):
                perimeter -= 1

    return perimeter


def find_region_sides(region):
    """
    Find the number of sides of a region.

    Parameters:
    region (list): A list of plants in the region.

    Returns:
    total_sides (int): The number of sides of the region.
    """

    region = [(int(plant[0]), int(plant[1])) for plant in region]

    up_sides = []
    down_sides = []
    left_sides = []
    right_sides = []

    for plant in region:

        if (plant[0], plant[1] - 1) not in region:
            left_sides.append((plant[0], plant[1]))
        if (plant[0], plant[1] + 1) not in region:
            right_sides.append((plant[0], plant[1] + 1))
        if (plant[0] - 1, plant[1]) not in region:
            up_sides.append((plant[0], plant[1]))
        if (plant[0] + 1, plant[1]) not in region:
            down_sides.append((plant[0] + 1, plant[1]))

    total_sides = 0

    left_ends = {(side[0] + 1, side[1])
                 for side in left_sides}  # Use a set for O(1) lookups
    for side in left_sides:
        if side not in left_ends:
            total_sides += 1

    right_ends = {(side[0] + 1, side[1]) for side in right_sides}
    for side in right_sides:
        if side not in right_ends:
            total_sides += 1

    up_ends = {(side[0], side[1] + 1) for side in up_sides}
    for side in up_sides:
        if side not in up_ends:
            total_sides += 1

    down_ends = {(side[0], side[1] + 1) for side in down_sides}
    for side in down_sides:
        if side not in down_ends:
            total_sides += 1

    return total_sides


def main():

    file_path = '2024/day12/input.txt'

    map = parse_input_file(file_path)

    price, price_discounted = get_total_price(map)
    print("Price:", price)
    print("Price discounted:", price_discounted)


if __name__ == '__main__':
    main()
