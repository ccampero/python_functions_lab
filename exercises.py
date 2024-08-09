# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.

def calculate_area_triangle(base, height):
    area = (base*height) / 2
    return area

print('Exercise 1:', calculate_area_triangle(10, 5))
print('Exercise 1:', calculate_area_triangle(7, 3) )

# Exercise 2: Calculate Simple Interest
#
# Write a function named `simple_interest` that takes principal, rate of interest (as a percentage), and time (years).
# Calculate and return the simple interest using the formula (principal * rate * time) / 100.
#
# Examples:
# simple_interest(1000, 5, 2) should return 100.
# simple_interest(1500, 3.5, 5) should return 262.5.
#
# Define your function and call it to see the result.

def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal*rate*time) / 100
    return simple_interest

print('Exercise 2:', calculate_simple_interest(1000, 5, 2))
print('Exercise 2:', calculate_simple_interest(1500, 3.5, 5))

# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.

def apply_discount(price, discount):
    discount = (price*discount) / 100
    new_price = price - discount
    return new_price

print('Exercise 3:', apply_discount(100, 25))
print('Exercise 3:', apply_discount(80, 10))

# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.

def convert_temperature(temp, unit):
    if unit == 'C':
        converted_temp = (temp * 9/5) + 32
    elif unit == 'F':
        converted_temp = (temp - 32) * 5/9
    return converted_temp

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
#
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.

def sum_to(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum


print('Exercise 5:', sum_to(6))
print('Exercise 5:', sum_to(10))


# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.

def largest(x, y, z):
    largest_number = x
    if y > largest_number:
        largest_number = y
    if z > largest_number:
        largest_number = z
    return largest_number

print('Exercise 6:', largest(1, 2, 3))
print('Exercise 6:', largest(25, 36, 574))

# Exercise 7: Calculate a Tip
#
# Create a function called `calculate_tip`. It should take the bill amount and the tip percentage (as a whole number).
# The function should return the amount of the tip.
#
# Examples:
# calculate_tip(50, 20) should return 10.
#
# Write your function and test its output below.

def calculate_tip(bill, tip):
    total_tip = (bill * tip) / 100
    return total_tip

print('Exercise 7:', calculate_tip(50, 20))
print('Exercise 7:', calculate_tip(150, 18))

# Exercise 8: Calculate Product of Numbers
#
# Write a function named `product` that takes an arbitrary number of numbers, multiplies them, and returns the product.
# Review your notes on *args for handling an arbitrary number of arguments.
#
# Examples:
# product(-1, 4) should return -4.
# product(2, 5, 5) should return 50.
#
# Define the function and call it with different sets of numbers to test.

def product(*args):
    product_result = 1
    for num in args: 
        product_result *= num
    return product_result


print('Exercise 8:', product(2, 5, 5))
print('Exercise 8:', product(7, 15, 25, 36, 52))


#Exercise 9: Basic Calculator


#Create a function named basicCalculator that takes three arguments:
# two numbers and a string representing an operation (‘add’, ‘subtract’, ‘multiply’, ‘divide’).
# Perform the provided operation on the two numbers. In operations where the order of numbers is important,
# treat the first parameter as the first operand and the second parameter as the second operand.


# Examples:
# basicCalculator(10, 5, ‘subtract’) should return 5.
# basicCalculator(10, 5, ‘add’) should return 15.
# basicCalculator(10, 5, ‘multiply’) should return 50.
# basicCalculator(10, 5, ‘divide’) should return 2.
# #

# Define the function and then call it below.

def basicCalculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return 'Error: Division by zero'
        return num1 / num2
    else:
        return 'Error: Invalid operation'
    

print('Exercise 9 Result:', basicCalculator(10, 5, 'subtract'))
print('Exercise 9 Result:', basicCalculator(3, 7, 'multiply'))
print('Exercise 9 Result:', basicCalculator(15, 9, 'add'))






