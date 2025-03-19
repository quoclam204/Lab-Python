import math

# Tính tổng n số nguyên đầu tiên 
def tong_n_so(n):
    if n == 1:
        return 1
    return n + tong_n_so(n - 1)

# Tính n! 
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

# Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không 
def is_perfect_square(num):
    return int(math.sqrt(num))**2 == num

def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Tìm số Fibonacci thứ n 
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Tính tổng n số Fibonacci đầu tiên 
def tong_n_so_fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + tong_n_so_fibonacci(n - 1)

