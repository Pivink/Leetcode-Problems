def spiral_matrix(matrix):
    row,col=len(matrix),len(matrix[0])
    count,direction=row*col,1
    i,j=0,-1
    res=[]
    while len(res)!=count:
        for _ in range(col):
            j+=direction
            res.append(matrix[i][j])
        row-=1
        for _ in range(row):
            i+=direction
            res.append(matrix[i][j])
        col-=1
        direction*=-1
    return res
print(spiral_matrix([[1,2,3],[4,5,6],[7,8,9]]))