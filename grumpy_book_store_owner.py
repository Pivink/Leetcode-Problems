def grumpy(customers,grumpy,minutes):
    n=len(customers)
    ans=0
    for i in range(len(customers)):
        if grumpy[i]==0:
            ans+=customers[i]
    unsatisfy=0
    for i in range(minutes):
        if grumpy[i]==1:
            unsatisfy+=customers[i]
    max_=unsatisfy
    for i in range(minutes,n):
        if grumpy[i-minutes]==0:
            unsatisfy-=customers[i-minutes]
        if grumpy[i]==1:
            unsatisfy+=customers[i]
        max_=max(max_,unsatisfy)
    print(max_)
    print(ans+max_)
grumpy([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3)