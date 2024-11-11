def Count_prime(n):
    if n<2:
        return 0
    ref=[True]*n
    i=2
    while i*i<n:
        print("i: ",i)
        if ref[i]:
            for j in range(i*i,n,i):
                print(i*i,i)
                ref[j]=False
        i+=1
    return ref.count(True)-2
print(Count_prime(10))