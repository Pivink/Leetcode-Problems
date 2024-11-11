def pascal_triangle(num):
    triangle=[[1]]
    for i in range(1,num):
        raw=[1]
        for j in range(1,i):
            raw.append(triangle[i-1][j-1]+triangle[i-1][j])
        raw.append(1)
        triangle.append(raw)
    return triangle
print(pascal_triangle(3))