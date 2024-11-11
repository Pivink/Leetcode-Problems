def Set_zeroes(matrix):
    row,col=len(matrix),len(matrix[0])
    z_row,z_col=set(),set()
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==0:
                z_row.add(i)
                z_col.add(j)
    for i in z_row:
        for j in range(col):
            matrix[i][j]=0
    for j in z_col:
        for i in range(row):
            matrix[i][j]=0
m=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Set_zeroes(m)
print(m)