# ==========================================================
# WHAT IS A LIST?
# So far, one variable could hold only ONE value (like age = 25).
# A LIST lets ONE variable hold MANY values together, in a specific order.
#
# A list is written using SQUARE BRACKETS [ ], with each value
# separated by a COMMA ",".
# ==========================================================

fruits = ["apple", "banana", "mango", "orange"]

print(fruits)          # prints the whole list at once
print(type(fruits))    # <class 'list'>

# A list can also hold DIFFERENT data types mixed together
mixed_list = ["Muneeb", 22, 5.9, True]
print(mixed_list)


# ==========================================================
# ACCESSING ITEMS (INDEXING)
# Just like strings, list items have index numbers starting from 0.
# ==========================================================

print(fruits[0])     # first item -> apple
print(fruits[2])     # third item -> mango
print(fruits[-1])    # last item  -> orange


# ==========================================================
# CHANGING AN ITEM
# Unlike strings, lists are "MUTABLE" — this means we CAN change
# their items after creating them.
# ==========================================================

fruits[1] = "grapes"      # replaces "banana" with "grapes"
print(fruits)


# ==========================================================
# ADDING ITEMS
# ==========================================================

fruits.append("kiwi")            # append() adds ONE item to the END of the list
print(fruits)

fruits.insert(1, "strawberry")   # insert(position, item) adds an item at a SPECIFIC position
print(fruits)


# ==========================================================
# REMOVING ITEMS
# ==========================================================

fruits.remove("mango")   # remove() deletes a specific item BY ITS VALUE (name)
print(fruits)

last_item = fruits.pop()  # pop() removes and RETURNS the LAST item (also gives it back to us)
print(last_item)
print(fruits)


# ==========================================================
# USEFUL LIST INFO
# ==========================================================

print(len(fruits))              # len() also works on lists -> counts how many items
print("grapes" in fruits)       # "in" checks if an item exists in the list -> True/False


# ==========================================================
# NOW YOU WRITE THIS PART YOURSELF:
# ==========================================================

# Step 1: Make a list called subjects with 4 of your actual subjects (as strings)
subjects = ["Math", "Science", "English", "History"]

# Step 2: Print the 2nd subject in the list (using indexing)
print(subjects[1])

# Step 3: Add a new subject to the END of the list using append()
subjects.append("Art")

# Step 4: Remove any one subject using remove()
subjects.remove("Science")

# Step 5: Print the final list, and print how many subjects are left using len()
print(subjects)
print(len(subjects))    