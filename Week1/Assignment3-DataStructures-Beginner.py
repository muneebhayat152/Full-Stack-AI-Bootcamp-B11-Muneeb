# Week 1 - Assignment 3: Data Structures (Beginner)

# ---------- Part A: Lists ----------

# A1
nums = [3, 1, 4, 1, 5]
print(nums[0])
print(nums[-1])

# A2
colors = ["red", "blue", "green"]
print(len(colors))

# A3
colors = ["red", "blue"]
colors.append("yellow")
print(colors)

# A4
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)

# A5
fruits = ["apple", "banana", "grapes"]
fruits.remove("banana")
print(fruits)

# A6
items = [10, 20, 30]
popped_value = items.pop()
print(popped_value)
print(items)

# A7
nums = [1, 2, 3, 4]
print(3 in nums)

# A8
nums = [0, 1, 2, 3, 4]
print(nums[2:4])

# A9
a = [5, 10, 15]
a[1] = 12
print(a)

# A10
nums = [1, 2, 2, 3, 2]
print(nums.count(2))

# ---------- Part B: Tuples ----------

# B1
t = (10, 20, 30)
print(t[1])

# B2
t = ('a', 'b', 'c')
print(len(t))

# B3
x, y = (4, 5)
print(x, y)

# B4
t = ('a', 'b', 'c')
print('b' in t)

# B5
t = ()
print(type(t))

# B6
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)

# B7
t = (7,)
print(t * 3)

# B8
t = (1, 2, 3, 2)
print(t.index(2))

# B9
print(t.count(2))

# B10
single_element_tuple = (5,)
print(single_element_tuple)
print(type(single_element_tuple))

# ---------- Part C: Sets ----------

# C1
s = set([1, 2, 2, 3])
print(s)

# C2
s = {1, 2, 3}
s.add(4)
print(s)

# C3
s = {1, 2, 3}
s.remove(2)
print(s)

# C4
s = {1, 3, 5}
print(5 in s)

# C5
s = {10, 20, 30}
print(len(s))

# C6
s = {1, 2, 3}
s.clear()
print(s)

# C7
letters = {"a", "b"}
if "c" not in letters:
    letters.add("c")
print(letters)

# C8
letters = set(['a', 'a', 'b'])
print(letters)

# C9
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)

# C10
print(set1 & set2)

# ---------- Part D: Dictionaries ----------

# D1
person = {"name": "Ali", "age": 25}
print(person["name"])

# D2
person["city"] = "Lahore"
print(person)

# D3
person["age"] = 30
print(person)

# D4
del person["age"]
print(person)

# D5
print("salary" in person)

# D6
print(list(person.keys()))

# D7
print(list(person.values()))

# D8
for key, value in person.items():
    print(key, value)

# D9
empty_dict = {}
print(empty_dict.get("score", 0))

# D10
keys = ['a', 'b']
values = [1, 2]
print(dict(zip(keys, values)))
