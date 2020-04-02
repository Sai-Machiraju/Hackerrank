import numpy as np
x,y=map(int,input().split())
l1=[]
l2=[]
for i in range(x):
    s=input()
    l=[int(i) for i in s if i!=" "]
    l1.append(l)
for i in range(x):    
    p=input()
    l=[int(i) for i in p if i!=" "]
    l2.append(l)
a=np.array(l1)
b=np.array(l2)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)



