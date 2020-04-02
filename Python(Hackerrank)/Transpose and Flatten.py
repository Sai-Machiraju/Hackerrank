import numpy as np
x, y = map(int,input().split())
l2=[]
for i in range(x):
    s=input()
    l1=[int(i) for i in s if i!=" "]
    l2.append(l1)
a=np.array([l2[0]])    
for i in range(1,len(l2)):    
    a=np.append(a,[(l2[i])],axis=0)
b=np.transpose(a)
print(b)
print(a.flatten())



