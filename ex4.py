# Assigns the number 100 to the variable name 'cars'
cars = 100
# Assigns the floating point number 4.0 to the variable name 'space_in_a_car'
space_in_a_car = 4.0
# Assigns the number 30 to the variable name 'drivers'
drivers = 30
# Assigns the number 90 to the variable name 'passengers'
passengers = 90
# Subtracts the 'cars' variable from the 'drivers' variable and assigns the
#    result to the 'cars_not_driven' variable
cars_not_driven = cars - drivers
# Assigns the 'drivers' variable to a new variable name 'cars_driven'
cars_driven = drivers
# Multiplies the 'cars_driven' variable by the 'space_in_a_car' variable and
#    assigns it to the 'carpool_capacity' variable
carpool_capacity = cars_driven * space_in_a_car
# Divides the 'passengers' variable by the 'cars_not_driven' variable and
#    assigns it to the 'average_passengers_per_car' variable
average_passengers_per_car = passengers / cars_not_driven

# Prints the given variable previously assigned within the given text
print('There are', cars, 'cars available.')
print('There are only', drivers, 'drivers available.')
print('There will be', cars_not_driven, 'empty cars today.')
print('We can transport', carpool_capacity, 'people today.')
print('We have', passengers, 'to carpool today.')
print('We need to put about', average_passengers_per_car, 'in each car.')
