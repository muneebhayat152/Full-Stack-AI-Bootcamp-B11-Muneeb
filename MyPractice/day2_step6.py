# ==========================================================
# WHILE LOOP
# "while" keeps repeating a block of code AS LONG AS a condition
# stays True. It stops the moment the condition becomes False.
#
# WARNING: if the condition NEVER becomes False, the loop will
# run FOREVER. This is called an "infinite loop" — always make
# sure something inside the loop eventually makes it False.
# ==========================================================

count = 1

while count <= 5:
    print(count)
    count += 1     # THIS LINE IS IMPORTANT: it changes count, so eventually count <= 5 becomes False

print("while loop finished")


# ==========================================================
# FOR LOOP with range()
# "for" repeats a block of code ONCE for each value in a sequence.
# range(5) creates the sequence: 0, 1, 2, 3, 4 (starts at 0,
# stops BEFORE 5, just like slicing does)
# ==========================================================

for i in range(5):
    print(i)

print("for loop with range finished")

# range(start, stop) -> lets us choose our own starting number
for i in range(2, 6):
    print(i)          # prints: 2, 3, 4, 5


# ==========================================================
# FOR LOOP over a LIST
# ==========================================================

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# ==========================================================
# BREAK
# "break" immediately STOPS the loop completely, even if the
# condition was still True.
# ==========================================================

for number in range(1, 10):
    if number == 5:
        break         # as soon as number becomes 5, the loop stops entirely
    print(number)


# ==========================================================
# CONTINUE
# "continue" SKIPS just the current round of the loop, then
# moves on to the NEXT round (it does NOT stop the whole loop).
# ==========================================================

for number in range(1, 6):
    if number == 3:
        continue      # when number is 3, this round is skipped, but the loop keeps going
    print(number)


# ==========================================================
# PASS
# "pass" does absolutely NOTHING. It is used as a placeholder
# when Python requires some code to be written, but we don't
# want to do anything there yet.
# ==========================================================

for number in range(1, 4):
    if number == 2:
        pass          # placeholder — nothing happens here, code just moves on
    print(number)


# ==========================================================
# NESTED LOOPS (a loop inside another loop)
# ==========================================================

for row in range(1, 3):
    for col in range(1, 3):
        print("row", row, "col", col)


# ==========================================================
# NOW YOU WRITE THIS PART YOURSELF:
# ==========================================================

# Step 1: Use a "for" loop with range() to print all numbers from 1 to 10
for i in range(1, 11):
    print(i)

# Step 2: Use a "for" loop to print only the EVEN numbers from 1 to 20
# (Hint: use the % operator you learned earlier — a number is even if number % 2 == 0)
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# Step 3: Use a "while" loop that starts at 10 and counts DOWN to 1
# (print each number)
i = 10
while i >= 1:
    print(i)
    i -= 1  # decrement i by 1 each time

# Step 4: Use a "for" loop over range(1, 20) that uses "break" to 
# stop as soon as it reaches a number greater than 7
for i in range(1, 20):
    if i > 7:
        break
    print(i)