# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
s=input()
m=[]
l=[]
m=s.split(" ")
k=int(input())
sum=0
for i in range(0,k):
    j=input()
    l=j.split(" ")
    if l[0] in m:
        sum=sum+int(l[1])
        m.remove(l[0])
print(sum)    
