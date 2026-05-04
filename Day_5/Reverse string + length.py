#Reverse string + length
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]

def length(s):
    if s == "":
        return 0
    return 1 + length(s[1:])

print(reverse_string("hello"))
print(length("hello"))
