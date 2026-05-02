#Unique words (lowercase + no punctuation)

import string

text = input().lower()

for i in string.punctuation:
    text = text.replace(i, "")

words = text.split()

s = set(words)

print(s)

sahana, is very fa.t
{'fat', 'very', 'sahana', 'is'}
