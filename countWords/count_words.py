"""
wordCount.py

This code reads a text file, counts the frequency of distinct words,
and writes the results to both the console and a file named WordCountResults.txt.

Usage:
    python wordCount.py fileWithData.txt
"""

# Instructions
# Req1. The program shall be invoked from a command line.
# The program shall receive a file as parameter.
# The file will contain a words (presumable between spaces).
# Req 2. The program shall identify all distinct words and the frequency of them
# (how many times the word “X” appears in the file).
# The results shall be print on a screen and on a file named WordCountResults.txt.
# All computation MUST be calculated using the basic algorithms,
# not functions orlibraries.
# Req 3. The program shall include the mechanism to handle invalid data in the
# file. Errors should be displayed in the console and the execution must continue.
# Req 4. The name of the program shall be wordCount.py
# Req 5. The minimum format to invoke the program shall be as follows:
# python wordCount.py fileWithData.txt
# Req 6. The program shall manage files having from hundreds of items to
# thousands of items.
# Req 7. The program should include at the end of the execution the
# time elapsed for the execution and calculus of the data.
# This number shall be included in the results file and on the screen.
# Req 8. Be compliant with PEP8

import sys
import time
import re

def get_words_from_file(file_path):
    """
    Reads the content of the file and extracts words.
    
    Args:
        file_path (str): Path to the input text file.
    
    Returns:
        list: A list of words extracted from the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = re.findall(r'\b\w+\b', content.lower())  # Extracts words using regex
            return words
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

def count_words(words):
    """
    Counts the frequency of each distinct word in a list.
    
    Args:
        words (list): List of words extracted from the file.
    
    Returns:
        dict: A dictionary where keys are words and values are their frequency.
    """
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def write_results(word_count, elapsed_time):
    """
    Writes the word frequency results and execution time to a file.
    
    Args:
        word_count (dict): Dictionary of word frequencies.
        elapsed_time (float): Time elapsed during execution.
    """
    with open("WordCountResults.txt", 'w', encoding='utf-8') as output_file:
        for word, count in sorted(word_count.items(), key=lambda item: item[1], reverse=True):
            output_file.write(f"{word}: {count}\n")
        output_file.write(f"\nExecution Time: {elapsed_time:.4f} seconds\n")

def main():
    """
    Main function to read a file, counts word frequency, prints results, and writes them to a file.
    """
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    words = get_words_from_file(file_path)
    word_count = count_words(words)
    elapsed_time = time.time() - start_time

    for word, count in sorted(word_count.items(), key=lambda item: item[1], reverse=True):
        print(f"{word}: {count}")
    print(f"\nExecution Time: {elapsed_time:.4f} seconds")

    write_results(word_count, elapsed_time)

if __name__ == "__main__":
    main()
