import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x


def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Kiểm tra số 13 có phải Fibonacci không
print(is_fibonacci(13))  # True
print(is_fibonacci(14))  # False
