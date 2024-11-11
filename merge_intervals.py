def Merge_intervals(intervals):
    intervals.sort(key=lambda x:x[0])
    res=[]
    for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
            print(res)
    return res
print(Merge_intervals([[1,3],[2,6],[8,10],[15,18]]))