from itertools import combinations
n=int(input())
s=input()
l=s.split()
m=int(input())
count=0
v=[]
k=[i for i in range(1,len(l)+1)]
com=list(combinations(k,m))
for i in range(len(l)):
    if l[i]=="a":
        v.append(i+1)
for i in com:
    for j in i:
        if j in v:
            count+=1
            break
print(round(count/len(com),4))
