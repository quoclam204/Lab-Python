import math

def solve_quadratic(a, b, c):
    if a == 0:
        return "Không phải phương trình bậc 2"
    
    delta = b ** 2 - 4 * a * c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Nghiệm x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x = -b / (2 * a)
        return f"Nghiệm kép x = {x}"
    else:
        return "Phương trình vô nghiệm"

# Giải phương trình x^2 - 3x + 2 = 0
print(solve_quadratic(1, -3, 2))
