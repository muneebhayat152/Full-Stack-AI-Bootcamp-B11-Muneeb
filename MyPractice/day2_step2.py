# ==========================================================
# WHAT IS A TUPLE?
# A tuple is very similar to a list — it also holds multiple
# values in order. But a tuple is written with ROUND BRACKETS ( )
# instead of square brackets.
#
# THE BIG DIFFERENCE: A tuple is "IMMUTABLE" — this means
# once it is created, it CANNOT be changed. No adding, no
# removing, no replacing items.
# ==========================================================

colors = ("red", "green", "blue")

print(colors)          # prints the whole tuple
print(type(colors))    # <class 'tuple'>


# ==========================================================
# ACCESSING ITEMS (same as lists — indexing works the same way)
# ==========================================================

print(colors[0])     # first item  -> red
print(colors[-1])    # last item   -> blue


# ==========================================================
# TRYING TO CHANGE A TUPLE (this will cause an ERROR)
# We are writing this as a COMMENT so it doesn't crash the program.
# Uncomment it yourself later just to SEE the error message, then
# comment it back again.
# ==========================================================

# colors[0] = "yellow"   # This line would give: TypeError: 'tuple' object does not support item assignment


# ==========================================================
# WHY USE A TUPLE IF WE CAN'T CHANGE IT?
# We use tuples for data that should NEVER change while the
# program is running — for example, the days of the week,
# or fixed coordinates (x, y) of a point.
# ==========================================================

days = ("Monday", "Tuesday", "Wednesday")
coordinate = (10, 20)     # this represents a single point: x = 10, y = 20

print(days)
print(coordinate)


# ==========================================================
# LOOPING THROUGH A TUPLE (a quick preview — we'll cover loops properly next)
# "for" repeats a block of code once for each item in the tuple.
# ==========================================================

for day in days:
    print(day)


# ==========================================================
# TUPLE UNPACKING
# We can take a tuple and instantly split its values into
# separate variables, all in one line.
# ==========================================================

x, y = coordinate     # x becomes 10, y becomes 20
print(x)
print(y)


# ==========================================================
# NOW YOU WRITE THIS PART YOURSELF:
# ==========================================================

# Step 1: Make a tuple called weekend_days with the values "Saturday" and "Sunday"
weekend_days = ("Saturday", "Sunday")

# Step 2: Print the first item of weekend_days using indexing
print(weekend_days[0])

# Step 3: Use a "for" loop to print each item in weekend_days (copy the pattern shown above)
for day in weekend_days:
    print(day)

# Step 4: Make a tuple called student = ("Ali", 21, "Computer Science")
# Unpack it into 3 variables: student_name, student_age, student_field
# Then print all three
student = ("Ali", 21, "Computer Science")
student_name, student_age, student_field = student
print(student_name)
print(student_age)
print(student_field)