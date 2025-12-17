import math
import sys

x=sys.stdin.read().split()
if x:
    t=int(x[0])

    for i in range(1,t+1):
        z=x[i]
        if z==0:
            print("Yes")
            continue
        total=sum(math.factorial(int(c)) for c in z)
        
        if total==int(z):
            print("Yes")
        else:
            print("No")