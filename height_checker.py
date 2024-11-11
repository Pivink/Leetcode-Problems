def checker(heights):
    expected=sorted(heights)
    c=0
    for i in range(len(heights)):
        if heights[i]!=expected[i]:
            c+=1
    return c
print(checker( [1,1,4,2,1,3]))