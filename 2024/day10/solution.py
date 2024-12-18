import numpy as np


def parse_input_file(file_path):
    """
    Parse the input file and return the topographical map as a numpy array.

    Parameters:
    file_path (str): The path to the input file.

    Returns:
    topo_map (numpy array): The topographical map as a numpy array.
    """

    with open(file_path, 'r') as file:

        lines = [list(map(int, line.strip())) for line in file.readlines()]
        topo_map = np.array(lines, dtype=int)

    return topo_map


def find_trailheads_scores(topo_map):
    """
    Find the scores of all the trailheads in the topographical map.

    Parameters:
    topo_map (numpy array): The topographical map as a numpy array.

    Returns:
    total_score (int): The total score of all the trailheads in the topographical map.
    """

    scores = []

    for i in range(topo_map.shape[0]):
        for j in range(topo_map.shape[1]):

            if topo_map[i, j] == 0:

                nines = []
                nines = find_trails_score((i, j), topo_map, nines)

                score = len(nines)
                scores.append(score)

    total_score = sum(scores)

    return total_score


def find_trails_score(trailhead, topo_map, nines):
    """
    Find the score of a trailhead in the topographical map.

    Parameters:
    trailhead (tuple): The coordinates of the trailhead.
    topo_map (numpy array): The topographical map as a numpy array.
    nines (list): The list of nine positions for the trailhead.

    Returns:
    nines (list): The updated list of nine positions for the trailhead.
    """

    value = topo_map[trailhead]

    if trailhead[0] < topo_map.shape[0] - 1:
        if topo_map[trailhead[0] + 1, trailhead[1]] == value + 1:
            if value == 8 and [trailhead[0] + 1, trailhead[1]] not in nines:
                nines.append([trailhead[0] + 1, trailhead[1]])
            else:
                nines = find_trails_score(
                    (trailhead[0] + 1, trailhead[1]), topo_map, nines)

    if trailhead[0] > 0:
        if topo_map[trailhead[0] - 1, trailhead[1]] == value + 1:
            if value == 8 and [trailhead[0] - 1, trailhead[1]] not in nines:
                nines.append([trailhead[0] - 1, trailhead[1]])
            else:
                nines = find_trails_score(
                    (trailhead[0] - 1, trailhead[1]), topo_map, nines)

    if trailhead[1] < topo_map.shape[1] - 1:
        if topo_map[trailhead[0], trailhead[1] + 1] == value + 1:
            if value == 8 and [trailhead[0], trailhead[1] + 1] not in nines:
                nines.append([trailhead[0], trailhead[1] + 1])
            else:
                nines = find_trails_score(
                    (trailhead[0], trailhead[1] + 1), topo_map, nines)

    if trailhead[1] > 0:
        if topo_map[trailhead[0], trailhead[1] - 1] == value + 1:
            if value == 8 and [trailhead[0], trailhead[1] - 1] not in nines:
                nines.append([trailhead[0], trailhead[1] - 1])
            else:
                nines = find_trails_score(
                    (trailhead[0], trailhead[1] - 1), topo_map, nines)

    return nines


def find_trailheads_ratings(topo_map):
    """
    Find the ratings of all the trailheads in the topographical map.

    Parameters:
    topo_map (numpy array): The topographical map as a numpy array.

    Returns:
    total_rating (int): The total rating of all the trailheads in the topographical map.
    """

    ratings = []

    for i in range(topo_map.shape[0]):
        for j in range(topo_map.shape[1]):

            if topo_map[i, j] == 0:

                counter = 0
                rating = find_trails_rating((i, j), topo_map, counter)

                ratings.append(rating)

    total_rating = sum(ratings)

    return total_rating


def find_trails_rating(trailhead, topo_map, counter):
    """
    Find the rating of a trailhead in the topographical map.

    Parameters:
    trailhead (tuple): The coordinates of the trailhead.
    topo_map (numpy array): The topographical map as a numpy array.
    counter (int): The counter for the rating of the trailhead.

    Returns:
    counter (int): The updated counter for the rating of the trailhead.
    """

    value = topo_map[trailhead]

    if trailhead[0] < topo_map.shape[0] - 1:
        if topo_map[trailhead[0] + 1, trailhead[1]] == value + 1:
            if value == 8:
                counter += 1
            else:
                counter = find_trails_rating(
                    (trailhead[0] + 1, trailhead[1]), topo_map, counter)

    if trailhead[0] > 0:
        if topo_map[trailhead[0] - 1, trailhead[1]] == value + 1:
            if value == 8:
                counter += 1
            else:
                counter = find_trails_rating(
                    (trailhead[0] - 1, trailhead[1]), topo_map, counter)

    if trailhead[1] < topo_map.shape[1] - 1:
        if topo_map[trailhead[0], trailhead[1] + 1] == value + 1:
            if value == 8:
                counter += 1
            else:
                counter = find_trails_rating(
                    (trailhead[0], trailhead[1] + 1), topo_map, counter)

    if trailhead[1] > 0:
        if topo_map[trailhead[0], trailhead[1] - 1] == value + 1:
            if value == 8:
                counter += 1
            else:
                counter = find_trails_rating(
                    (trailhead[0], trailhead[1] - 1), topo_map, counter)

    return counter


def main():

    file_path = '2024/day10/input.txt'

    topo_map = parse_input_file(file_path)

    total_score = find_trailheads_scores(topo_map)
    print("Total score: ", total_score)

    total_rating = find_trailheads_ratings(topo_map)
    print("Total rating: ", total_rating)


if __name__ == '__main__':
    main()
