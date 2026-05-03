#Student marks and display average, maximum, and minimum values

def avg(l):
    avg = sum(l)/len(l)
    return avg
    
l=list(map(int,input().split()))
print(avg(l))
print(max(l))
print(min(l))
