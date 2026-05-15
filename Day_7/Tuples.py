# Day 7 - Tuples
# Problem: Convert list into tuple and print hash value

if __name__ == '__main__':
    n = int(input())

    integer_list = map(int, input().split())

    t = tuple(integer_list)

    print(hash(t))
