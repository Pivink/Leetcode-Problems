def Divide(arr):
    arr.sort()
    i,j=0,len(arr)-1
    total,chem=arr[0]+arr[-1],0
    while i<j:
        if arr[i]+arr[j]!=total:
            return -1
        chem+=arr[i]*arr[j]
        i+=1 
        j-=1
    return chem
print(Divide([3,2,5,1,3,4]))