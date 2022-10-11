from fractions import Fraction
import fractions
from tkinter import Y
x=Fraction(1, 2)
y=Fraction(51,100)
z=(x+y)/2
while z>x:
    z=z+(1/10000000)
    if z>y:
        break
    print(Fraction(z))

