def plus_one(l):
    for i in reversed(range(len(l))):
        print(l)
        if l[i]==9:
            l[i]=0
        else:
            l[i]+=1
            return l
    return [1]+l
print(plus_one([9,9]))