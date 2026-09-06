# ==========================================================
# PART 1: COMPARISON OPERATORS
# These operators COMPARE two values and give an ANSWER that is
# always either True or False (this is called a BOOLEAN answer).
# ==========================================================

x = 10
y = 3

print(x == y)    # DOUBLE EQUALS -> "is equal to?"        -> False (10 is not equal to 3)
print(x != y)    # NOT EQUAL sign -> "is NOT equal to?"    -> True  (10 is indeed not equal to 3)
print(x > y)     # GREATER THAN sign                       -> True  (10 is bigger than 3)
print(x < y)     # LESS THAN sign                          -> False (10 is not smaller than 3)
print(x >= y)    # GREATER THAN OR EQUAL sign               -> True
print(x <= y)    # LESS THAN OR EQUAL sign                  -> False

# Important: "=" (one equals sign) STORES a value.
#            "==" (two equals signs) COMPARES two values.
#            These are two completely different symbols. Do not mix them up.


# ==========================================================
# PART 2: LOGICAL OPERATORS
# These operators JOIN two or more True/False answers together.
# ==========================================================

age = 20
has_id_card = True

# "and" -> the WHOLE answer is True only if BOTH sides are True
print(age >= 18 and has_id_card)     # True and True -> True

# "or" -> the WHOLE answer is True if AT LEAST ONE side is True
print(age >= 18 or has_id_card)      # True or True -> True

# "not" -> this FLIPS a True/False answer to its opposite
print(not has_id_card)               # has_id_card is True, so "not True" -> False


# ==========================================================
# PART 3: ASSIGNMENT OPERATORS (SHORTCUTS)
# These are shortcuts for "take my current value, change it, and
# save it back into the same variable name."
# ==========================================================

score = 10

score += 5    # SAME AS WRITING: score = score + 5   -> score becomes 15
print(score)

score -= 3    # SAME AS WRITING: score = score - 3   -> score becomes 12
print(score)

score *= 2    # SAME AS WRITING: score = score * 2   -> score becomes 24
print(score)

score //= 5   # SAME AS WRITING: score = score // 5  -> score becomes 4
print(score)


# ==========================================================
# NOW YOU WRITE THIS PART YOURSELF:
# ==========================================================

# Step 1: Make two variables: temperature = 40 and is_summer = True
# Print the result of checking: is temperature greater than 35 AND is_summer is True
temperature = 40
is_summer = True
print(temperature > 35 and is_summer)  

# Step 2: Make a variable called balance = 100
balance = 100
# Using the += shortcut, add 250 to balance, then print it
balance += 250
print(balance)  
# Using the -= shortcut, subtract 75 from balance, then print it
balance -= 75
print(balance) 