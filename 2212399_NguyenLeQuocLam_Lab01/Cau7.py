import math

def sum_square_root(n):
    return sum(math.sqrt(i) for i in range(1, n + 1))

print(sum_square_root(4))  
