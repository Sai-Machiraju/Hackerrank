def swap_case(s):
    new_str=""
    if((s.isupper())=="True"):
        s=s.lower()
        return s
    elif((s.islower())==True):
        s=s.upper()
        return s
    else:
        for k in s:
            if((k.isupper())==True):
                new_str+=(k.lower())
            elif((k.islower())==True):
                new_str+=(k.upper())
            else:
                new_str+=k 
        return new_str                      
