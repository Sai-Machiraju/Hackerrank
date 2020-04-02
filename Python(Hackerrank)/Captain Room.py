from collections import Counter
n=int(input())
a=list(map(int,input().split()))
m=Counter(a)
k=list(m.keys())
v=list(m.values())
ind=v.index(1)
print(k[ind])
