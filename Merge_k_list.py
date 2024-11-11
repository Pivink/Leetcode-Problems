def merge_lists(lists):
    s=[]
    for i in lists:
        j=0
        while j<len(i):
            s.append(i[j])
            j+=1
    print(sorted(s))
li=[[1,4,5],[1,3,4],[2,6]]
# li=[]
merge_lists(li)