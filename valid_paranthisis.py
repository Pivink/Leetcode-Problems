def valid_para(s):
    stack=[]
    for i in s:
        if i in '({[':
            stack.append(i)
        elif not stack:
            return False
        else:
             if not stack or  (i == ')' and stack[-1] != '(') or (i == '}' and stack[-1] != '{') or (i == ']' and stack[-1] != '['):
                 return False
             stack.pop()
    return len(stack)==0
t="()[]{}"
# print(t.count('(')==t.count(')'))
print(valid_para(t))