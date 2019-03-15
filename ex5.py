name = 'Zed A, Shaw'
age = 35  # Not a lie
height = 74  # inches
# Convert inches to centimeters by multiplying the inches by 2.54
# 1 inch = 2.54 centimeters
height_centimeters = height * 2.54  # height in centimeters
weight = 180  # lbs
# Convert lbs to kilograms by multiplying lbs by 0.45
# 1 kg = 2.2 lbs
weight_kilograms = weight * 0.45  # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f'Let us talk about {name}.')
print(f"He's {height} inches tall or {height_centimeters} centimeters tall.")
print(f"He's {weight} pounds or {weight_kilograms} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
