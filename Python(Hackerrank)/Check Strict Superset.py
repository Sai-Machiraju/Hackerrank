a=set(map(int,input().split()))
k=[]
for i in range(int(input())):
    l=set(map(int,input().split()))
    if a.intersection(l)==l and len(a)>len(l):
        k.append(True)
    else:
        k.append(False)    
if all(k):
    print(True)
else:
    print(False)            
