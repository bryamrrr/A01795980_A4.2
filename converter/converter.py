"""
This script processes a file containing numbers, converting each number to
binary and hexadecimal representations.

Usage:
    python convertNumbers.py fileWithData.txt
"""

# Instructions
# Req1. The program shall be invoked from a command line.
# The program shall receive a file as parameter.
# The file will contain a list of items (presumable numbers).
# Req 2. The program shall convert the numbers to binary and hexadecimal base.
# The results shall be print on a screen and on a file named ConvertionResults.txt.
# All computation MUST be calculated using the basic algorithms, not functions or libraries.
# Req 3. The program shall include the mechanism to handle invalid data in the file.
# Errors should be displayed in the console and the execution must continue.
# Req 4. The name of the program shall be convertNumbers.py
# Req 5. The minimum format to invoke the program shall be as follows:
# python convertNumbers.py fileWithData.txt
# Req 6. The program shall manage files having from hundreds of items to thousands of items.
# Req 7. The program should include at the end of the execution the time elapsed for
# the execution and calculus of the data. This number shall be included in the results file
# and on the screen.
# Req 8. Be compliant with PEP8

import sys
import time

def to_binary(n):
    """
    Converts a decimal number to its binary representation.
    
    Args:
        n (int): The decimal number to convert.
    
    Returns:
        str: The binary representation of the number.
    """
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def to_hexadecimal(n):
    """
    Converts a decimal number to its hexadecimal representation.
    
    Args:
        n (int): The decimal number to convert.
    
    Returns:
        str: The hexadecimal representation of the number.
    """
    hex_chars = "0123456789ABCDEF"
    if n == 0:
        return "0"
    hexadecimal = ""
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n //= 16
    return hexadecimal

def read_numbers_from_file(filename):
    """
    Reads a file and extracts valid numerical data, skipping invalid entries.
    
    Args:
        filename (str): The path to the input file.
    
    Returns:
        list: A list of valid floating-point numbers from the file.
    """
    numbers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                print(f"Invalid data encountered and skipped: {line.strip()}")
    return numbers

def main():
    """
    Reads a file containing numbers, converts them to binary and hexadecimal,
    and writes the results to a file while also printing them.
    
    Args:
        filename (str): The name of the file to process.
        
    Raises:
        FileNotFoundError: If the input file does not exist.
    """
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "ConvertionResults.txt"

    try:
        results = []
        start_time = time.time()

        numbers = read_numbers_from_file(input_file)

        for number in numbers:
            num = int(number)
            binary = to_binary(num)
            hexadecimal = to_hexadecimal(num)
            results.append(f"{num} -> Binary: {binary}, Hexadecimal: {hexadecimal}")

        elapsed_time = time.time() - start_time
        results.append(f"Execution Time: {elapsed_time:.6f} seconds")

        with open(output_file, "w", encoding='utf-8') as file:
            file.write("\n".join(results))

        print("\n".join(results))
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
