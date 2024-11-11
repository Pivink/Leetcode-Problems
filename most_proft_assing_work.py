def assign_work(difficulty,profit,worker):
    res,j,best,temp=0,0,0,[]
    for i in range(len(difficulty)):
        temp.append((difficulty[i],profit[i]))
    print(temp)
    temp.sort()
    worker.sort()
    for work in worker:
            while j < len(temp) and work >= temp[j][0]:
                best = max(best, temp[j][1])
                j += 1
            res += best
    return res
print(assign_work([2,4,6,8,10],[10,20,30,40,50],[4,5,6,7]))