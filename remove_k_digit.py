from decimal import Decimal

def removeKdigits(num, k):
    s = []
    for i in num:
        while k > 0 and s and s[-1] > i:
            k -= 1
            s.pop()
        s.append(i)

    res = "".join(s[:len(s)-k]).lstrip("0")
    return res if res else "0"
n=input("Enter an number : ")
k=int(input("How many digit to remove: "))
print(n)
print(removeKdigits(n,k))