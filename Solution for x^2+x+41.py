import cmath
import numpy as np
count = 0
x=int(input('enter x value '))
y=x*x+x+41
print(y)

if y > 1:

    for i in range(2,y):
        if (y % i) == 0:
            print(y,"is not a prime number")
            print(i,"times",y//i,"is",y)
            if (y % i)!=0:
               break
        

    else:
        print(y,"is not  a prime number")