from itertools import combinations
s,k=map(str,input().split())
k=int(k)
l1=[]
for i in sorted(s):
       print(i)
for i in range(2,k+1):
    l=list(combinations(s,i))
    for j in l:
        l1.append("".join(sorted("".join(j))))    
    l1.sort()
    for m in l1:
         print(m)
    l1=[]     
