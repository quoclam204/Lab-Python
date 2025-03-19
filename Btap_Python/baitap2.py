'''
2. Giải các bài tập sau sử dụng biểu thức lambda, filter:

Cho: danh_sach = [5, 7, 6, 9, 14, 26, 21, 17, 44]

a. Xuất các số lẻ không chia hết cho 3

b. Xuất các số nguyên tố

c. Tình tổng các số nguyên tổ của màng

'''

import math


danh_sach = [5, 7, 6, 9, 14, 26, 21, 17, 44]

# a. Xuất các số lẻ không chia hết cho 3
cacSoLe = list(filter(lambda x: x % 2 != 0 and x % 3 != 0, danh_sach))
print(cacSoLe)

# Sử dụng vòng lặp: C1 -> tối ưu hơn C2
result = []
for i in danh_sach:
    if (i % 2 != 0 and i % 3 != 0):
       result.appendlambda (i)

print(result)

# C3
result2 = []
for i in range(len(danh_sach)):
    if (danh_sach[i] % 2 != 0 and danh_sach[i]% 3 != 0):
        result2.append(danh_sach[i])

print(result2)

# b. Xuất các số nguyên tố
def kt_so_nguyen_to(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

def ds_so_nguyen_to(dsSo):
    dsSoNTT = [so for so in dsSo if kt_so_nguyen_to(so)]
    return dsSoNTT


danhSachSo = list(map(int, danh_sach))

dsSoNT = ds_so_nguyen_to(danhSachSo)

print(*dsSoNT)

# Thay vì viết như trên thì dùng filter để lọc
ds_sont = filter(kt_so_nguyen_to, danh_sach)
print(list(ds_sont))

# C2
def so_nguyen_to(n):
    if n < 2:
       return False
    soNguyenTo = list(filter(lambda x : n % x == 0, range(2, n)))

    return len(soNguyenTo) == 0

# Filter giữ lại cái số trong danh sach mà def so_nguyen_to(n): trả về true
ds_so_nt = list(filter(so_nguyen_to, danh_sach))
print(ds_so_nt)
   
def Tong():
    sum = 0
    for i in danh_sach:
        if (kt_so_nguyen_to(i)): # kiểm tra i có phải là số NT ko
            sum += i
    return sum

print(Tong())