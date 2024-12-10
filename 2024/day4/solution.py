import numpy as np


def parse_input_file(file_path):

    with open(file_path, 'r') as file:

        lines = file.readlines()
        grid = np.array([list(line.strip()) for line in lines])

    return grid


def find_xmas(grid):

    rows, cols = grid.shape
    words = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 'X':

                for m in range(-1, 2):
                    for n in range(-1, 2):

                        if 0 <= i + m * 3 < rows and 0 <= j + n * 3 < cols:

                            if grid[i + m,
                                    j + n] == 'M' and grid[i + m * 2,
                                                           j + n * 2] == 'A' and grid[i + m * 3,
                               j + n * 3] == 'S':
                                words += 1

    return words


def find_x_mas(grid):

    rows, cols = grid.shape
    words = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 'A':

                counter = 0

                for m in [-1, 1]:
                    for n in [-1, 1]:

                        if 0 <= i + m < rows and 0 <= j + \
                                n < cols and 0 <= i - m < rows and 0 <= j - n < cols:

                            if grid[i + m,
                                    j + n] == 'M' and grid[i - m,
                                                           j - n] == 'S':
                                counter += 1

                if counter == 2:
                    words += 1

    return words


def main():

    file_path = '2024/day4/input.txt'

    grid = parse_input_file(file_path)

    words = find_x_mas(grid)

    print("Number of words:", words)


if __name__ == '__main__':
    main()
