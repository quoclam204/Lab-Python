import math

danh_sach = [5, 7, 6, 9, 14, 26, 21, 17, 44]

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