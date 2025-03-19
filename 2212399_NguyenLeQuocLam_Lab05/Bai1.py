import pyodbc

# conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=DESKTOP-E3V9138;DATABASE=QLMonAn;UID=sa;PWD=123456;Encrypt=no')
connectionString = '''DRIVER={ODBC Driver 18 for SQL Server};
                      SERVER=DESKTOP-E3V9138;DATABASE=QLSinhVien;
                      UID=sa;PWD=123456;Encrypt=no'''

# Mở chuỗi kết nối
def get_connection():
    try:
        conn = pyodbc.connect(connectionString)
        return conn
    except pyodbc.Error as e:
        print("Không thể kết nối đến SQL Server. Lỗi:", e)
        return None

# Đóng chuỗi kết nối
def close_connection(conn):
    if conn:
        conn.close()

# Hàm lấy danh sách tất cả các lớp học từ bảng 'Lop'
def get_all_class():
    try:
        # Kết nối đến SQL Server
        connection = get_connection()
        if not connection:
            return  # Nếu không kết nối được thì thoát

        cursor = connection.cursor()

        # Câu lệnh SQL lấy dữ liệu từ bảng 'Lop'
        select_query = "SELECT * FROM Lop"
        cursor.execute(select_query)

        # Lấy tất cả dữ liệu
        records = cursor.fetchall()

        # In danh sách lớp ra màn hình
        print("\nDanh sách các lớp học:")
        if len(records) == 0:
            print("Không có lớp nào trong cơ sở dữ liệu.")
        else:
            for row in records:
                print("*" * 50)
                print("Mã lớp: ", row[0])
                print("Tên lớp: ", row[1])

        # Đóng kết nối sau khi lấy dữ liệu
        close_connection(connection)

    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi truy vấn dữ liệu. Thông tin lỗi:", error)

# Hàm lấy danh sách tất cả sinh viên từ bảng 'SinhVien'
def get_all_students():
    try:
        # Kết nối đến SQL Server
        connection = get_connection()
        if not connection:
            return  # Nếu không kết nối được thì thoát

        cursor = connection.cursor()

        # Câu lệnh SQL lấy dữ liệu từ bảng 'SinhVien'
        select_query = "SELECT ID, HoTen, MaLop FROM SinhVien ORDER BY ID"
        cursor.execute(select_query)

        # Lấy tất cả dữ liệu
        records = cursor.fetchall()

        # In danh sách sinh viên ra màn hình
        print("\nDanh sách tất cả sinh viên là:")
        print(f"{'Mã số':<5} {'Họ tên':<25} {'Mã lớp':<5}")
        print("=" * 50)

        for row in records:
            ma_so = row[0]
            ho_ten = row[1]
            ma_lop = row[2] if row[2] is not None else "N/A"  # Xử lý nếu MaLop NULL
            print(f"{ma_so:<5} {ho_ten:<25} {ma_lop:<5}")

        # Đóng kết nối sau khi lấy dữ liệu
        close_connection(connection)

    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi truy vấn dữ liệu. Thông tin lỗi:", error)

def get_all_studentss():
    try:
        # Kết nối đến SQL Server
        connection = get_connection()
        if not connection:
            return  # Nếu không kết nối được thì thoát

        cursor = connection.cursor()

        # Câu lệnh SQL sử dụng JOIN để lấy thêm tên lớp từ bảng 'Lop'
        select_query = """
            SELECT SinhVien.ID, SinhVien.HoTen, SinhVien.MaLop, Lop.TenLop
            FROM SinhVien
            LEFT JOIN Lop ON SinhVien.MaLop = Lop.ID
            ORDER BY SinhVien.ID
        """
        cursor.execute(select_query)

        # Lấy tất cả dữ liệu
        records = cursor.fetchall()

        # In danh sách sinh viên ra màn hình
        print("\nDanh sách tất cả sinh viên là:")
        print(f"{'Mã số':<5} {'Họ tên':<25} {'Mã lớp':<5} {'Tên lớp':<10}")
        print("=" * 60)

        for row in records:
            ma_so = row[0]
            ho_ten = row[1]
            ma_lop = row[2] if row[2] is not None else "N/A"  # Xử lý nếu MaLop NULL
            ten_lop = row[3] if row[3] is not None else "Chưa có lớp"
            print(f"{ma_so:<5} {ho_ten:<25} {ma_lop:<5} {ten_lop:<10}")

        # Đóng kết nối sau khi lấy dữ liệu
        close_connection(connection)

    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi truy vấn dữ liệu. Thông tin lỗi:", error)

