from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# One line option from above?
# in_file = open(from_file).read()
# Change indata variable below to in_file and remove in_file close statment

# To make this script more friendly, remove all lines below up to and including
# the input() line:
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
# Stop removing here for friendly version

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

# My super short version looks like this:
# from sys import argv

# script, from_file, to_file = argv

# with open(from_file) as in_file:
#     data = in_file.read()
#     open(to_file, 'w').write(data)
