import numpy as np
from itertools import combinations


def parse_input_file(file_path):

    with open(file_path, 'r') as file:

        line = file.readline().strip()
        disk_map = [int(digit) for digit in line]
        
    return disk_map


def visualize_blocks(disk_map):

    id = 0
    visualization = []

    for i in range(len(disk_map)):

        if i % 2 == 0:
            for j in range(disk_map[i]):
                visualization.append(id)
            id += 1
        
        if i % 2 != 0:
            for j in range(disk_map[i]):
                visualization.append('.')

    return visualization


def rearrange_visualization(visualization):

    arranged_visualization = visualization.copy()
    end = False
    
    for i in range(1, len(visualization)):

        if end:
            break

        if visualization[-i] != '.':
            
            for j in range(len(visualization)):
                if j >= len(visualization) - i:
                    end = True
                    break
                if arranged_visualization[j] == '.':
                    arranged_visualization[j] = visualization[-i]
                    arranged_visualization[-i] = '.'
                    break
    
    return arranged_visualization


def calulate_checksum(arranged_visualization):

    products = []
    for i in range(len(arranged_visualization)):
        
        if arranged_visualization[i] == '.':
            break

        products.append(i * arranged_visualization[i])

    checksum = sum(products)

    return checksum


def expand_disk_map(disk_map):

    expansion = []
    id = 0

    for i in range(len(disk_map)):

        if i % 2 == 0:
            expansion.append(id)
            id += 1
        
        if i % 2 != 0:
            expansion.append(-1)

    expanded_map = np.stack([disk_map, expansion])
    
    return expanded_map


def rearrange_expanded_map(expanded_map):

    arranged_map = expanded_map.copy()
    end = False

    print(visualize_expanded_map(arranged_map))
    print('-------------------------------------------------')

    for i in range(1, expanded_map.shape[1]):

        if end:
            break

        if expanded_map[1, -i] != -1:

            for j in range(expanded_map.shape[1]):

                if j >= expanded_map.shape[1] - i:
                    break

                if arranged_map[1, j] == -1 and arranged_map[0, j] >= expanded_map[0, -i]:
                    
                    arranged_map = np.insert(arranged_map, j, expanded_map[:,-i], axis=1)
                    
                    arranged_map[0, j+1] -= arranged_map[0, j]

                    arranged_map[1, -i] = -1
                    print(visualize_expanded_map(arranged_map))
                    print('-------------------------------------------------')
                    break
    
    return arranged_map


def visualize_expanded_map(expanded_map):

    visualization = []

    for i in range(expanded_map.shape[1]):

        if expanded_map[1, i] == -1:
            for j in range(expanded_map[0, i]):
                visualization.append('.')
        else:
            for j in range(expanded_map[0, i]):

                value = str(expanded_map[1, i])

                visualization.append(str(expanded_map[1, i]))

    return np.array(visualization)
                    
            
            



def main():

    file_path = '2024/day9/test_input.txt'

    disk_map = parse_input_file(file_path)

    # visualization = visualize_blocks(disk_map)

    # arranged_visualization = rearrange_visualization(visualization)

    # checksum = calulate_checksum(arranged_visualization)

    # print("Checksum: ", checksum)

    expanded_map = expand_disk_map(disk_map)

    arranged_map = rearrange_expanded_map(expanded_map)

    visualization = visualize_expanded_map(arranged_map)

    print(visualization)


if __name__ == '__main__':
    main()
