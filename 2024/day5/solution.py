import numpy as np


def parse_input_file(file_path):

    with open(file_path, 'r') as file:

        lines = file.readlines()
        grid = np.array([list(line.strip()) for line in lines])

    return grid


def main():

    file_path = '2024/day5/test_input.txt'

    test = parse_input_file(file_path)

    print("Number of words:", )


if __name__ == '__main__':
    main()
