#Identify vowels and consonants in a string

text = input()
s = set(text)

vowels = set()
consonants = set()

for i in s:
    if i in 'AEIOUaeiou':
        vowels.add(i)
        
    else:
        consonants.add(i)
        
print("vowels : ", vowels)
print("consonants : ", consonants)

sahana
vowels :  {'a'}
consonants :  {'s', 'n', 'h'}
