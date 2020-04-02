def palind(n):
    s=str(n)
    m=s[::-1]
    if s==m:
        return True
    else:
        return False
n=int(input())
a=-1
l=list(map(int,input().split()))
for i in l:
    if i<=0:
        print(False)
        a=0
        break
    if palind(i):
        a+=1
if a!=0 and a!=-1:
    print(True)
elif a ==-1:
    print(False)
