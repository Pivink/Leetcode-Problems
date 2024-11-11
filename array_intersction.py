def intersection_array(num1,num2):
    num1.sort()
    num2.sort()
    res=[]
    i,j=0,0
    while i<len(num1) and j<len(num2):
        if num1[i]==num2[j]:
            res.append(num1[i])
            i+=1
            j+=1
        elif num1[i]<num2[j]:
            i+=1
        else:
            j+=1
    return res
print(intersection_array([1,2,1],[1,2]))