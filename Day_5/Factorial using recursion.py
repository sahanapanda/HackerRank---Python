#Factorial using recursionfunction 
def factorial(n):
    if n < 0:
        return "Invalid"
    if n == 0:
        return 1
    return n * factorial(n - 1)
