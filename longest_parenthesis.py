def longest_parenthesis(l):
    stack=[-1]
    max_length=0
    for i in range(len(l)):
        if l[i]=="(":
            stack.append(i)
            # print(stack,l[i],max_length,"--append")
        else:
            stack.pop()
            if not stack:
                stack.append(i)
                # print(stack,l[i],max_length,"--append not stack")
            else:
                # print(stack,l[i],max_length,"--Else")
                max_length=max(max_length,i-stack[-1])
    return max_length
s="()(())"
print(longest_parenthesis(s))