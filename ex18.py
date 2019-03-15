# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()


# Function Checklists
# FUNCTION SETUP
# 1. Start function with "def"
# 2. Function name only characters and "_" underscores
# 3. Open parenthesis after function name
# 4. Arguments inside parenthesis separated by commas
# 5. Each argument must be unique
# 6. Colon after the closing parenthesis
# 7. Indent 4 spaces all lines after function
# 8. End function by removing the line indents
#
# FUNCTION USAGE
# 1. Run/Call/Use function by calling its name
# 2. Put "(" character after the name to run it
# 3. Put values separated by commas
# 4. End function call with the ")" character
