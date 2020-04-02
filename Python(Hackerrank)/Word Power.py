from collections import Counter
l=[]
m=[]
l2=[]
for i in range(int(input())):
    l.append(input())
c=Counter(l)
m=c.values()
print(len(m))
for i in m:
    print(i,end=" ")
