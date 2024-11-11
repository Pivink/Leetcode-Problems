def traping(height):
    left=[]
    right=[0]*len(height)
    left.append(height[0])
    right[-1]=height[-1]
    for i in range(1,len(height)):
        left.append(max(height[i],left[i-1]))
    for i in range(len(height)-2,-1,-1):
        right[i]=max(height[i],right[i+1])
    trap=0
    for i in range(len(height)):
        water=min(left[i],right[i])
        trap+=water-height[i]
    return trap
print(traping([0,1,0,2,1,0,1,3,2,1,2,1]))