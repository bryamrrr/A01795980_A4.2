# Instructions
# Req1. The program shall be invoked from a command line. The program shall receive a file as parameter. The file will contain a list of items (presumable numbers).
# Req 2. The program shall compute all descriptive statistics from a file containing numbers. The results shall be print on a screen and on a file named StatisticsResults.txt. All computation MUST be calculated using the basic algorithms, not functions or libraries. The descriptive statistics are mean, median, mode, standard deviation, and variance.
# Req 3. The program shall include the mechanism to handle invalid data in the file. Errors should be displayed in the console and the execution must continue.
# Req 4. The name of the program shall be computeStatistics.py
# Req 5. The minimum format to invoke the program shall be as follows: python computeStatistics.py fileWithData.txt
# Req 6. The program shall manage files having from hundreds of items to thousands of items.
# Req 7. The program should include at the end of the execution the time elapsed for the execution and calculus of the data. This number shall be included in the results file and on the screen.
# Req 8. Be compliant with PEP8.

# Test cases and evidence
# Record the execution. Use files included in the assignment.

import sys
import time

def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                print(f"Invalid data encountered and skipped: {line.strip()}")
    return numbers

# Descriptive statistics
def calculate_mean(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def calculate_mode(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, val in frequency.items() if val == max_freq]
    return modes if len(modes) > 1 else modes[0]

def calculate_standard_deviation(variance):
    return variance ** 0.5

def calculate_variance(numbers, mean):
    total = 0
    for num in numbers:
        total += (num - mean) ** 2
    return total / len(numbers)

def main():
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "StatisticsResults.txt"

    try:
        start_time = time.time()

        numbers = read_numbers_from_file(input_file)

        if not numbers:
            print("No valid data in the file.")
            sys.exit(1)

        mean = calculate_mean(numbers)
        median = calculate_median(numbers)
        mode = calculate_mode(numbers)
        variance = calculate_variance(numbers, mean)
        std_deviation = calculate_standard_deviation(variance)

        elapsed_time = time.time() - start_time

        results = (
            f"Descriptive Statistics:\n"
            f"Mean: {mean}\n"
            f"Median: {median}\n"
            f"Mode: {mode}\n"
            f"Variance: {variance}\n"
            f"Standard Deviation: {std_deviation}\n"
            f"Execution Time: {elapsed_time:.2f} seconds\n"
        )

        print(results)

        with open(output_file, 'w') as file:
            file.write(results)

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
