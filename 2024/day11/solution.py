import numpy as np


def parse_input_file(file_path):
    """
    Parse the input file and return the stone line.

    Parameters:
    file_path (str): The path to the input file.

    Returns:
    stone_line (numpy array): The stone line.
    """

    with open(file_path, 'r') as file:

        stone_line = np.array(list(map(int, file.readline().split())))

    return stone_line


def update_line(stone_line, blinks):
    """
    Update the stone line with the given number of blinks.

    Parameters:
    stone_line (numpy array): The stone line.
    blinks (int): The number of blinks.

    Returns:
    number_of_stones (int): The number of stones in the stone line.
    """

    results = 0
    memo = {}
    for i in range(len(stone_line)):

        result = expand_step(stone_line[i], blinks, memo)
        results += result

    return results


def expand_step(stone, blinks, memo):
    """
    Expand the stone line with the given number of blinks.

    Parameters:
    stone (int): The stone.
    blinks (int): The number of blinks.
    memo (dict): The memoization dictionary.

    Returns:
    result (int): The number of stones in the expanded stone line.
    """

    if blinks == 0:

        return 1

    if (stone, blinks) in memo:

        return memo[(stone, blinks)]

    if stone == 0:

        next_stones = [1]

    elif len(str(stone)) % 2 == 0:

        mid = len(str(stone)) // 2
        stone1 = int(str(stone)[:mid])
        stone2 = int(str(stone)[mid:])

        next_stones = [stone1, stone2]

    else:

        next_stones = [stone * 2024]

    result = 0
    for next_stone in next_stones:

        result += expand_step(next_stone, blinks - 1, memo)

    memo[(stone, blinks)] = result

    return result


def main():

    file_path = '2024/day11/input.txt'

    stone_line = parse_input_file(file_path)

    number_of_stones = update_line(stone_line, 75)

    print("Number of stones: ", number_of_stones)


if __name__ == '__main__':
    main()