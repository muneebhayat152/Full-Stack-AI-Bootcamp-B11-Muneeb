# Week 1 - Assignment 2: String Operations (Intermediate)

# Q1. Count vowels & consonants
text = "Hello, World! 123"
vowels = 0
consonants = 0
for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels, "Consonants:", consonants)

# Q2. Palindrome check (ignore case & punctuation)
text = "A man, a plan, a canal: Panama!"
clean_text = ""
for ch in text:
    if ch.isalnum():
        clean_text += ch.lower()
print(clean_text == clean_text[::-1])

# Q3. Manual title case (without .title())
sentence = "hELLO wORLD from PYTHON"
result_words = []
for word in sentence.split():
    result_words.append(word[0].upper() + word[1:].lower())
print(" ".join(result_words))

# Q4. Find all indices of a substring (overlaps allowed)
s = "aaaa"
sub = "aa"
indices = []
for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        indices.append(i)
print(indices)

# Q5. Character frequency dictionary
text = "Baa Baa Black Sheep"
freq = {}
for ch in text.lower():
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1
print(freq)

# Q6. Anagram checker
s1 = "Listen"
s2 = "Silent"
print(sorted(s1.lower()) == sorted(s2.lower()))

# Q7. Compress repeated characters (RLE)
text = "aaabbcaaaa"
compressed = ""
count = 1
for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        compressed += text[i - 1] + str(count)
        count = 1
compressed += text[-1] + str(count)
print(compressed)

# Q8. Longest word in a sentence
sentence = "Find the longest word here!"
longest_word = ""
for word in sentence.split():
    clean_word = word.strip(".,!?")
    if len(clean_word) > len(longest_word):
        longest_word = clean_word
print(longest_word)

# Q9. Remove duplicate characters, keep order
text = "banana"
seen = []
result = ""
for ch in text:
    if ch not in seen:
        seen.append(ch)
        result += ch
print(result)

# Q10. Mask email username
email = "muneebhayat152@gmail.com"
username, domain = email.split("@")
masked_username = username[0] + "*" * (len(username) - 2) + username[-1]
print(masked_username + "@" + domain)
