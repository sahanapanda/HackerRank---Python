# Day 9 - Count Substring
# Problem: Count occurrences of a substring in a string

def count_substring(string, sub_string):
    count = 0

    sub_len = len(sub_string)

    for i in range(0, len(string) - sub_len + 1):
        if string[i:i + sub_len] == sub_string:
            count += 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)

    print(count)
