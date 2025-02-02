from typing import List
import numpy as np


def parse_input_file(file_path: str) -> List[np.ndarray]:
    """
    Reads and parses the input file into a list of numpy arrays.

    Each line in the file should contain integers separated by whitespace.

    Parameters:
        file_path (str): The path to the input file.

    Returns:
        List[np.ndarray]: A list where each element is a numpy array of integers from a line.
    """
    reports = []  # Each report is a numpy array representing one line of integers.
    with open(file_path, 'r') as file:
        for line in file:
            # Remove leading/trailing whitespace and split on any whitespace.
            numbers_str = line.strip().split()
            # Convert the strings to integers and then create a numpy array.
            numbers_array = np.array([int(num) for num in numbers_str])
            reports.append(numbers_array)
    return reports


def check_safety(reports: List[np.ndarray]) -> int:
    """
    Determines the number of safe reports.

    A report is considered safe if it meets the safety condition directly or can be
    made safe by removing one number (dampening).

    Parameters:
        reports (List[np.ndarray]): The list of reports.

    Returns:
        int: The count of safe reports.
    """
    safe_count = 0
    for report in reports:
        # A report is safe if it meets the condition or can be fixed by removing one element.
        if check_safety_condition(report) or problem_dampener(report):
            safe_count += 1
    return safe_count


def check_safety_condition(report: np.ndarray) -> bool:
    """
    Checks if a report is safe based on its ordering and the differences between consecutive numbers.

    A report is safe if:
      - It is strictly increasing with each consecutive difference less than 4, or
      - It is strictly decreasing with each consecutive difference greater than -4.

    Parameters:
        report (np.ndarray): The report to check.

    Returns:
        bool: True if the report is safe, False otherwise.
    """
    differences = np.diff(report)  # Compute differences once to avoid redundancy
    if np.all(differences > 0) and np.all(differences < 4):
        return True
    if np.all(differences < 0) and np.all(differences > -4):
        return True
    return False


def problem_dampener(report: np.ndarray) -> bool:
    """
    Checks if a report can be made safe by removing one element.

    Parameters:
        report (np.ndarray): The report to check.

    Returns:
        bool: True if removing one element results in a safe report, False otherwise.
    """
    for index in range(len(report)):
        # Create a version of the report without the element at the current index.
        report_without_element = np.delete(report, index)
        if check_safety_condition(report_without_element):
            return True
    return False


def main() -> None:
    """
    Main execution function.
    """
    file_path = '2024/day02/input.txt'
    reports = parse_input_file(file_path)
    safe_reports = check_safety(reports)
    print(f'The number of safe reports is: {safe_reports}')


if __name__ == '__main__':
    main()
