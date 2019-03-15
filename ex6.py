# Assign variable types_of_people the number 10 and then add that variable
# to the x variable inside the formated string using {}.
types_of_people = 10
x = f"There are {types_of_people} types of people"

# Assign variable binary and do_not strings and then add those variables
# to the y variable inside the formated string using {}.
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Print the x then y variables
print(x)
print(y)

# Print the strings with the x and y variables formated inside the strings
# using {}.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Assign the varible hilarious equal to boolean False and a formatted string to
# the variable joke_evaluation.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Print the joke_evaluation variable with the varible hilarious formated
# into the end of the string where the {} occur.
print(joke_evaluation.format(hilarious))

# Assign strings to variables w and e
w = "This is the left side of..."
e = "a string with a right side."

# Print the two variables of strings w and e by joining them together with
# the '+' symbol as one string.
print(w + e)
