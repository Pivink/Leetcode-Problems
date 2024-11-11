def Maximum_gold(grid):
    nrow,ncol=len(grid),len(grid[0])
    visited=set()
    def inbound(raw,col):
        return 0<=raw<nrow and 0<=col<ncol
    def Path(raw,col):
        if not inbound(raw,col) or (raw,col) in visited or grid[raw][col]==0:
            return 0
        visited.add((raw,col))
        up=Path(raw-1,col)
        down=Path(raw+1,col)
        left=Path(raw,col-1)
        right=Path(raw,col+1)
        visited.remove((raw,col))
        return grid[raw][col]+max(up,down,left,right)
    max_gold=0
    for i in range(nrow):
        for j in range(ncol):
            if grid[i][j] and (i,j) not in visited:
                max_gold=max(max_gold,Path(i,j))
    return max_gold
print(Maximum_gold( [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))