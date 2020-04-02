import numpy as np
x,y,c=map(int,input().split())
l2=[]
l3=[]
for i in range(x):
    s=input()
    l=[int(i) for i in s if i!=" "]
    l2.append(l)
for i in range(y):
    str=input()
    m=[int(i) for i in str if i!=" "]
    l3.append(m)
a=np.array(l2)
b=np.array(l3)
print(np.concatenate((a,b),axis=0))








