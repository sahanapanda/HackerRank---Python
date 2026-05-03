#Password Strength Checker

def c_p(p):
    if len(p) < 8:
        print("weak")
        return
    u = 0
    l = 0
    d = 0
    
    for i in p:
        if i.isupper():
            u = 1
            
        if i.islower():
            l = 1
            
        if i.isdigit():
            d=1
    if u == 1 and l == 1 and d == 1:
        print("Strong")
    else:
        print("weak")
            
p = input()
c_p(p)

