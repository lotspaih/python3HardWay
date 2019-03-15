# Imports the argv module from sys
from sys import argv

# Breaks the argv variable into two variables assigned by order
script, input_file = argv


# Creates a function that receives the open file as input and prints it
def print_all(f):
    print(f.read())


# Creates a function that receives the open file and resets the file offset
# back to the beginning of the file
def rewind(f):
    f.seek(0)


# Create a function that receives the open file and an assigned variable with
# a line number to assign then reads that line and prints the line number and
# the line iteself
def print_a_line(line_count, f):
    print(line_count, f.readline())


# Assigns the cvariable to an open text file from the argv input variable
current_file = open(input_file)

# Prints the text
print("First let's print the whole file:\n")

# Runs the print_all function passing it the current_file variable
print_all(current_file)

# Prints the text
print("Now let's rewind, kind of like a tape.")

# Runs the rewind function passing it the current_file variable
rewind(current_file)

# Prints the text
print("Let's print three lines:")

# Assigns the variable current_file the numeric value of 1
current_line = 1
# Runs the print_a_line function passing it the current_line variable and
# the current oprn file text
print_a_line(current_line, current_file)

# Assigns the variable current_file the numeric value of itself plus itself
current_line += current_line
# Runs the print_a_line function passing it the current_line variable and
# the current oprn file text
print_a_line(current_line, current_file)

# Assigns the variable current_file the numeric value of itself plus 1
current_line += 1
# Runs the print_a_line function passing it the current_line variable and
# the current oprn file text
print_a_line(current_line, current_file)
