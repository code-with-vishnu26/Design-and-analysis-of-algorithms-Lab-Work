M = [[2, -2, -4],
     [-1, 3, 4],
     [1, -2, -3]
     ]

def matrix_multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

M_squared = matrix_multiply(M, M)

def is_idempotent(matrix1, matrix2):
    return matrix1 == matrix2

if is_idempotent(M, M_squared):
    print("Matrix M is idempotent.")
else:
    print("Matrix M is not idempotent.")
