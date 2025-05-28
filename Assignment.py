# question 1

# Taking two numbers as input from the user
num1 = int(input("Enter the first number (dividend):"))
num2 = int(input("Enter the second number (divisor, not 0): "))

# Calculating the remainder
remainder = num1 % num2

print("The remainder when", num1, "is divided by ", num2, " is: " , remainder)

# question 2

# Taking the number input from a user
num = float(input("Enter any number here:"))

# if the number is greater >, < +, == 10
is_greater = num > 10
is_less = num < 10
is_equal = num == 10

print("The number is greater than 10:", is_greater)
print("The number is less than 10:", is_less)
print("The number is equal to 10:", is_equal)


# question 3

# Taking a number as input from the user
number = float(input("Enter a number: "))

# Checking if the number is between 1 and 100 using the 'and' operator
is_in_range = number >= 1 and number <= 100

print(f"Is the number between 1 and 100? {is_in_range}")

# question 4

# Taking a number as input from the user
number = float(input("Enter a number: "))

# Checking if the number is not negative using the 'not' operator
is_not_negative = not (number < 0)

print("Is the number not negative?", is_not_negative)

# question 5

# Taking a number as input from the user
number = float(input("Enter a number: "))

# Increasing the number by 5 using the += operator
number += 5

# Multiplying the number by 2 using the *= operator
number *= 2

print("The final result is:", number)

