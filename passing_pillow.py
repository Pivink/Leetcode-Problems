def passing_pillow(n,t):
    i,c=1,0
    while t>0:
        print("i->",i,"c->",c,"t->",t)
        if c%2==0:
            i+=1
            t-=1
        else:
            i-=1
            t-=1
        if i==n and c>=0:
            c-=1
        elif i==1 and c<0:
            c+=1
    return i
def passing_pillow2(n,t):
    i=1
    direction=1
    while t>0:
        i+=direction
        if i==n or i==1:
            direction*=(-1)
        t-=1
    return i
print(passing_pillow2(4,5))