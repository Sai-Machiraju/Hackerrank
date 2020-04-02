a=[]
for i in range(int(input())):
    l=[]
    m=[]
    e=int(input())
    l=set(map(int,input().split()))
    el=int(input())
    m=set(map(int,input().split()))
    if l.union(m)==m:
        a.append(True)
    else:
        a.append(False) 
for i in a:
    print(i)           
