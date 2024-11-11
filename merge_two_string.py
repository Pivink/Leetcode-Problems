def merge(word1,word2):
    s=''
    for i,j in zip(word1,word2):
        if i:
            s+=i
        if j:
            s+=j
    return s
w1="abc"
w2="pqr"
print(merge(w1,w2))