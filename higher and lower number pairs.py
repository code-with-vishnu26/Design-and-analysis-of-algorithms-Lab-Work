array = [14,21,3,1]
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            print(f"({array[i]},{array[j]})")
