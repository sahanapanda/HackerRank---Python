#Missing Alphabets
import string

text = input()
s = set(text)

all_letters = set(string.ascii_lowercase + string.ascii_uppercase)
missing = all_letters - s

print("Missing letters :", missing)
