def rev_prefix(s, ch):
    if ch in s:
        i = s.index(ch)
        prefix = ''.join(reversed(s[:i+1]))
        s = prefix + s[i+1:]
    return s
print(rev_prefix("abcdefd", "d"))