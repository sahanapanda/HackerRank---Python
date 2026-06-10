# Day 6 - Runner-Up Score
# Problem: Find the second highest number in a list

n = int(input())

arr = list(map(int, input().split()))

arr = list(set(arr))

arr.sort()
 
print(arr[-2])
