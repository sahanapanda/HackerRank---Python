#Bonus Calculation + Final Salary

def c(s,r):
    if r==5:
        bonus = s*0.20
    elif r==4:
        bonus = s*0.10
    elif r==3:
        bonus = s*0.05
    elif r==1 or r == 2:
        bonus = 0
    else:
        print("Invalid rating")
        
    final = s+bonus
    print(bonus)
    print(final)
    
s = int(input())
r = int(input())
c(s,r)
