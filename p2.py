x = input()
for i in range(len(x)):
    if x[i].isupper():
        print(x[i].lower(),end="")
    elif x[i].islower():
        print(x[i].upper(),end="")