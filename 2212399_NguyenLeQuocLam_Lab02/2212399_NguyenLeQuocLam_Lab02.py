from datetime import datetime

class SinhVien:
    # thuộc tính
    truong = "Đại học Đà Lạt"

    # self để truy cập và gán giá trị, và dùng để truy cập các thuộc tính của đối tượng
    # _ là private, chỉ được truy cập bên trong lớp
    # __init__: là một hàm khởi tạo
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self._maSo = maSo
        self._hoTen = hoTen
        self._ngaySinh = ngaySinh
    
    # lấy giá trị mã số
    @property
    def maSo(self):
        return self._maSo
    
    # kiểm tra nếu mã số hợp lệ _maSo sẽ được cập nhật, nếu ko setter ko gán giá trị mới cho _maSo
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self._maSo = maso
        else:
            raise ValueError("Mã số không hợp lệ. Mã số phải có đúng 7 chữ số.")

    # kiểm tra mã số hợp lệ là maso có 7 chữ số
    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7
    
    @property
    def hoTen(self):
        return self._hoTen  # Trả về giá trị của _hoTen

    @hoTen.setter
    def hoTen(self, ho_ten_moi):
        if len(ho_ten_moi) > 0:
            self._hoTen = ho_ten_moi
        else:
            raise ValueError("Họ tên không được để trống.")
    
    # classmethod: định nghĩa phương thức lớp, Phương thức này không làm việc với các thuộc tính 
    # của một đối tượng cụ thể mà thay vào đó làm việc với thuộc tính của lớp.
    '''

    Phương thức đối tượng: Hoạt động trên một đối tượng cụ thể, tham số đầu tiên là self (đối tượng hiện tại).
    Phương thức lớp: Hoạt động trên lớp, tham số đầu tiên là cls (lớp hiện tại).

    '''
    @classmethod
    def doiTenTruong(cls, tenmoi):
        cls.truong = tenmoi

    # phương thức ghi đè toString()
    def __str__(self) -> str:
        ngaySinhFormat = self._ngaySinh.strftime("%d/%m/%Y")  # Định dạng ngày tháng năm
        return f"{self._maSo}\t{self._hoTen}\t{ngaySinhFormat}"
    
    # xuất sinh viên
    def Xuat(self):
        ngaySinhFormat = self._ngaySinh.strftime("%d/%m/%Y")
        print(f"{self._maSo}\t{self._hoTen}\t{ngaySinhFormat}")

class DanhSachSV:

    # phương thức khởi tạo dssv rỗng
    def __init__(self) -> None: # None: phương thức không trả về giá trị nào
        self.dssv = []

    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)
    
    def xuatDSSV(self):
        for sv in self.dssv:
            print(sv)

    def timSvTheoMaSo(self, mssv: int):
        return [sv for sv in self.dssv if sv.maSo == mssv]

    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen.lower() in ten.lower()]

    # Hàm enumerate() giúp lấy chỉ mục và giá trị của dssv
    def timVTSvTheoMaSo(self, mssv: int):
        for index, sv in enumerate(self.dssv):
            if (sv.maSo == mssv):
                return index
        return -1

    # def timVTSvTheoMaSo(self, mssv: int):
    #     for i in range (len(self.dssv)):
    #         if self.dssv[i].maSo == mssv:
    #             return i
    #     return -1


    '''

    self.dssv[:] tạo ra một bản sao của danh sách, giúp bạn tránh gặp phải vấn đề khi thay đổi (xóa) phần tử trong khi đang lặp qua danh sách.
    Việc sử dụng bản sao giúp vòng lặp tiếp tục kiểm tra tất cả các phần tử mà không bị gián đoạn khi thay đổi danh sách ban đầu.

    '''
    def xoaSvTheoMaSo(self, mssv: int) -> bool:
        for sv in self.dssv[:]:
            if sv.maSo == mssv:
                self.dssv.remove(sv)
                return True
        return False
    
    # def xoaSvTheoMaSo(self, mssv: int) -> bool:
    #     for sv in self.dssv:
    #         if (sv.maSo == mssv):
    #             self.dssv.remove(sv)
    #             return True
    #     return False

    def __str__(self):
        # Ghi đè để hiển thị danh sách sinh viên
        return "\n".join(str(sv) for sv in self.dssv)
    
    def docTuFile(self, ten_file: str):
        with open(ten_file, 'r', encoding='utf-8') as file:
            for line in file:

                parts = line.strip().split(', ')

                maSo = int(parts[0])
                hoTen = parts[1].strip('"') # Họ tên sinh viên (bỏ dấu ngoặc kép)
                
                # Tách năm, tháng, ngày từ các phần tử
                nam = int(parts[2])
                thang = int(parts[3])
                ngay = int(parts[4])

                # Tạo đối tượng datetime từ năm, tháng, ngày
                ngaySinh = datetime(nam, thang, ngay)

                # Tạo sinh viên và thêm vào danh sách
                sv = SinhVien(maSo, hoTen, ngaySinh)
                self.themSinhVien(sv)

    # Mặc định reverse là False
    def sapXepTangTheoTen(self):
        self.dssv = sorted(self.dssv, key=lambda sv: sv.hoTen.lower())
    
    # reverse=True là giảm dần
    # khi dùng sort() sẽ làm thay đổi danh sách gốc
    def sapXepGiamTheoTen(self):
        self.dssv = sorted(self.dssv, key=lambda sv: sv.hoTen.lower(), reverse=True)

    # def sapXepTangTheoTen(self):
    #     for i in range(len(self.dssv) - 1):
    #         for j in range(i + 1, len(self.dssv)):
    #             if (self.dssv[i].hoTen > self.dssv[j].hoTen):
    #                 tmp = self.dssv[i]
    #                 self.dssv[i] = self.dssv[j]
    #                 self.dssv[j] = tmp

ds = DanhSachSV()

# ds.themSinhVien(SinhVien(2212685, "Nguyễn Văn A", datetime(2025, 2, 15)))
# ds.themSinhVien(SinhVien(2212222, "Nguyễn Văn B", datetime(2025, 3, 22)))
# ds.themSinhVien(SinhVien(2212321, "Nguyễn Văn C", datetime(2025, 2, 2)))
# ds.themSinhVien(SinhVien(2212213, "Nguyễn Văn D", datetime(2025, 8, 12)))
# ds.themSinhVien(SinhVien(2212734, "Nguyễn Văn E", datetime(2025, 4, 11)))

# ds.xuatDSSV()

ds.docTuFile("DanhSachSV.txt")
ds.xuatDSSV()

ten = str(input("Nhập tên cần tìm: "))
kq = ds.timSvTheoTen(ten)

if kq:
    print("Kết quả tìm kiếm: ")
    for sv in kq:
        print(sv)
else:
    print("Không tìm thấy sinh viên nào có tên: ", ten)


maSo = int(input("Nhập mã số cần tìm: "))
kq1 = ds.timVTSvTheoMaSo(maSo)

print(f"\nVị trí của sinh viên có mã số {maSo}: {kq1}")

xoaMaSo = int(input("Nhập mã số sinh viên cần xóa: "))
kq2 = ds.xoaSvTheoMaSo(xoaMaSo)
print("Danh sách sau khi xóa:")
ds.xuatDSSV()

print("Danh sách SV tăng theo tên: ")
ds.sapXepTangTheoTen()
ds.xuatDSSV()