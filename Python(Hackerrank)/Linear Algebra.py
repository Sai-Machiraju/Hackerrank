import numpy as np
x=int(input())
l=[]
l1=[]
l2=[]
for i in range(x):
    s=input()
    l=s.split()
    for i in l:
        l1.append(float(i))
    l2.append(l1)   
    l1=[]
a=np.array(l2)    
print(round(np.linalg.det(a),2))     



