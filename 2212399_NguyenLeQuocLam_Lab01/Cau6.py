def sum_fibonacci_iterative(n):
    a, b = 0, 1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total

print(sum_fibonacci_iterative(6))  # 12
