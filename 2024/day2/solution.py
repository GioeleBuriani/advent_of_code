import numpy as np


def parse_input_file(file_path):
    '''
    Function to read and parse the content of the input file

    Parameters:
    file_path (str): The path to the input file

    Returns:
    numbers (np.array): A numpy array with the numbers from the input file
    '''

    with open(file_path, 'r') as file:

        # Initialize the list to store the numbers
        numbers_list = []

        # Read the file line by line
        for line in file:

            # Split the line by the spaces
            numbers = line.split(' ')

            # Convert the numbers to integers
            numbers = [int(number) for number in numbers]

            # Append the numbers to the list
            numbers_list.append(numbers)

    # Convert the list to a numpy array
    numbers = np.array(numbers_list)

    return numbers



# Main function
def main():

    # Define the path to the input file
    file_path = '2024/day2/input.txt'

    # Read and parse the content of the file
    numbers = parse_input_file(file_path)

    print ("test")


if __name__ == '__main__':
    main()
