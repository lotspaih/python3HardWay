# Import argv from sys module
from sys import argv

# Assign argv CLI input to variables
script, filename = argv

# Open the file assigned to the filename variable and assign the input to the
# txt variable
txt = open(filename)

# Print static text with the txt variable text below it using the read method
print(f"Here's your file {filename}:")
print(txt.read())

# Closes the txt file
txt.close()

# Ask for user input for the filename to open next
print("Type the filename again:")
file_again = input("> ")

# Open the file input from the file_again variable and assign to txt_again
txt_again = open(file_again)

# Print the input from the txt_again variable
print(txt_again.read())

# Closes the txt_again file
txt_again.close()
