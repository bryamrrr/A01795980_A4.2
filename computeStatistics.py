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