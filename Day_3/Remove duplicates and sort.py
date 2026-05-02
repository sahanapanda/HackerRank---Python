#Remove duplicates and sort

l = list(map(int,input().split()))
s = set(l)
result = sorted(s)

print(result)

1 2 15 60 75 43 43 15 3
[1, 2, 3, 15, 43, 60, 75]

