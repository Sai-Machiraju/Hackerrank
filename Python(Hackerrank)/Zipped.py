n,x=map(int,input().split())
m=[]
for i in range(x):
    l=list(map(float,input().split()))
    m.append(l)
marks=list(zip(*m))
for i in marks:
    print(sum(i)/len(i))    
