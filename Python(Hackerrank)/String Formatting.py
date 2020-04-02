def print_formatted(number):
    # your code goes here
    k=(bin(n)).replace("0b","")
    k=(len(k))
    for i in range(1,n+1):
        print("{0:{1}d} {0:{1}o} {0:{1}X} {0:{1}b}".format(i,k))

