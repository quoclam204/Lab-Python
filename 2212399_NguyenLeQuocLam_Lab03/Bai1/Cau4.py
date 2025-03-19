numbers = [1, 2, 3, 4, 5, 6, 7]

# square = [x**2 for x in numbers]
square = list(map(lambda x: x**2, numbers))

print(square)
  