# Hàm lấy thông tin lớp và danh sách sinh viên theo Mã Lớp
def get_class_by_id(class_id):
    try:
        connection = get_connection()
        if not connection:
            return  # Nếu không kết nối được thì thoát

        cursor = connection.cursor()

        # Truy vấn lấy thông tin lớp
        select_query = "SELECT * FROM Lop WHERE ID = ?"
        cursor.execute(select_query, (class_id,))
        record = cursor.fetchone()

        if record:
            print(f"\nThông tin lớp có ID = {class_id}:")
            print(f"Mã lớp: {record[0]}")
            print(f"Tên lớp: {record[1]}")
        else:
            print(f"Không tìm thấy lớp có ID = {class_id}")
            close_connection(connection)
            return

        # Truy vấn danh sách sinh viên trong lớp đó
        student_query = "SELECT ID, HoTen FROM SinhVien WHERE MaLop = ? ORDER BY ID"
        cursor.execute(student_query, (class_id,))
        students = cursor.fetchall()

        if students:
            print("\nDanh sách sinh viên trong lớp:")
            print(f"{'Mã số':<5} {'Họ tên':<25}")
            print("=" * 40)
            for student in students:
                print(f"{student[0]:<5} {student[1]:<25}")
        else:
            print("\nLớp này chưa có sinh viên nào.")

        # Đóng kết nối
        close_connection(connection)

    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi truy vấn dữ liệu. Thông tin lỗi:", error)

# Hiển thị danh sách sinh viên theo mã lớp hoặc tên lớp
def get_students_by_class(class_identifier):
    try:
        connection = get_connection()
        if not connection:
            return

        cursor = connection.cursor()

        # Kiểm tra nếu class_identifier là số (tức mã lớp) hay chuỗi (tức tên lớp)
        if isinstance(class_identifier, int):
            query = "SELECT ID, HoTen FROM SinhVien WHERE MaLop = ?"
            cursor.execute(query, (class_identifier,))
        else:
            query = """SELECT SinhVien.ID, SinhVien.HoTen 
                       FROM SinhVien 
                       JOIN Lop ON SinhVien.MaLop = Lop.ID 
                       WHERE Lop.TenLop = ?"""
            cursor.execute(query, (class_identifier,))

        students = cursor.fetchall()

        if students:
            print(f"\nDanh sách sinh viên trong lớp {class_identifier}:")
            print(f"{'Mã số':<5} {'Họ tên':<25}")
            print("=" * 40)
            for student in students:
                print(f"{student[0]:<5} {student[1]:<25}")
        else:
            print(f"⚠️ Không có sinh viên nào trong lớp {class_identifier}")

        close_connection(connection)

    except (Exception, pyodbc.Error) as error:
        print("Lỗi khi truy vấn dữ liệu:", error)

# Tìm sinh viên theo tên trong một lớp
def find_student(class_id, student_name):
    try:
        connection = get_connection()
        if not connection:
            return

        cursor = connection.cursor()
        query = """SELECT ID, HoTen, MaLop FROM SinhVien 
                   WHERE MaLop = ? AND HoTen LIKE ?"""
        cursor.execute(query, (class_id, f"%{student_name}%"))
        students = cursor.fetchall()

        if students:
            print(f"\nDanh sách tất cả sinh viên tên '{student_name}' ở lớp có mã {class_id}:")
            print(f"{'Mã số':<5} {'Họ tên':<25} {'Mã lớp':<5}")
            print("=" * 50)
            for student in students:
                print(f"{student[0]:<5} {student[1]:<25} {student[2]:<5}")
        else:
            print(f"Không có sinh viên nào tên '{student_name}' trong lớp {class_id}")

        close_connection(connection)

    except (Exception, pyodbc.Error) as error:
        print("Lỗi khi truy vấn dữ liệu:", error)

# Gọi hàm để chạy

# get_all_class()

# get_all_students()

# get_all_studentss()

# get_class_by_id(1)

# get_students_by_class(3)  

find_student(3, "Trung")
