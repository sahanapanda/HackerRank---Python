# Day 8 - Split and Join
# Problem: Replace spaces in a string with hyphens

def split_and_join(line):
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
