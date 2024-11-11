def generate(n):
    stack=[]
    res=[]
    def backtrack(openN,closeN):
        if openN==closeN==n:
            res.append("".join(stack))
            return 
        if openN < n:
            stack.append("(")
            print(stack)
            backtrack(openN+1,closeN)
            stack.pop()
        if closeN < openN:
            stack.append(")")
            print(stack)
            backtrack(openN,closeN+1)
            stack.pop()
    backtrack(0,0)
    return res
print(generate(3))
# stack=[")"]
# res=[]
# res.append("".join(stack))
# print(res)