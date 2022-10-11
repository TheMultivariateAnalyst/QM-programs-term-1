import math
x=2
n=int(input('no of terms:'))
for i in range(1,n+1):
    x=((1/2)*(x+(2/x)))
print(x)
print(math.sqrt(2))
