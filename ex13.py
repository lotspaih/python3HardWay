# Imports argv from the sys module
from sys import argv

# Below assigns the argv CLI input into three variables
script, first, second, third = argv

# Get name input from user and assign to name variables
name = input("What is your name? ")

# Print the three argv variables and the single input variable
print("The script is called:", script)
print("The first variable is:", first)
print("The second variable is:", second)
print("The third variable is:", third)
print("Your name is: ", name)
