#Format a username by converting to lowercase and removing spaces

def user(u):
    u = u.lower()
    u = u.replace(" ","")
    print(u)
u = input()
user(u)
