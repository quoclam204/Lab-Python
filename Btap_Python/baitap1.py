'''
Cho 1 mảng số nguyên. Hãy xuất ra màn hình những dây 3 số má số thứ 3 bằng tổng của 2 số đầu tiên. 
Lưu ý màng được xoay vòng nghĩa là sau vị trí n-1 sẽ là vị trí 0. Các đây được xuất theo thứ tự từ 
trái qua phải. 
Ví dụ màng số nguyễn [ 2, 2, 3, 5, 1, 1 ] có 2 dây thóa yêu cầu được xuất ra màn hình là 2+3=5 và 1+1=2

'''

arr = [ 2, 2, 3, 5, 1, 1 ]

def tim_chuoi(arr):
    n = len(arr)
    result = []

    for i in range(n):
        a = arr[i]
        b = arr[(i + 1) % n] # %n: là sau khi mảng duyệt đến phần tử cuối cùng thì mảng sẻ quay lại vị trí 0 (xoay vòng)
        c = arr[(i + 2) % n]

        if c == a + b:
            result.append(f"{a} + {b} = {c}") # append: thêm phần tử mới vào danh sách result
    
    for item in result:
        print(item)

tim_chuoi(arr)