# Define cheese_and_crackers function taking variables input and printing the
# lines below using those same variables


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")


# My Own Function With Several Calls


def breakfast_order(item1, item2, item3):
    print(f"You ordered: {item1}, {item2}, and {item3} for breakfast.")


# Print the line and call the cheese_and_crackers function with the variables
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Print the line and call the cheese_and_crackers function with the variables
# assigned below
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Print the line and call the cheese_and_crackers function with the math
# variables assigned below
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Print the line and call the cheese_and_crackers function with the assigned
# and math variables below
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Here I call my own function several times
breakfast_order("spam", "eggs", "ham")

order_item1 = "eggs"
order_item2 = "spam"
order_item3 = "spam"
breakfast_order(order_item1, order_item2, order_item3)

breakfast_order(order_item1, f"ham, {order_item1}", order_item2)

breakfast_order(order_item3, order_item1 + ", bacon", order_item3)

print("What three items would you like for breakfast?")
order_item1 = input("Item 1: ")
order_item2 = input("Item 2: ")
order_item3 = input("Item 3: ")
breakfast_order(order_item1, order_item2, order_item3)
