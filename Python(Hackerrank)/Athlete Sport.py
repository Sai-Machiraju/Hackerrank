def func(x):
    global k
    return x[k]
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list((map(int,input().split()))))
k=int(input())    
a.sort(key=func)
for i in a:
    print(" ".join(map(str,i)))
