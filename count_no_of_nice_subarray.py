def count_no(nums,k):
    hashing={0:1}
    result=0
    odd=0
    for i in nums:
        if i%2==1:
            odd+=1
        if odd-k in hashing:
            result+=hashing[odd-k]
        if odd in hashing:
            hashing[odd]+=1
        else:
            hashing[odd]=1
    return result
print(count_no([1,1,2,1,1],3))