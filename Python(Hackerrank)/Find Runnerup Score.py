n=int(input())
arr=list(map(int,input().split()))
k=max(arr)
while (max(arr)==k):
  arr.remove(max(arr))
print(max(arr))
