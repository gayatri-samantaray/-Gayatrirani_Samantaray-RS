import numpy as np
matrix = np.array([[6,1,1], [4,-2,5], [2,8,7]])
det = (
    matrix[0,0]*(matrix[1,1]*matrix[2,2] - matrix[1,2]*matrix[2,1])
    - matrix[0,1]*(matrix[1,0]*matrix[2,2] - matrix[1,2]*matrix[2,0])
    + matrix[0,2]*(matrix[1,0]*matrix[2,1] - matrix[1,1]*matrix[2,0])
)
print("Determinant:", det)