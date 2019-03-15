# Assign strings with escape sequences to variables
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# Added additional escape sequences and format strings
fishy = "Fishies"
fat_cat = '''
I'll do a list:
\t\b\b\b* Cat Food
\t\b\b* {}
\t\b* Catnip\n\t* Grass
'''.format(fishy)

# Print the various variables to see their formating with escape sequences
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
