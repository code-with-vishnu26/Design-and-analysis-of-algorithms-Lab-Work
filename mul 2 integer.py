multiply = lambda x, y: 0 if y == 0 else x + multiply(x, y - 1)

print(multiply(3,3))
