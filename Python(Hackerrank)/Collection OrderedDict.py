n=int(input())
m=[]
p=[]
for i in range(n):
    s=input()
    l=s.split()
    m.append(l)    
sum=0    
for i in range(len(m)):
    sum=int(m[i][-1])
    for j in range(i+1,len(m)):
        if m[i][:-1]==m[j][:-1]:
            sum=sum+int(m[i][-1])
    if m[i] not in p:        
       print(" ".join(m[i][:-1]),sum)
       p.append(m[i])
      
