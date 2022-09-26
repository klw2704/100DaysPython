# PRIMITIVE DATA TYPES

# returns the amount of characters in a string, cant do it with int
print(len("Hello"))

#Strings = a string of characters, double quotes
# can pull out each character individually
print("Hello"[0])  # subscripting - to print a specific character
print("Hello"[-1]) # prints the last character
print("123" + "345") # will print 123345 as defined as a string

# Integers = whole numbers, no decimal places
int = 123 + 345 # will return 468, actually being calculated
123_456_789 # the underscores equate to commas to help read larger numbers

# float = floating point number
3.14 

# boolean = only true or false, must have capitals 
True
False


# TYPE ERROR, TYPE CHECKING AND TYPE CONVERSION
num_char = len(input("What is your name? ")) # user should enter their name
print("Your name has " + str(num_char) + " characters.") # string concatenation, will get an ERROR if you dont convert the int to str

# examples

a = 123 # should be integer
print(type(a))

a = str(123) # will be a string
print(type(a))

# MATHEMATICAL OPERATORS IN PYTHON
3 + 5 # addition
7 - 3 # subtraction
3 * 2 # multiplication
6 / 3 # division
6 // 3 # floor division, for no floating point
2 ** 2 # to the power of

# remember PEMDAS
# PARENTHESIS
# EXPONENTS
# MULTIPLICATION AND DIVISION
# ADDITION AND SUBTRACTION
# calculations that are most to the left will be prioritised 

# NUMBER MANIPULATION AND F-STRINGS IN PYTHON 
print(int(8 / 3)) # would chop off the decimal points without rounding
print(round(8 / 3)) # rounds into a whole number
print(round(8 / 3, 2)) # rounds to a specific number of decimal places

# you can continue performing calculations if you save them into a variable
result = 4 / 2
result /= 2 # divides the result variable by 2 again

+= 1 # adds 1 to a value / variable
/= 1 # divides a value / variable by 1

# F STRINGS
score = 0
height = 1.8
isWinning = True

f"Your score is {score}, your hieght is {height}, you are winning is {isWinning}."