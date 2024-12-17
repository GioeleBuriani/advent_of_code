import numpy as np


def parse_input_file(file_path):

    with open(file_path, 'r') as file:

        lines = [list(map(int, line.strip())) for line in file.readlines()]
        topo_map = np.array(lines, dtype=int)

    return topo_map


def find_trailheads_scores(topo_map):

    scores = []

    for i in range(topo_map.shape[0]):
        for j in range(topo_map.shape[1]):

            if topo_map[i, j] == 0:

                score = find_trails((i, j), topo_map, 0)
                print(score)

def find_trails(trailhead, topo_map, counter):

    value = topo_map[trailhead]

    if trailhead[0] < topo_map.shape[0] - 1:
        if topo_map[trailhead[0] + 1, trailhead[1]] == value + 1:
            if value == 8:
                counter += 1
            else:
                counter = find_trails((trailhead[0] + 1, trailhead[1]), topo_map, counter)

    if trailhead[0] > 0:
        if topo_map[trailhead[0] - 1, trailhead[1]] == value + 1:
            if value == 8:
                counter += 1
            else:
                counter = find_trails((trailhead[0] - 1, trailhead[1]), topo_map, counter)

    if trailhead[1] < topo_map.shape[1] - 1:
        if topo_map[trailhead[0], trailhead[1] + 1] == value + 1:
            if value == 8:
                counter += 1
            else:
                counter = find_trails((trailhead[0], trailhead[1] + 1), topo_map, counter)

    if trailhead[1] > 0:
        if topo_map[trailhead[0], trailhead[1] - 1] == value + 1:
            if value == 8:
                counter += 1
            else:
                counter = find_trails((trailhead[0], trailhead[1] - 1), topo_map, counter)

    return counter


def main():

    file_path = '2024/day10/test_input.txt'

    topo_map = parse_input_file(file_path)

    find_trailheads_scores(topo_map)

if __name__ == '__main__':
    main()
