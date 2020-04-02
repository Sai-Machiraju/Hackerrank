for i in range(int(input())):
    n=int(input())//2
    l=list(map(int,input().split()))
    a=0
    while l:
        if l.index(max(l)) not in [0,len(l)-1]:
           print("No")
           a=1
           break
        else:
            l=l.remove(max(l))
    if a==0:        
       print("Yes")
