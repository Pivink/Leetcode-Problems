def Split_string(s):
    def track(start,seen):
        if start==len(s):
            return 0
        max_split=0
        for i in range(start+1,len(s)+1):
            string=s[start:i]
            if string not in seen:
                seen.add(string)
                max_split=max(max_split,1+track(i,seen))
                seen.remove(string)
        return max_split
    return track(0,set())
print(Split_string("aba"))