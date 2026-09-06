# ==========================================================
# WHAT IS A SET?
# A set is a collection that automatically removes DUPLICATE
# values, and does NOT keep any fixed order.
#
# A set is written using CURLY BRACES { } (NOT square or round brackets).
# ==========================================================

numbers = {1, 2, 3, 3, 2, 1, 4}

print(numbers)          # notice: duplicates are automatically removed!
print(type(numbers))    # <class 'set'>


# ==========================================================
# IMPORTANT TRAP: EMPTY SET
# You might think {} creates an empty set, but it does NOT.
# {} actually creates an empty DICTIONARY (we'll learn dictionaries next).
# To create a truly empty set, you MUST use the set() function.
# ==========================================================

empty_set = set()
print(type(empty_set))   # <class 'set'>


# ==========================================================
# ADDING AND REMOVING ITEMS
# ==========================================================

fruits_set = {"apple", "banana"}

fruits_set.add("mango")           # add() puts ONE new item into the set
print(fruits_set)

fruits_set.update(["kiwi", "grapes"])   # update() adds MULTIPLE items at once (from a list)
print(fruits_set)

fruits_set.discard("banana")      # discard() removes an item (no error even if it doesn't exist)
print(fruits_set)


# ==========================================================
# SET OPERATIONS (like in Mathematics)
# These are very useful for comparing two groups of data.
# ==========================================================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a | set_b)    # UNION: combines both sets, no duplicates      -> {1,2,3,4,5,6}
print(set_a & set_b)    # INTERSECTION: only items in BOTH sets         -> {3,4}
print(set_a - set_b)    # DIFFERENCE: items in set_a that are NOT in set_b -> {1,2}


# ==========================================================
# NOW YOU WRITE THIS PART YOURSELF:
# ==========================================================

# Step 1: Make a set called my_hobbies with 4 hobbies, but repeat one hobby TWICE
# (write the same hobby name twice on purpose)
# Print it, and see for yourself that the duplicate disappears
my_hobbies = {"reading", "swimming", "cooking", "swimming"}
print(my_hobbies)

# Step 2: Add one more hobby to my_hobbies using add()
my_hobbies.add("dancing")
print(my_hobbies)

# Step 3: Make two more sets:
# weekday_classes = {"Math", "Science", "English"}
# weekend_classes = {"Science", "Art"}
# Print the INTERSECTION of weekday_classes and weekend_classes
# (this shows which subject appears on both days)
weekday_classes = {"Math", "Science", "English"}
weekend_classes = {"Science", "Art"}
print(weekday_classes & weekend_classes)    