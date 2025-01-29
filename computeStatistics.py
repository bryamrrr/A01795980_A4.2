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

# Function to read a file with numbers
def read_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            numbers.append(float(line.strip()))
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

