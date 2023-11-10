def chrs_associated_numbers(number):
    chr_mapping = {
        '1': '000',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqr',
        '8': 'stu',
        '9': 'vwx'
    }

    number_str = str(number)
    pairs = ['']

    for num in number_str:
        new_pairs = []
        for chr in chr_mapping[num]:
            for combination in pairs:
                new_pairs.append(combination + chr)
        pairs = new_pairs

    return pairs

number = input("Enter a number (0-9): ")
pairs = chrs_associated_numbers(number)
print(pairs)
