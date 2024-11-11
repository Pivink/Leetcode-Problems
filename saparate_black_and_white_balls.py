def Seperate(s):
    black,swap=0,0
    for i in s:
        if i=='0':
            swap+=black
        else:
            black+=1
    return swap
print(Seperate('1110'))