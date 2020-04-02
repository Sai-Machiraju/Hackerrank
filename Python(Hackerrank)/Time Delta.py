from datetime import datetime 
for i in range(int(input())):
    frmt="%a %d %b %Y %H:%M:%S %z"
    print(int(abs((datetime.strptime(input(),frmt)-datetime.strptime(input(),frmt)).total_seconds())))
