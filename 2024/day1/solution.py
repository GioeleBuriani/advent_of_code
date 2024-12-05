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
            numbers = line.split('   ')

            # Convert the numbers to integers
            numbers = [int(number) for number in numbers]

            # Append the numbers to the list
            numbers_list.append(numbers)
    
    # Convert the list to a numpy array
    numbers = np.array(numbers_list)

    return numbers
    

def calculate_total_distance(numbers1, numbers2):

    '''
    Function to calculate the total distance between two arrays

    Parameters:
    numbers1 (np.array): The first array of numbers
    numbers2 (np.array): The second array of numbers

    Returns:
    total_distance (int): The total distance between the two arrays
    '''

    # Order the numbers in ascending order
    numbers1 = np.sort(numbers1)
    numbers2 = np.sort(numbers2)
    
    # Make the element wise distance between the two arrays
    distance = np.abs(numbers1 - numbers2)

    # Calculate the total distance
    total_distance = np.sum(distance)

    return total_distance


def get_similarity_score(numbers1, numbers2):

    score = 0

    # Iterate over the first array
    for number1 in numbers1:

        # Count the number of elements in the second array that are equal to the current element
        appearances = np.sum(numbers2 == number1)

        # Add the score to the total score
        score += appearances * number1

    return score


# Main function
def main():

    # Define the path to the input file
    file_path = '2024/day1/input.txt'

    # Read and parse the content of the file
    numbers = parse_input_file(file_path)

    # Split the numbers into two arrays
    numbers1 = numbers[:, 0]
    numbers2 = numbers[:, 1]

    # Calculate the total distance
    total_distance = calculate_total_distance(numbers1, numbers2)

    # Print the total distance
    print("The total distance is", total_distance)

    # Calculate the similarity score
    similarity_score = get_similarity_score(numbers1, numbers2)

    # Print the similarity score
    print("The similarity score is", similarity_score)

    

if __name__ == '__main__':
    main()