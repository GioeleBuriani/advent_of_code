import numpy as np


def parse_input_file(file_path):

    with open(file_path, 'r') as file:

        stone_line = np.array(list(map(int, file.readline().split())))
        
    return stone_line


def update_line(stone_line):

    for i in range(75):
        print("Iteration: ", i)

        new_line = []
        for j in range(len(stone_line)):

            if stone_line[j] == 0:
                new_line.append(1)

            elif len(str(stone_line[j])) % 2 == 0:

                mid = len(str(stone_line[j])) // 2
                stone1 = int(str(stone_line[j])[:mid])
                stone2 = int(str(stone_line[j])[mid:])
                
                new_line.append(stone1)
                new_line.append(stone2)
            
            else:
                new_line.append(stone_line[j] * 2024)

        stone_line = np.array(new_line)
    
    return stone_line


def main():

    file_path = '2024/day11/input.txt'

    stone_line = parse_input_file(file_path)

    updated_line = update_line(stone_line)

    number_of_stones = len(updated_line)

    print("Number of stones: ", number_of_stones)

if __name__ == '__main__':
    main()
