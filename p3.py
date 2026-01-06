x=input()
new=""
for i in x:
    if i.isupper():
        new+=i.lower()
    elif i.islower():
        new+=i.upper()
    else:
        new+=i
print(new)