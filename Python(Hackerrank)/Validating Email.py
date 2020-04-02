def fun(s):
    # return True if s is a valid email, else return False
    if "@" and "." not in s or s.count("@")>1 or s.count(".")>1:
        return False
    l=s.split("@")
    if l[0]=="":
        return False
    for i in l[0]:
        if i.lower() not in "abcdefghijklmnopqrstuvwxyz1234567890_-":
            return False
    m=l[1].split(".")
    for i in m[0]:
        if i.lower() not in "abcdefghijklmnopqrstuvwxyz1234567890":
            return False

    if len(m[1])>3:
        return False
    return True        

