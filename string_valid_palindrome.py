def valid_palindrome(s):
    l=0
    r=len(s)-1
    while l<r:
        if not s[l].isalnum():
            l+=1
        elif not s[r].isalnum():
            r-=1
        elif s[l].lower()==s[r].lower():
            r-=1
            l+=1
        else:
            return False
    return True
print(valid_palindrome("A man, a plan, a canal: Panama"))