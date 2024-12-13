import numpy as np


def parse_input_file(file_path):

    with open(file_path, 'r') as file:

        equations = []

        for line in file:

            equation = np.array(line.split())
            equations.append(equation)

    return equations


def check_feasibility(equation):

    result = equation[0]
    terms = equation[1:]


def main():

    file_path = '2024/day7/test_input.txt'

    equations = parse_input_file(file_path)

    print(equations)

    


if __name__ == '__main__':
    main()
