from collections import OrderedDict
def merge_the_tools(string, k):
        for i in range(0,len(string),k):
            m=string[i:i+k]
            print("".join(OrderedDict.fromkeys(m)))

