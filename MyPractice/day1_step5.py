# ==========================================================
# PART 1: STRING INDEXING
# Every letter inside a string has a POSITION NUMBER, called an INDEX.
# Counting in Python ALWAYS starts from 0, not from 1.
# ==========================================================

word = "Python"

#        P  y  t  h  o  n
# index: 0  1  2  3  4  5   <- counting from the LEFT, starts at 0
# index:-6 -5 -4 -3 -2 -1   <- counting from the RIGHT, starts at -1

# Square brackets [ ] after a variable are used to PICK OUT one letter
# by giving its index number.

print(word[0])     # First letter   -> P
print(word[2])     # Third letter   -> t
print(word[-1])    # LAST letter (negative index counts from the end) -> n
print(word[-2])    # Second-last letter -> o


# ==========================================================
# PART 2: STRING SLICING
# Slicing means: cutting out a PIECE (a range of letters) from a string.
# The format is:  word[start : stop]
# It gives everything FROM "start" UP TO (but NOT including) "stop".
# ==========================================================

print(word[0:2])    # letters at index 0 and 1 (stops before index 2) -> Py
print(word[2:6])    # letters at index 2,3,4,5                        -> thon
print(word[:3])     # nothing before ":" means "start from the beginning" -> Pyt
print(word[3:])     # nothing after ":" means "go all the way to the end" -> hon
print(word[::-1])   # this special trick REVERSES the whole string        -> nohtyP


# ==========================================================
# PART 3: STRING METHODS
# A "method" is a function that belongs to a specific data type.
# We call a string method by writing: variable.method_name()
# The DOT "." connects the variable to the method.
# ==========================================================

sentence = "  Hello Python World  "

print(sentence.upper())       # changes every letter to CAPITAL letters
print(sentence.lower())       # changes every letter to small letters
print(sentence.strip())       # removes extra spaces from the start and end
print(sentence.replace("Python", "AI"))   # swaps one piece of text for another
print(len(sentence))          # len() is a function (not a method) that counts
                               # how many characters (including spaces) are in the string


# ==========================================================
# PART 4: input()
# input() is a function that PAUSES the program and waits for the
# user to type something on the keyboard, then press Enter.
# Whatever the user types is always received as a STRING.
# ==========================================================

user_name = input("What is your name? ")   # the text inside () is just a question shown on screen
print("Nice to meet you, " + user_name)     # "+" here JOINS two strings together (this is called concatenation)


# ==========================================================
# NOW YOU WRITE THIS PART YOURSELF:
# ==========================================================

# Step 1: Make a variable city = "Islamabad"
city = "Islamabad"
# Print only the first 3 letters of city using slicing
print(city[0:3])

# Step 2: Print the city name in all UPPERCASE letters
print(city.upper())

# Step 3: Ask the user for their favorite color using input(), store it in fav_color
# Then print a sentence like: "Your favorite color is <whatever they typed>" 
fav_color = input("What is your favorite color? ")     
print("Your favorite color is " + fav_color)    