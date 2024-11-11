def make_bouquets(bloomday,m,k):
    if len(bloomday)<(m*k):
        return -1
    def isbouquet(bloomday,m,k,day):
        total=0
        flower=0
        for b in bloomday:
            if b<=day:
                flower+=1
                if flower==k:
                    total+=1
                    flower=0
            else:
                flower=0
            if total>=m:
                return True
        return False
    low,high=0,max(bloomday)
    while low < high:
        mid =(low+high)//2
        if isbouquet(bloomday,m,k,mid):
            high=mid
        else:
            low=mid+1
    return low
print(make_bouquets([1,10,3,10,2],3,1))