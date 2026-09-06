# ==========================================================
# WHAT IS A DICTIONARY?
# A list stores values in order, found by position (index number).
# A DICTIONARY stores values found by a NAME instead of a position.
# Each name is called a KEY, and what it points to is called a VALUE.
# Together, one "name: value" pair is called a KEY-VALUE PAIR.
#
# A dictionary is written with CURLY BRACES { }, and each
# key-value pair is written as   key : value
# (this is why {} alone means an empty DICTIONARY, not a set)
# ==========================================================

student = {
    "name": "Muneeb",
    "age": 22,
    "course": "Full Stack AI"
}

print(student)          # prints the whole dictionary
print(type(student))    # <class 'dict'>


# ==========================================================
# ACCESSING A VALUE
# Instead of an index number, we use SQUARE BRACKETS with the KEY NAME.
# ==========================================================

print(student["name"])     # Muneeb
print(student["age"])      # 22


# ==========================================================
# ADDING OR CHANGING A VALUE
# If the key already exists, this CHANGES its value.
# If the key does NOT exist yet, this CREATES a new key-value pair.
# ==========================================================

student["age"] = 23              # CHANGES the existing "age" key
student["city"] = "Lahore"       # CREATES a brand new "city" key
print(student)


# ==========================================================
# DELETING A KEY
# ==========================================================

del student["city"]     # del removes a key-value pair completely
print(student)


# ==========================================================
# GETTING ALL KEYS, ALL VALUES, OR ALL PAIRS
# ==========================================================

print(student.keys())      # gives all the KEY names
print(student.values())    # gives all the VALUES
print(student.items())     # gives all the KEY-VALUE pairs together


# ==========================================================
# LOOPING THROUGH A DICTIONARY
# ==========================================================

for key, value in student.items():
    print(key, "->", value)


# ==========================================================
# SAFE ACCESS WITH .get()
# Using student["xyz"] crashes the program if "xyz" doesn't exist.
# .get() is SAFER — it returns None (or a default we choose)
# instead of crashing.
# ==========================================================

print(student.get("email"))              # key doesn't exist -> prints None (no crash)
print(student.get("email", "Not Found")) # key doesn't exist -> prints our own default text


# ==========================================================
# NOW YOU WRITE THIS PART YOURSELF:
# ==========================================================

# Step 1: Make a dictionary called book with keys: "title", "author", "pages"
# and fill them with any real book's details
book = {
    "title": "1984",
    "author": "George Orwell",
    "pages": 328
}

# Step 2: Print only the "author" value
print(book["author"])


# Step 3: Add a new key "price" with any number value
book["price"] = 19.99

# Step 4: Use a for loop to print every key and value in book (copy the pattern shown above)
for key, value in book.items():
    print(key, "->", value)

# Step 5: Use .get() to safely check for a key called "publisher" that does NOT exist,
# and give it the default value "Unknown"
print(book.get("publisher", "Unknown"))
