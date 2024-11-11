def Sort(nums):
    dict={}
    max_num=max(nums)
    for i in nums:
        if i in nums and i in dict:
            dict[i]+=1
        elif i in nums and i not in dict:
            dict[i]=1
        else:
            dict[i]=0
    j=0
    for i in sorted(dict):
        while dict[i]>0:   
            print(i)
            nums[j]=i
            dict[i]-=1
            j+=1         
        
    print(nums)
Sort([2,0,2,1,1,0])
