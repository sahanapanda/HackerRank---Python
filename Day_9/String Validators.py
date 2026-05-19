# Day 9 - String Validators
# Problem: Check different properties of characters in a string 

if __name__ == '__main__':
    s = input()

    print(any(char.isalnum() for char in s))

    print(any(char.isalpha() for char in s))

    print(any(char.isdigit() for char in s))

    print(any(char.islower() for char in s))

    print(any(char.isupper() for char in s))
