import re

def parse_input_file(file_path: str) -> list[str]:
    """
    Reads the input file and returns a list of lines without newline characters.

    Parameters:
        file_path (str): Path to the input file.

    Returns:
        list[str]: List of lines in the file.
    """
    with open(file_path, 'r') as file:
        # Using splitlines() automatically removes newline characters
        return file.read().splitlines()


def process_line(line: str, enable: bool) -> tuple[int, bool]:
    """
    Processes a line of commands and calculates the product from 'mul' commands.
    It toggles the enable flag when encountering 'do()' and "don't()" commands.

    The recognized commands are:
      - do(): Sets enable to True.
      - don't(): Sets enable to False.
      - mul(x,y): If enable is True, adds x*y to the running product.

    Parameters:
        line (str): A line containing the commands.
        enable (bool): The initial state of the enable flag.

    Returns:
        tuple[int, bool]: The product sum from the line and the final state of enable.
    """
    line_product = 0

    # Compile a regular expression that matches:
    #  - do() command, or
    #  - don't() command, or
    #  - mul(x,y) command with x and y as integers.
    pattern = re.compile(r"(do\(\))|(don't\(\))|(mul\((\d+),(\d+)\))")
    
    # Process commands in the order they appear in the line.
    for match in pattern.finditer(line):
        if match.group(1):          # Matches do()
            enable = True
        elif match.group(2):        # Matches don't()
            enable = False
        elif match.group(3):        # Matches mul(x,y)
            if enable:
                num1 = int(match.group(4))
                num2 = int(match.group(5))
                line_product += num1 * num2

    return line_product, enable


def main() -> None:
    file_path = '2024/day03/input.txt'
    lines = parse_input_file(file_path)
    total_product = 0
    enable = True

    # Process each line and accumulate the product.
    for line in lines:
        line_product, enable = process_line(line, enable)
        total_product += line_product

    print("The total product is", total_product)


if __name__ == '__main__':
    main()
