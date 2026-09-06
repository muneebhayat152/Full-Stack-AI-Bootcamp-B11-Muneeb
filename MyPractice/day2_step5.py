# ==========================================================
# WHAT IS "if"?
# "if" lets the program CHECK a condition (True or False),
# and only run some code WHEN that condition is True.
#
# Notice the COLON ":" at the end of the if line, and the
# INDENTATION (spaces) before the line underneath it.
# The colon says "a block of code is about to start".
# The indentation says "this line BELONGS to the if above it".
# ==========================================================

marks = 85

if marks >= 40:
    print("You passed!")     # this line is INDENTED, so it belongs to "if"

print("Program continues...")   # this line is NOT indented, so it always runs


# ==========================================================
# if / else
# "else" runs ONLY when the "if" condition was False.
# ==========================================================

marks = 30

if marks >= 40:
    print("You passed!")
else:
    print("You failed!")


# ==========================================================
# if / elif / else
# "elif" means "else if" — it lets us check MULTIPLE conditions
# in order, one after another. Python checks them top to bottom
# and stops at the FIRST one that is True.
# ==========================================================

marks = 72

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: F")


# ==========================================================
# NESTED if (an if INSIDE another if)
# ==========================================================

age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Welcome to the movie!")
    else:
        print("Please buy a ticket first.")
else:
    print("Sorry, you must be 18 or older.")


# ==========================================================
# TERNARY EXPRESSION (a short one-line version of if/else)
# Format:  value_if_true if condition else value_if_false
# ==========================================================

marks = 55
result = "Pass" if marks >= 40 else "Fail"
print(result)


# ==========================================================
# NOW YOU WRITE THIS PART YOURSELF:
# ==========================================================

# Step 1: Make a variable temperature = 38
temperature = 38
if temperature > 37:
    print("You have a fever")
else:
    print("Your temperature is normal")


# Step 2: Make a variable number = 15
# Using if/elif/else, check and print:
#   "Positive" if number > 0
#   "Negative" if number < 0
#   "Zero" if number == 0
number = 15
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Step 3: Make a variable password = "abc123"
# Using a ternary expression, store "Strong" if len(password) >= 8,
# otherwise store "Weak", into a variable called strength
# Then print strength
password = "abc123"
strength = "Strong" if len(password) >= 8 else "Weak"
print(strength)