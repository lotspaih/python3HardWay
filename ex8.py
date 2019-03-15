# Define formatter variable
formatter = "{} {} {} {}"

# Using the format function, send the listed 4 variables to the formatter
# variable replacing the {} with the listed variable in order then print
# the formatter variable with the listed variables.
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# In the single line below instead of replacing the {} with listed variables it
# prints the formatter variable itself four times keeping the {}
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
      "Try your",
      "Own text here",
      "Maybe a poem",
      "Or a song about fear"
      ))
