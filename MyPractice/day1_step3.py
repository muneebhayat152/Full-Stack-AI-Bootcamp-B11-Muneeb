# ==========================================================
# PART 1: TYPE CASTING
# "Type Casting" means: changing one data type into another data type.
# For example: changing text ("25") into a real number (25).
# ==========================================================

# Imagine this text came from a user typing on the keyboard.
# Even though it LOOKS like a number, Python sees it as a STRING (text).
user_input_text = "25"

print(type(user_input_text))   # This will show: <class 'str'>  (still text!)

# int() is a function that converts something INTO an integer (whole number).
user_input_number = int(user_input_text)

print(type(user_input_number))  # This will show: <class 'int'>  (now a real number!)

# Now that it is a real number, we can do math with it.
print(user_input_number + 5)    # This works: 25 + 5 = 30

# str() is a function that converts something INTO a string (text).
number_value = 100
number_as_text = str(number_value)
print(type(number_as_text))     # This will show: <class 'str'>

# float() is a function that converts something INTO a decimal number.
whole_number = 7
decimal_version = float(whole_number)
print(decimal_version)          # This will show: 7.0


# ==========================================================
# PART 2: ARITHMETIC OPERATORS
# These are the symbols Python uses to do math, like a calculator.
# ==========================================================

a = 10
b = 3

print(a + b)     # PLUS sign        -> addition           -> 13
print(a - b)     # MINUS sign       -> subtraction        -> 7
print(a * b)     # ASTERISK sign    -> multiplication     -> 30
print(a / b)     # FORWARD SLASH    -> division (gives decimal answer) -> 3.333...
print(a // b)    # DOUBLE SLASH     -> "floor division" (division, answer ROUNDED DOWN, no decimal) -> 3
print(a % b)     # PERCENT sign     -> "modulus" (gives the LEFTOVER/remainder after division) -> 1
print(a ** b)    # DOUBLE ASTERISK  -> "exponent" (power) -> 10 to the power of 3 -> 1000


# ==========================================================
# NOW YOU WRITE THIS PART YOURSELF:
# ==========================================================

# Step 1: Make a variable called price_text with the value "450" (as a string, with quotes)

price_text = "450"  # STRING: text data, always written inside quotes " "
# Step 2: Convert price_text into a real number using int(), and store it in price_number
price_number = int(price_text) 

# Step 3: Add 50 to price_number and print the result
print(price_number + 50)
# Step 4: Make two variables: num1 = 17 and num2 = 5
num1 = 17
num2 = 5
# Print the result of num1 divided by num2 using normal division (/)
print(num1 / num2)
# Then print the result of num1 divided by num2 using floor division (//)
print(num1 // num2)
# Then print the remainder using modulus (%)
print(num1 % num2)