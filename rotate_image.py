import numpy as np
def rotate(m):
# Example matrix
    matrix = np.array(m)

    # Reverse the rows of the matrix
    rev= np.flip(matrix, axis=0)

    # Transpose the reversed matrix
    rev= np.transpose(rev)

    print("Original Matrix:")
    print(matrix)
    print("\nTransposed Matrix with Last Row as First:")
    print(rev)
rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
