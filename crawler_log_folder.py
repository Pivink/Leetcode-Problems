def log_crawler(logs):
    res=0
    for i in logs:
        if i=="../":
            if res>0:
                res-=1
            else:
                res=0
        elif i != "./":
            res+=1
    print(res)
log_crawler(["d1/","d2/","./","d3/","../","d31/"])