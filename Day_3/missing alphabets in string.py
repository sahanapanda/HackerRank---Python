#Missing Alphabets
import string

text = input()
s = set(text)

all_letters = set(string.ascii_lowercase + string.ascii_uppercase)
missing = all_letters - s

print("missing :", missing)

abcdefghijklmnopqrstuvwABCDEFGHIJKLMNOPQRSTUVW
missing : {'Y', 'Z', 'z', 'X', 'x', 'y'}
