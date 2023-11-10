def remove_duplicates(input_list):
    if not input_list:
        return []

    unique_elements = []
    for item in input_list:
        is_duplicate = False
        for unique_item in unique_elements:
            if item == unique_item:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_elements.insert(len(unique_elements), item) 

    return unique_elements

mixed_list = [1, 12, 11, 10, 11, 1]
result = remove_duplicates(mixed_list)
print(result)  
