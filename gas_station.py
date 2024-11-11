def station(gas,cost):
    sum_gas=sum(gas)
    sum_cost=sum(cost)
    current=0
    start=0
    if sum_cost>sum_gas:
        return -1
    for i in range(len(gas)):
        current+=gas[i]-cost[i]
        if current<0:
            current=0
            start=i+1
    return start
print(station([1,2,3,4,5],[3,4,5,1,2]))

