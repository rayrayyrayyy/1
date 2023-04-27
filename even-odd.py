# Ray Allessandra D. Pacis | BSCPE 1-5 

# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file; the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. 
# The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

# import modules
import pyfiglet
import time
from colorama import Fore, Back, Style

# intro
even_odd = pyfiglet.figlet_format('\n' + "EVEN and ODD!", font = "tanja", width = 150, justify = "center")
print(Fore.LIGHTRED_EX + even_odd)
print(Style.RESET_ALL)
print(Fore.YELLOW + "-___-"*30)
print(Style.RESET_ALL)
instruction = "INSTRUCTION: Please enter 20 random integers and I'll identify if it's an even or odd number."
instruction_center = instruction.center(150)
print(instruction_center)
print('\n' + Fore.YELLOW + "-___-"*30)
print(Style.RESET_ALL)

# open file numbers.txt(write)
with open("numbers.txt", 'w') as input_file:

    # create loop until we have 20 integers
    i = 0
    while (i < 2):
        # ask user for numbers
        random_numbers = input('\033[0;31m' + "\t\tPlease write a number: \033[0m")
        # put the numbers to numbers.txt
        input_file.write((random_numbers) + '\n')
        i += 1
        
print('\n' + Fore.YELLOW + "-"*150)
print('\nPROCESSING. Please wait...')
print("...")
time.sleep(4)

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

# output
# open files numbers.txt(read), even.txt(write), and odd.txt(write)
with open("numbers.txt") as numbers_file1, open("even.txt") as even_num1, open("odd.txt") as odd_num1:
    # read numbers.txt by line
    user_num1 = [int(line) for line in numbers_file1.read().split()]
    # show user the numbers they entered
    print(Fore.RED + "\n\n\tCHOSEN NUMBERS: " + Style.RESET_ALL, user_num1)
    time.sleep(1)

    # read even.txt by line
    num_even = [int(line) for line in even_num1.read().split()]
    # show user even numbers 
    print(Fore.RED + "\n\n\tEVEN NUMBERS: " + Style.RESET_ALL, num_even)
    time.sleep(1)

    # read odd.txt by line
    num_odd = [int(line) for line in odd_num1.read().split()]

# end of program