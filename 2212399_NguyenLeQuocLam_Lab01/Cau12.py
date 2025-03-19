import math

arr = [3, 10, 5, 8, 13, 21, 34, 55, 7, 2]

# Câu a: Xuất tất cả số lẻ không chia hết cho 5
def odd_not_divisible_by_5(arr):
    return [x for x in arr if x % 2 == 1 and x % 5 != 0]

print(odd_not_divisible_by_5(arr)) 

# Câu b: Xuất tất cả các số Fibonacci trong danh sách
def is_perfect_square(n):
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def filter_fibonacci(arr):
    return [x for x in arr if is_fibonacci(x)]

print(filter_fibonacci(arr))  

# Câu c: Tìm số nguyên tố lớn nhất
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def max_prime(arr):
    primes = [x for x in arr if is_prime(x)]
    return max(primes, default=None)

print(max_prime(arr))  

# Câu d: Tìm số Fibonacci bé nhất
def min_fibonacci(arr):
    fib_nums = [x for x in arr if is_fibonacci(x)]
    return min(fib_nums, default=None)

print(min_fibonacci(arr))  

# Câu e: Tính trung bình các số lẻ
def average_odd(arr):
    odd_numbers = [x for x in arr if x % 2 == 1]
    return sum(odd_numbers) / len(odd_numbers) if odd_numbers else None

print(average_odd(arr))  # 9.8


# Câu f: Tính tích các số lẻ không chia hết cho 3
from functools import reduce

def product_odd_not_div3(arr):
    odd_numbers = [x for x in arr if x % 2 == 1 and x % 3 != 0]
    return reduce(lambda x, y: x * y, odd_numbers, 1)

print(product_odd_not_div3(arr))  # 65

# Câu g:  Đổi chỗ 2 phần tử
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

arr = [1, 2, 3, 4, 5]
swap(arr, 1, 3)
print(arr)  # [1, 4, 3, 2, 5]

# Câu h: Đảo ngược danh sách
def reverse_list(arr):
    return arr[::-1]

print(reverse_list(arr))  

# Câu i: Xuất số lớn thứ nhì
def second_largest(arr):
    unique_sorted = sorted(set(arr), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

print(second_largest(arr))  

# Câu j: Tính tích chữ số các số chẵn
def product_digit_even_numbers(arr):
    even_numbers = [x for x in arr if x % 2 == 0]
    return reduce(lambda x, y: x * y, even_numbers, 1)

print(product_digit_even_numbers(arr))  

# Câu k: Đếm số lần xuất hiện của một số
from collections import Counter

def count_occurrences(arr, x):
    return arr.count(x)

print(count_occurrences(arr, 5))  

# Câu l: Xuất các số xuất hiện n lần
def numbers_appear_n_times(arr, n):
    counter = Counter(arr)
    return [num for num, count in counter.items() if count == n]

print(numbers_appear_n_times(arr, 2))  

# Câu m: Xuất số xuất hiện nhiều lần nhất
def most_frequent_number(arr):
    counter = Counter(arr)
    return max(counter, key=counter.get)

print(most_frequent_number(arr))  







