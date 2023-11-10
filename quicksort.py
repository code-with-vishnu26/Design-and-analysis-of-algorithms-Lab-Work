def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(arr)
    return quicksort(left) + middle + quicksort(right)
array = [8, 20, 9, 4, 15, 10, 7, 22, 3, 12 ]
sorted_array = quicksort(array)
print(sorted_array)
