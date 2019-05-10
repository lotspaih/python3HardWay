# Edited for function creation
def number_loop(max, incr):
    """Increments number list based on inputs"""
    i = 0
    numbers = []

    while i < max:
        print(f"At the top of i is {i}")
        numbers.append(i)

        i = i + incr
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

        print("The numbers: ")
        for num in numbers:
            print(num)


number_loop(8, 2)

# Written to use a for-loop instead of while-loop
i = 0
numbers = []

for i in range(0, 6):
    print(f"At the top of i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")
for num in numbers:
    print(num)
