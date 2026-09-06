# ==========================================================
# In this file we will learn: what is a VARIABLE.
#
# A VARIABLE is like a labeled box where we can store
# a piece of data and use it again later.
# ==========================================================

# Look at the line below:
#   name = "Muneeb"
#
# "name"    -> this is the NAME of our variable (we choose this name ourselves)
# "="       -> this is called the EQUALS SIGN, also known as the
#              ASSIGNMENT OPERATOR.
#              It means: "take the value on the RIGHT side of =
#              and STORE it inside the name on the LEFT side of ="
# "Muneeb"  -> this is the VALUE we are storing. It is inside quotes,
#              so it is a STRING (text)

name = "Muneeb"        # STRING: text data, always written inside quotes " "

age = 22                # INTEGER (short form: "int"): a whole number, no decimal point

height = 6.0             # FLOAT: a number with a decimal point

is_student = True        # BOOLEAN (short form: "bool"): only 2 possible values -> True or False
                          # (it shows whether something is "true" or "false")

# ----------------------------------------------------------
# Now we will print() all these variables on the screen.
# This time there are NO quotes inside print(), because we are
# not printing plain text — we are printing the VALUE stored
# inside each variable.
# ----------------------------------------------------------

print(name)
print(age)
print(height)
print(is_student)

# ----------------------------------------------------------
# type() is also a function (just like print() was a function).
# Its job is: tell us the DATA TYPE (the kind) of whatever
# is written inside its brackets.
# ----------------------------------------------------------

print(type(name))         # <class 'str'>   -> str means STRING
print(type(age))          # <class 'int'>   -> int means INTEGER
print(type(height))       # <class 'float'> -> float means FLOAT (decimal number)
print(type(is_student))   # <class 'bool'>  -> bool means BOOLEAN


# ==========================================================
# NOW YOU WRITE THIS PART YOURSELF (using what you just learned):
# ==========================================================

# Step 1: Store your name in a variable called my_name (string, use quotes)

my_name = "Muneeb Ur Rehman"
# Step 2: Store your age in a variable called my_age (integer, no quotes)

my_age = 22
# Step 3: Store your favorite subject in a variable called fav_subject (string)
fav_subject = "Islamic Studies"

# Step 4: Print all three variables using print()
print(my_name)
print(my_age)
print(fav_subject)