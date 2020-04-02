from collections import deque
d=deque()
for i in range(int(input())):
    command,*args=input().split()
    getattr(d,command)(*args)   
print(" ".join(d))    
