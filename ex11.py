print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# Python's input function waits for data to be entered and then processes it
# as determined by the program (e.g. assigns it to a variable)

# Another form and way to use the input function
name = input("What is your name? ")
surname = input("What is your surname? ")

print("Hello, {} {}, and welcome to Python!".format(name, surname))
