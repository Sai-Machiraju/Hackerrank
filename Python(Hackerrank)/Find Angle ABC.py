import math
a,b=int(input()),int(input())
c= math.sqrt((a**2)+(b**2))
x=math.asin((a/c))*(180/math.pi)    
print(round(x),chr(176),sep="")
