def power(n):
    s=[2**i for i in range(0,30)]
    if n in s and n>=-2**31 and n<2**31-1:
        print(True)
    else:
        print(False)
power(1073741824)
print(2**31)