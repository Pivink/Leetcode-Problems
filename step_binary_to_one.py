def binary_to_one(s):
    decimal=int(s,2)
    count=0
    print(decimal)
    while decimal>1:
        if decimal%2==0:
            decimal//=2
            print(decimal)
        else:
            decimal+=1
        count+=1
    return count
print(binary_to_one("1111011110000011100000110001011011110010111001010111110001"))