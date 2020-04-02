def count_substring(string, sub_string):
    count=0
    i=-1
    while True:
      i=string.find(sub_string,i+1)
      if (i == -1):
            break
      else:
           count+=1
    return count

