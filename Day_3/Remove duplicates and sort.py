#Remove duplicates and sort

l = list(map(int,input().split()))
s = set(l)
result = sorted(s)

print(result)

