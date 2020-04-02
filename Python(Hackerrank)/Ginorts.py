s=input()
low="".join([i for i in s if i in "abcdefghijklmnopqrstuvwxyz"])
up="".join([i for i in s if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
num=[int(i) for i in s if i in "1234567890"]
odd="".join([str(i) for i in num if i%2!=0])
even="".join([str(i) for i in num if i%2==0])
print("".join(sorted(low)+sorted(up)+sorted(odd)+sorted(even)))
