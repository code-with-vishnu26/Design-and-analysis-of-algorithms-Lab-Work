def remove_duplicates(arr):
    if not arr:
        return []

    unique_elements = []
    for item in arr:
        if item not in unique_elements:
            unique_elements.append(item)

    return unique_elements


input_list = [1, 12, 11, 10, 11, 1]
result = remove_duplicates(input_list)
print(result)  
