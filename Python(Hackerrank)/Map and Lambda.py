cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n==0:
        return []
    elif n==1:
        return [0]
    else:
        a=0
        b=1
        l=[]
        l.append(a)
        l.append(b)
        i=n-2
        while i:
            c=a+b
            l.append(c)
            a=b
            b=c
            i-=1
        return l     

