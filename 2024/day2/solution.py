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
            numbers = np.array([int(number) for number in numbers])

            # Append the numbers to the list
            numbers_list.append(numbers)

    return numbers_list


def check_safety(numbers):
    '''
    Function to check the safety of the reports

    Parameters:
    numbers (list): The list with the reports

    Returns:
    safe_reports (int): The number of safe reports
    '''

    # Initialize the counter for the safe reports
    safe_reports = 0

    # Iterate over the reports
    for report in numbers:

        # Check if the report is safe
        if check_safety_condition(report):
            safe_reports += 1
        elif problem_dampener(report):
            safe_reports += 1

    return safe_reports


def check_safety_condition(report):
    '''
    Function to check if a report is safe

    Parameters:
    report (np.array): The report to check

    Returns:
    is_safe (bool): True if the report is safe, False otherwise
    '''

    # Check if the report is sorted in ascending order and the difference
    # between the numbers is less than 4
    if np.all(np.diff(report) > 0) and np.all(np.diff(report) < 4):
        return True
    # Check if the report is sorted in descending order and the difference
    # between the numbers is less than 4
    elif np.all(np.diff(report) < 0) and np.all(np.diff(report) > -4):
        return True
    # If the report is not sorted or the difference between the numbers is
    # greater than 4
    else:
        return False


def problem_dampener(report):

    # Iterate over the indexes in the report
    for i in range(len(report)):

        # Remove the level from the array
        report_copy = np.delete(report, i)

        # Check if the report is safe
        if check_safety_condition(report_copy):
            return True

    return False


# Main function
def main():

    # Define the path to the input file
    file_path = '2024/day2/input.txt'

    # Read and parse the content of the file
    numbers = parse_input_file(file_path)

    # Check the safety of the reports
    safe_reports = check_safety(numbers)

    # Print the number of safe reports
    print(f'The number of safe reports is: {safe_reports}')


if __name__ == '__main__':
    main()
