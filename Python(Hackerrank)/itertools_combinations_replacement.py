from itertools import combinations_with_replacement
s,k=map(str,input().split())
k=int(k)
l1=[]
l=list(combinations_with_replacement(s,k))
for j in l:
    l1.append("".join(sorted("".join(j))))    
l1.sort()
for m in l1:
    print(m)
     
