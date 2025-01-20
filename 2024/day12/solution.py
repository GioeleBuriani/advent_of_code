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

    plants = np.array(np.where(map == type))

    regions = []
    while len(plants.T) != 0:
        
        plant = plants[:,0]
        plants = np.delete(plants, 0, axis=1)

        region = [plant]
        for plant1 in region:

            for plant2 in plants.T:

                if is_adjacent(plant1, plant2):
                    region.append(plant2)
                    plants = np.delete(plants, np.where(np.all(plants == plant2.reshape(2,1), axis=0)), axis=1)

        regions.append(region)

    return regions


def is_adjacent(plant1, plant2):

    return abs(plant1[0] - plant2[0]) + abs(plant1[1] - plant2[1]) == 1


def find_region_perimeter(region):

    perimeter = len(region) * 4

    for plant in region:

        for plant2 in region:
            if is_adjacent(plant, plant2):
                perimeter -= 1

    return perimeter


def find_region_sides(region):

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

    left_ends = []
    for side in left_sides:
        if side not in left_ends:
            left_ends.append((side[0] + 1, side[1]))
    
    right_ends = []
    for side in right_sides:
        if side not in right_ends:
            right_ends.append((side[0] + 1, side[1]))
    
    up_ends = []
    for side in up_sides:
        if side not in up_ends:
            up_ends.append((side[0], side[1] + 1))

    down_ends = []
    for side in down_sides:
        if side not in down_ends:
            down_ends.append((side[0], side[1] + 1))

    total_sides = len(left_ends) + len(right_ends) + len(up_ends) + len(down_ends)
    print(total_sides)

    # print(region)
    # print(np.array(up_sides))
    # print(np.array(down_sides))
    # print(np.array(left_sides))
    # print(np.array(right_sides))
    # print("-----------------")

    return total_sides
    


def main():

    file_path = '2024/day12/test_input.txt'

    map = parse_input_file(file_path)

    price, price_discounted = get_total_price(map)
    print("Price:", price)
    print("Price discounted:", price_discounted)


if __name__ == '__main__':
    main()