m=int(input())
a=set(map(int,input().split()))
n=int(input())
k=[]
for i in range(0,n):
    s=input()
    l=[]
    l=s.split()
    if l[0]=="intersection_update":
        k=list(map(int,input().split()))
        a.intersection_update(k)
        k=[]
    elif l[0]=="update":
        k=set(map(int,input().split()))
        a.update(k)
        k=[]
    elif l[0]=="symmetric_difference_update":
        k=list(map(int,input().split()))
        a.symmetric_difference_update(k)
        k=[]
    else:
        k=set(map(int,input().split()))
        a.difference_update(k)
        k=[]
print(sum(a))        

