from itertools import permutations
s,k=map(str,input().split())
k=int(k)
l1=[]
l=list(permutations(s,k))
for i in l:
    l1.append("".join(i))
l1.sort()
for i in l1:
    print(i)    
