def climbing_stairs(n):
    if n>=2:
        return n
    p=1
    c=2
    for i in range(3,n+1):
        next_step=p+c
        p=c
        c=next_step
    return c
print(climbing_stairs(2))