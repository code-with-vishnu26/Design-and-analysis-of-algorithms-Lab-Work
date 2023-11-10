matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

num_rows = len(matrix)
num_cols = len(matrix[0])

middle_row = matrix[num_rows // 2]
middle_col = [matrix[i][num_cols // 2] for i in range(num_rows)]

intersecting_element = matrix[num_rows // 2][num_cols // 2]

total_sum = sum(middle_row) + sum(middle_col) - intersecting_element

print("Sum of middle row and middle column with intersecting element added once:", total_sum)
