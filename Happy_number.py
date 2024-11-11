def happy_number(num):
    def Power(n):
        s=0
        while n>0:
            rem=n%10
            n//=10
            s+=rem**2
        return s
    has_map={num:1}
    n=num
    while n!=1:
        n=Power(n)
        print(n)
        if n in has_map and has_map[n]==1:
            return False

        has_map[n]=1
    return True
print(happy_number(19))


#Optimize
def isHappy(num: int) -> bool:
        def Power(n):
            s=0
            while n>0:
                s+=(n%10)**2
                n//=10
            return s
        has_map=set()
        n=num
        while n!=1 and n not in has_map:
            has_map.add(n)
            n=Power(n)
        return n==1
print(isHappy(19))

