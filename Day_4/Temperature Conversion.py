#Temperature Conversion

def c_f(c):
    c = (c*9/5)+32
    return c
def f_c(f):
    f = (f - 32)*5/9
    return f 
    
choice = input("c or f ").lower()

if choice == 'c':
    c = float(input())
    print(c_f(c))
elif choice == 'f':
    f = float(input())
    print(f_c(f))

