a,b=map(int,input().split())
l1=[]
l2=[]
ind=[]
main=[]
for i in range(a):
    ele=input()
    l1.append(ele)
for i in range(b):
    ele=input()
    l2.append(ele)   
for i in l2:
    for j in range(len(l1)):
        if i==l1[j]:
            ind.append(j+1)
    if len(ind)==0:
        ind.append(-1)        
    main.append(ind)
    ind=[]
for i in range(len(main)):
    main[i]=map(str,main[i])
    print(" ".join(main[i]))    
