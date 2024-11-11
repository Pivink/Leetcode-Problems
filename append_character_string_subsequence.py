def append_for_substring(s,t):
    n=len(t)
    s_iter=iter(s)
    for i,j in enumerate(t):
        print(i,"--",j)
        if j not in s_iter:
            return n-i
    return 0
print(append_for_substring("coaching","coding"))