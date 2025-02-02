import numpy as np

def parse_input_file(file_path: str) -> np.ndarray:
    """
    Read and parse the content of the input file.

    This version uses numpy's built-in function to load numeric data from a text file,
    reducing manual parsing code and improving robustness.

    Parameters:
        file_path (str): The path to the input file.

    Returns:
        np.ndarray: A numpy array with the numbers from the input file.
    """
    # np.loadtxt automatically handles whitespace-separated numbers.
    return np.loadtxt(file_path, dtype=int)


def calculate_total_distance(numbers1: np.ndarray, numbers2: np.ndarray) -> int:
    """
    Calculate the total distance between two arrays after sorting them.

    The function sorts both arrays in ascending order, computes the absolute difference
    between each corresponding pair of elements, and sums these differences.

    Parameters:
        numbers1 (np.ndarray): The first array of numbers.
        numbers2 (np.ndarray): The second array of numbers.

    Returns:
        int: The total distance between the two arrays.
    """
    sorted1 = np.sort(numbers1)
    sorted2 = np.sort(numbers2)
    differences = np.abs(sorted1 - sorted2)
    total_distance = np.sum(differences)
    return int(total_distance)


def get_similarity_score(numbers1: np.ndarray, numbers2: np.ndarray) -> int:
    """
    Calculate the similarity score between two arrays.

    For each unique number in the first array, this function multiplies the number by
    the product of its frequency in both arrays and sums these values. This approach avoids
    repeatedly scanning the second array for every element in the first.

    Parameters:
        numbers1 (np.ndarray): The first array of numbers.
        numbers2 (np.ndarray): The second array of numbers.

    Returns:
        int: The similarity score.
    """
    # Calculate unique values and their counts for both arrays.
    unique1, counts1 = np.unique(numbers1, return_counts=True)
    unique2, counts2 = np.unique(numbers2, return_counts=True)
    count2_dict = dict(zip(unique2, counts2))
    
    score = 0
    for num, count1 in zip(unique1, counts1):
        count2 = count2_dict.get(num, 0)
        score += num * count1 * count2
    return score


def main() -> None:
    """
    Main function to run the Advent of Code Day 1 solution.
    
    It reads the input file, splits the data into two columns, calculates the total distance,
    and computes the similarity score, printing both results.
    """
    input_file = '2024/day01/input.txt'
    numbers = parse_input_file(input_file)
    
    # Check that the input contains at least two columns
    if numbers.ndim != 2 or numbers.shape[1] < 2:
        raise ValueError("Input file must contain at least two columns of numbers.")
    
    # Split the array into two separate arrays (columns)
    numbers1 = numbers[:, 0]
    numbers2 = numbers[:, 1]
    
    total_distance = calculate_total_distance(numbers1, numbers2)
    print("The total distance is", total_distance)
    
    similarity_score = get_similarity_score(numbers1, numbers2)
    print("The similarity score is", similarity_score)


if __name__ == '__main__':
    main()
