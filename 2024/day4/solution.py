import numpy as np

def parse_input_file(file_path):

    with open(file_path, 'r') as file:

        lines = file.readlines()
        grid = np.array([list(line.strip()) for line in lines])

    return grid


def find_words(grid):

    rows, cols = grid.shape
    words = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 'X':

                start_row = max(0, i-1)
                end_row = min(rows, i+2)
                start_col = max(0, j-1)
                end_col = min(cols, j+2)
                subgrid = grid[start_row:end_row, start_col:end_col]
                print(subgrid)

                X_index = np.array(np.where(subgrid == 'M'))
                # Subtract 1 from the indexes emlement-wise
                print(X_index)

    return X_index




def main():

    file_path = '2024/day4/test_input.txt'

    grid = parse_input_file(file_path)

    index = find_words(grid)



if __name__ == '__main__':
    main()
