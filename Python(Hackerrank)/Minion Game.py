def minion_game(string):
    # your code goes here
    vowel='AEIOU'
    stuart=0
    kevin=0
    for i in range(0,len(s)):
        if s[i] in vowel:
            kevin+= (len(s)-i)
        else:
            stuart+=(len(s)-i)
    if(stuart>kevin):
        print("Stuart",stuart) 
    elif(kevin>stuart):
        print("Kevin",kevin)
    else:
        print("Draw")               



