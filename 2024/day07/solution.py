import numpy as np
from itertools import product


def parse_input_file(file_path):
    """
    Parse the input file and return a list of equations.

    Parameters:
    file_path (str): The path to the input file.

    Returns:
    equations (list): The list of equations.
    """

    with open(file_path, 'r') as file:

        equations = []

        for line in file:

            equation = [int(x) if x.isdigit() else x for x in line.split()]
            equation[0] = int(equation[0][:-1])

            equations.append(equation)

    return equations


def check_feasibility(equation, n_op):
    """
    Check if the equation is feasible.

    Parameters:
    equation (list): The equation to check.
    n_op (int): The number of operators to use.

    Returns:
    feasible (bool): True if the equation is feasible, False otherwise.
    """

    result = equation[0]
    terms = equation[1:]

    operators = generate_operators(terms, n_op)

    for operator in operators:

        if do_operation(terms, operator) == result:
            return True

    return False


def generate_operators(terms, n_op):
    """
    Generate all possible operators for the equation.

    Parameters:
    terms (list): The list of terms in the equation.
    n_op (int): The number of operators to use.

    Returns:
    operators (list): The list of operators.
    """

    digits = range(n_op)
    operators = list(product(digits, repeat=len(terms) - 1))

    return operators


def do_operation(terms, operators):
    """
    Perform the operation on the equation.

    Parameters:
    terms (list): The list of terms in the equation.
    operators (list): The list of operators.

    Returns:
    result (int): The result of the operation.
    """

    result = terms[0]

    for i in range(len(operators)):

        if operators[i] == 0:
            result += terms[i + 1]
        elif operators[i] == 1:
            result *= terms[i + 1]
        elif operators[i] == 2:
            result = int(str(result) + str(terms[i + 1]))

    return result


def main():

    file_path = '2024/day7/input.txt'

    equations = parse_input_file(file_path)

    results = []
    for equation in equations:
        if check_feasibility(equation, n_op=2):
            equations.remove(equation)
            results.append(equation[0])

    for equation in equations:
        if check_feasibility(equation, n_op=3):
            results.append(equation[0])

    calibration_result = np.sum(results)
    print("Calibration result: ", calibration_result)


if __name__ == '__main__':
    main()
