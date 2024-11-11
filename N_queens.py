def Queens(n):
    board=[["."]*n for i in range(n)] 
    negdiag=set()
    posdiag=set()
    col=set()
    res=[]
    def backtrack(r):
        if r==n:
            copy=["".join(raw) for raw in board]
            res.append(copy)
        for c in range(n):
            if c in col or (r-c) in negdiag or (r+c) in posdiag:
                continue
            col.add(c)
            negdiag.add(r-c)
            posdiag.add(r+c)
            board[r][c]="Q"
            backtrack(r+1)
            col.remove(c)
            negdiag.remove(r-c)
            posdiag.remove(r+c)
            board[r][c]="."
    backtrack(0)
    return res
print(Queens(4))