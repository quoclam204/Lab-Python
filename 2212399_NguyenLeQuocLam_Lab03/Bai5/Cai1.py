import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Xuất tất cả các số lẻ không chia hết cho 5
# Cách 1:
def cac_so_le():
    for i in numbers:
        if i % 2 != 0 and i % 5 != 0:
            print(i)

# Cách 2:
so_le = [i for i in numbers if i % 2 != 0 and i % 5 != 0]


# Xuất tất cả các số Fibonacci
def fibonacci(n):
    fib_list = [0, 1]  # Khởi tạo 2 số đầu tiên
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])  # Cộng 2 số cuối
    return fib_list

# Tìm số nguyên tố lớn nhất
def kt_so_nguyen_to(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

def tim_so_nt_max(n):
    so_nt = [num for num in n if kt_so_nguyen_to(num)]
    return max(so_nt) if so_nt else None  # Trả về None nếu không có số nguyên tố

# Tìm số Fibonacci bé nhất 
def tim_so_fibonacci_min(n):
    so_fi = [num for num in n if fibonacci(num)]
    return min(so_fi) if so_fi else None


# Tính trung bình các số lẻ
def trung_binh_so_le(n):
    so_le = [num for num in n if num % 2 != 0]
    if not so_le:
        return None
    return sum(so_le) / len(so_le)

# Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng 
def tich_so_le(n):
    so_le_khong_3 = [num for num in n if num % 2 != 0 and num % 3 != 0]

    if not so_le_khong_3:
        return 1
    
    tich = 1
    for num in so_le_khong_3:
        tich *= num
    
    return tich

# Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ 
def doi_cho_phan_tu(lst, index1, index2):
    if index1 < 0 or index2 < 0 or index1 >= len(lst) or index2 >= len(lst):
        print("Vị trí nhập vào không hợp lệ!")
        return lst  # Giữ nguyên danh sách nếu vị trí không hợp lệ
    
    lst[index1], lst[index2] = lst[index2], lst[index1]  # Đổi chỗ 2 phần tử
    return lst

# Đảo ngược trật tự các phần tử của danh sách i) Xuất tất cả các số lớn thứ nhì của danh sách 
reversed_numbers = numbers[::-1]

def so_lon_thu_nhi(numbers):
    unique_numbers = list(set(numbers))  # Loại bỏ số trùng lặp
    unique_numbers.sort(reverse=True)  # Sắp xếp giảm dần
    
    if len(unique_numbers) < 2:
        return None  # Không có số lớn thứ nhì
    
    return unique_numbers[1]  # Lấy số lớn thứ nhì

# Tính tổng các chữ số của tất cả các số trong danh sách 
def tong_cac_chu_so(numbers):
    return sum(sum(int(digit) for digit in str(abs(num))) for num in numbers)

# Đếm số lần xuất hiện của một số trong danh sách
def dem_so_lanXuat_hien(x):
    return numbers.count(x)

# Xuất các số xuất hiện n lần trong danh sách 
def so_xuat_hien_n_lan(numbers, n):
    tan_suat = {}  # Dictionary lưu số lần xuất hiện của từng số
    
    for num in numbers:
        tan_suat[num] = tan_suat.get(num, 0) + 1  # Đếm số lần xuất hiện
    
    return [num for num, count in tan_suat.items() if count == n]  # Lọc số xuất hiện đúng n lần

