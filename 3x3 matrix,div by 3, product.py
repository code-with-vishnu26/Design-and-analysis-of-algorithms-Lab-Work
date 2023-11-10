matrix = [
    [1, 3, 2],
    [9, 4, 12],
    [6, 8, 18]
]
div_by_3 = []

for row in matrix:
    for num in row:
        if num % 3 == 0:
            div_by_3.append(num)

product = 1
for num in div_by_3:
    product *= num

if product > 50:
    print("All the numbers that are divisible:", div_by_3, "product is:", product)
else:
    print("Product is not greater than 50.")
