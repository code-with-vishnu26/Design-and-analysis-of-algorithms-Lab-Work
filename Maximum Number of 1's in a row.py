matrix = [
    [0, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 1]
]

max_row = -1
max_count = -1

for i, row in enumerate(matrix):
    count_ones = row.count(1)
    
  
    if count_ones > max_count:
        max_row = i
        max_count = count_ones

print(f"Row {max_row + 1} has the most ones with {max_count} ones.")
