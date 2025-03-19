import math


class PhanSo:

    def __init__(self, x, y) -> None:
        if y == 0:
            raise ValueError("Mẫu số không thể bằng 0.")
        self.x = x
        self.y = y
        self.rutGon() # Tự động rút gọn khi khởi tạo

    def rutGon(self):
        gcd = math.gcd(self.x, self.y) # Tìm UCLN của 2 số x và y
        self.x //= gcd
        self.y //= gcd
        if self.y < 0: # Quy ước mẫu số luôn dương
            self.x = -self.x
            self.y = -self.y

    def __str__(self):
        return f"{self.x}/{self.y}"

    # Cộng 2 phân số
    def __add__(self, other):
        tu = self.x * other.y + other.x * self.y
        mau = self.y * other.y
        return PhanSo(tu, mau)

    # Trừ 2 phân số
    def __sub__(self, other):
        tu = self.x * other.y - other.x * self.y
        mau = self.y * other.y
        return PhanSo(tu, mau)

    # Nhân 2 phân số
    def __mul__(self, other):
        tu = self.x * other.x
        mau = self.y * other.y
        return PhanSo(tu, mau)

    # Chia 2 phân số
    def __truediv__(self, other):
        if other.x == 0:
            raise ZeroDivisionError("Không thể chia cho phân số có tử số bằng 0.")
        
        tu = self.x * other.y
        mau = self.y * other.x
        return PhanSo(tu, mau)
    
    def is_negative(self):
        return self.x < 0
    
    def is_positive(self):
        return self.x > 0
    
    # So sánh giá trị thực của hai phân số mà không cần đổi thành số thực (float). -> (2)
    def __lt__(self, other):
        return self.x * other.y < other.x * self.y
    
    # So sánh hai phân số có bằng nhau không -> (3)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
class DsPhanSo:
    
    def __init__(self):
        self.dsps = []    

    def them(self, ps):
        self.dsps.append(ps)

    def xuat(self):
        for ds in self.dsps:
            print(str(ds))

    # Số 1 là mỗi lần có số âm thì + 1 vào tổng(sum)
    def demPhanSoAm(self):
        return sum(1 for ps in self.dsps if ps.is_negative())
    
    # def phanSoDuongMin(self):
    #     return min(ps for ps in self.dsps if ps.is_positive())

    def phanSoDuongMin(self):
        ps_duong = [ps for ps in self.dsps if ps.is_positive()]
        
        return min(ps_duong, default=None)
    
    def timVTPhanSo(self, x):
        return [i for i, ps in enumerate(self.dsps) if ps == x]
    
    def tongPhanSoAm(self):
        sum = PhanSo(0, 1)
        for ps in self.dsps:
            if ps.is_negative():
                sum += ps
        return sum
    
    def xoaPhanSo(self, x):
        self.dsps = [ps for ps in self.dsps if ps != x]
    




ds = DsPhanSo()

ds.them(PhanSo(2, 3))
ds.them(PhanSo(-3, 4))
ds.them(PhanSo(3, 4))

ds.xuat()

# Đếm số phân số âm
print("Tổng số âm:", ds.demPhanSoAm())

# Tìm phân số dương nhỏ nhất
print("Số dương nhỏ nhất trong mảng:", ds.phanSoDuongMin())

# Tìm vị trí của phân số

# tu = int(input("Nhập tử số: "))
# mau = int(input("Nhập mẫu số: "))
# x = PhanSo(tu, mau)
x = PhanSo(2, 3)
print("vị trí là: ", ds.timVTPhanSo(x))

# Tính tổng các phân số âm
print(ds.tongPhanSoAm())

# Xóa phân số
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
x = PhanSo(tu, mau)

print("Danh sách phân số sau khi xóa:")
ds.xoaPhanSo(x)
ds.xuat()
