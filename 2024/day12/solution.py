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

    for type in plant_types:

        regions = find_regions(map, type)

        for region in regions:
            
            area = len(region)

            perimeter = find_region_perimeter(region)

            price += area * perimeter

    return price


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



def main():

    file_path = '2024/day12/input.txt'

    map = parse_input_file(file_path)

    price = get_total_price(map)
    print("Price:", price)


if __name__ == '__main__':
    main()