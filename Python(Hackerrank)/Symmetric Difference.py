n=int(input())
a=set(list(map(int,input().split())))
m=int(input())
b=set(list(map(int,input().split())))
l=[]
for j in a.difference(b):
    l.append(j)
for i in b.difference(a):
    l.append(i)
l.sort()    
for i in l:
    print(i)    
