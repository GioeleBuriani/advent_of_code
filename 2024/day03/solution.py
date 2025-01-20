import numpy as np


def parse_input_file(file_path):
    '''
    Function to read and parse the content of the input file

    Parameters:
    file_path (str): The path to the input file

    Returns:
    lines (list): A list with the lines from the input file
    '''

    with open(file_path, 'r') as file:

        lines = file.readlines()

    return lines


def calculate_sections(line, enable):
    '''
    Function to calculate the product of the sections in a line

    Parameters:
    line (str): The line with the sections
    enable (bool): The flag to enable the calculation

    Returns:
    line_product (int): The product of the sections in the line
    enable (bool): The flag to enable the calculation
    '''

    # Initialize the variable to store the product of the sections
    line_product = 0

    # Iterate over the characters of the line
    for i in range(len(line)):

        # Check if the character is 'd', 'o', '(', and ')'
        if line[i] == 'd' and line[i + 1] == 'o' and line[i + 2] == '(' \
            and line[i + 3] == ')':
            enable = True

        # Check if the character is 'd', 'o', 'n', 't', '(', and ')'
        if line[i] == 'd' and line[i + 1] == 'o' and line[i + 2] == 'n' \
            and line[i + 3] == '\'' and line[i + 4] == 't' and line[i +5] == '(' \
                and line[i + 6] == ')':
            enable = False

        # Check if the character is 'm', 'u', 'l', '(', and a digit
        if line[i] == 'm' and line[i + 1] == 'u' and line[i + \
            2] == 'l' and line[i + 3] == '(' and line[i + 4].isdigit():

            # Find the index of the comma
            j = line[i + 5:i + 8].find(',')
            # Check if the comma is found and the characters before the comma
            # are digits
            if j >= 0 and np.all(line[i + 4:i + 5 + j].isdigit()):
                # Convert the characters to an integer
                num1 = int(line[i + 4:i + 5 + j])

                # Find the index of the closing parenthesis
                k = line[i + 7 + j:i + 10 + j].find(')')
                # Check if the closing parenthesis is found and the characters
                # before the closing parenthesis are digits
                if k >= 0 and np.all(line[i + 6 + j:i + 7 + j + k].isdigit()):
                    # Convert the characters to an integer
                    num2 = int(line[i + 6 + j:i + 7 + j + k])

                    # Calculate the product of the two numbers if the enable
                    # flag is True
                    if enable:
                        line_product += num1 * num2

    return line_product, enable


# Main function
def main():

    # Define the path to the input file
    file_path = '2024/day3/input.txt'

    # Read and parse the content of the file
    lines = parse_input_file(file_path)

    # Initialize the variable to store the total product and the enable flag
    total_product = 0
    enable = True

    # Iterate over the lines
    for line in lines:
        # Calculate the product of the sections in the line
        line_product, enable = calculate_sections(line, enable)
        # Add the product to the total product
        total_product += line_product

    # Print the total product
    print("The total product is", total_product)


if __name__ == '__main__':
    main()
