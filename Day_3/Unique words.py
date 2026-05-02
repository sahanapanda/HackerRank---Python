#Unique words (lowercase + no punctuation)

import string

text = input().lower()

for i in string.punctuation:
    text = text.replace(i, "")

words = text.split()

s = set(words)

print(s)
