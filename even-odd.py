# Ray Allessandra D. Pacis | BSCPE 1-5 

# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file; the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. 
# The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

# import modules
import pyfiglet
import time
from colorama import Fore, Back, Style


# open numbers.txt , even.txt, and odd.txt
with open("numbers.txt") as input_file, open("even.txt", 'w') as even_output, open("odd.txt", 'w') as odd_output:

    # for each line
    for line in input_file:
        # convert each line to integer
        extract_number = int(line)
        # if extracted number is even
        if extract_number % 2 == 0:
            # put extracted number to even.txt
            even_output.write(str(extract_number) + '\n')
        # else if the extracted number is odd
        elif extract_number % 2 == 1:
            # put extracted number to odd.txt
            odd_output.write(str(extract_number) + '\n')

# end of program