def matrix_multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def is_idempotent(matrix1, matrix2):
    return matrix1 == matrix2

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

matrix = []

print("Enter the elements of the matrix:")

for i in range(n):
    row = []
    for j in range(m):
        element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix.append(row)

M_squared = matrix_multiply(matrix, matrix)

if is_idempotent(matrix, M_squared):
    print("The input matrix is idempotent.")
else:
    print("The input matrix is not idempotent.")
