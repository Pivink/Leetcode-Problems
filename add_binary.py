def add_binary(a,b):
    a=int(a,2)
    b=int(b,2)
    c=a+b
    c=bin(c)
    return c[2:]
print(add_binary("11","1"))