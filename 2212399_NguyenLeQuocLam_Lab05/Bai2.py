import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# 🔹 Kết nối đến SQL Server
def get_connection():
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 18 for SQL Server};"
            "SERVER=DESKTOP-E3V9138;"
            "DATABASE=QLMonAn;"
            "UID=sa;"
            "PWD=123456;"
            "Encrypt=no;"
            "TrustServerCertificate=yes;"
        )
        return conn
    except Exception as e:
        print("Lỗi kết nối SQL Server:", e)
        return None

# Lấy danh sách nhóm món ăn
def get_food_groups():
    conn = get_connection()
    if not conn:
        return {}

    cursor = conn.cursor()
    cursor.execute("SELECT MaNhom, TenNhom FROM NhomMonAn ORDER BY MaNhom")
    groups = {row[0]: row[1] for row in cursor.fetchall()}
    conn.close()
    return groups  # Trả về dạng {1: 'Khai vị', 2: 'Hải sản', ...}

# Lấy danh sách món ăn theo nhóm
def get_food_by_group(group_id):
    conn = get_connection()
    if not conn:
        return []

    cursor = conn.cursor()
    cursor.execute("""
        SELECT MonAn.MaMonAn, MonAn.TenMonAn, MonAn.DonViTinh, CAST(MonAn.DonGia AS VARCHAR), NhomMonAn.TenNhom
        FROM MonAn 
        LEFT JOIN NhomMonAn ON MonAn.Nhom = NhomMonAn.MaNhom
        WHERE MonAn.Nhom = ?
        ORDER BY MonAn.MaMonAn
    """, (group_id,))
    
    foods = [tuple(row) for row in cursor.fetchall()]
    conn.close()
    return foods

def update_food_list(event=None):
    selected_group = group_combobox.get()
    group_id = next((key for key, value in food_groups.items() if value == selected_group), None)

    # Xóa dữ liệu cũ trong bảng
    for item in tree.get_children():
        tree.delete(item)

    if group_id is not None:
        foods = get_food_by_group(group_id)
        for food in foods:
            tree.insert("", tk.END, values=food)

def delete_food():
    selected_item = tree.selection()  # Lấy dòng đang chọn
    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một món ăn để xóa!")
        return

    # Lấy Mã món ăn của dòng đang chọn
    item = tree.item(selected_item)
    food_id = item['values'][0]  # Cột đầu tiên là Mã món ăn

    # Xác nhận xóa
    confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa món ăn có Mã {food_id} không?")
    if not confirm:
        return

    # Kết nối database và thực hiện truy vấn xóa
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM MonAn WHERE MaMonAn = ?", (food_id,))
            conn.commit()
            messagebox.showinfo("Thành công", f"Đã xóa món ăn có Mã: {food_id}")

            # Xóa dòng khỏi giao diện
            tree.delete(selected_item)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xóa món ăn: {e}")
        finally:
            conn.close()

def edit_food():
    selected_item = tree.selection()  # Lấy dòng đang chọn
    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một món ăn để sửa!")
        return

    # Lấy Mã món ăn của dòng đang chọn
    item = tree.item(selected_item)
    food_id = item['values'][0]  # Cột đầu tiên là Mã món ăn
    food_name = item['values'][1]  # Cột thứ 2 là Tên món ăn
    unit = item['values'][2]  # Cột thứ 3 là Đơn vị tính
    price = item['values'][3]  # Cột thứ 4 là Đơn giá
    group_name = item['values'][4]  # Cột thứ 5 là Nhóm món ăn

    # Mở cửa sổ sửa món ăn
    edit_window = tk.Toplevel(root)
    edit_window.title("Sửa món ăn")
    edit_window.geometry("400x300")

    # Các trường nhập liệu cho món ăn
    name_label = ttk.Label(edit_window, text="Tên món ăn:")
    name_label.pack(pady=5)
    name_entry = ttk.Entry(edit_window)
    name_entry.insert(0, food_name)
    name_entry.pack(pady=5)

    unit_label = ttk.Label(edit_window, text="Đơn vị tính:")
    unit_label.pack(pady=5)
    unit_entry = ttk.Entry(edit_window)
    unit_entry.insert(0, unit)
    unit_entry.pack(pady=5)

    price_label = ttk.Label(edit_window, text="Đơn giá:")
    price_label.pack(pady=5)
    price_entry = ttk.Entry(edit_window)
    price_entry.insert(0, price)
    price_entry.pack(pady=5)

    group_label = ttk.Label(edit_window, text="Nhóm món ăn:")
    group_label.pack(pady=5)
    group_combobox_edit = ttk.Combobox(edit_window, values=list(food_groups.values()))
    group_combobox_edit.set(group_name)
    group_combobox_edit.pack(pady=5)

    def save_changes():
        new_name = name_entry.get()
        new_unit = unit_entry.get()
        new_price = price_entry.get()
        new_group = group_combobox_edit.get()

        # Tìm MaNhom từ tên nhóm
        new_group_id = next((key for key, value in food_groups.items() if value == new_group), None)

        if not new_name or not new_unit or not new_price or not new_group_id:
            messagebox.showwarning("Cảnh báo", "Vui lòng điền đầy đủ thông tin!")
            return

        # Cập nhật dữ liệu trong cơ sở dữ liệu
        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE MonAn
                    SET TenMonAn = ?, DonViTinh = ?, DonGia = ?, Nhom = ?
                    WHERE MaMonAn = ?
                """, (new_name, new_unit, new_price, new_group_id, food_id))
                conn.commit()

                messagebox.showinfo("Thành công", f"Đã cập nhật món ăn có Mã: {food_id}")
                edit_window.destroy()
                update_food_list()  # Cập nhật lại danh sách món ăn sau khi sửa
            except Exception as e:
                messagebox.showerror("Lỗi", f"Lỗi khi sửa món ăn: {e}")
            finally:
                conn.close()

    save_button = ttk.Button(edit_window, text="Lưu thay đổi", command=save_changes)
    save_button.pack(pady=10)

# Thêm món ăn
def add_food():
    # Mở cửa sổ thêm món ăn
    add_window = tk.Toplevel(root)
    add_window.title("Thêm món ăn")
    add_window.geometry("400x300")

    # Các trường nhập liệu cho món ăn
    name_label = ttk.Label(add_window, text="Tên món ăn:")
    name_label.pack(pady=5)
    name_entry = ttk.Entry(add_window)
    name_entry.pack(pady=5)

    unit_label = ttk.Label(add_window, text="Đơn vị tính:")
    unit_label.pack(pady=5)
    unit_entry = ttk.Entry(add_window)
    unit_entry.pack(pady=5)

    price_label = ttk.Label(add_window, text="Đơn giá:")
    price_label.pack(pady=5)
    price_entry = ttk.Entry(add_window)
    price_entry.pack(pady=5)

    group_label = ttk.Label(add_window, text="Nhóm món ăn:")
    group_label.pack(pady=5)
    group_combobox_add = ttk.Combobox(add_window, values=list(food_groups.values()))
    group_combobox_add.pack(pady=5)

    def save_food():
        new_name = name_entry.get()
        new_unit = unit_entry.get()
        new_price = price_entry.get()
        new_group = group_combobox_add.get()

        # Tìm MaNhom từ tên nhóm
        new_group_id = next((key for key, value in food_groups.items() if value == new_group), None)

        if not new_name or not new_unit or not new_price or not new_group_id:
            messagebox.showwarning("Cảnh báo", "Vui lòng điền đầy đủ thông tin!")
            return

        # Thêm món ăn vào cơ sở dữ liệu mà không cần chỉ định MaMonAn
        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO MonAn (TenMonAn, DonViTinh, DonGia, Nhom)
                    VALUES (?, ?, ?, ?)
                """, (new_name, new_unit, new_price, new_group_id))
                conn.commit()

                messagebox.showinfo("Thành công", "Đã thêm món ăn mới!")
                add_window.destroy()
                update_food_list()  # Cập nhật lại danh sách món ăn sau khi thêm mới
            except Exception as e:
                messagebox.showerror("Lỗi", f"Lỗi khi thêm món ăn: {e}")
            finally:
                conn.close()

    save_button = ttk.Button(add_window, text="Lưu món ăn", command=save_food)
    save_button.pack(pady=10)

# ====================================
# Giao diện Tkinter
# ====================================

root = tk.Tk()
root.title("Quản lý món ăn")
root.geometry("700x500")

# Tiêu đề
title_label = ttk.Label(root, text="Quản lý món ăn", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Chọn nhóm món ăn
frame_top = ttk.Frame(root)
frame_top.pack(fill=tk.X, padx=10)

group_label = ttk.Label(frame_top, text="Nhóm món ăn", font=("Arial", 12, "bold"))
group_label.pack(side=tk.LEFT, padx=5)

food_groups = get_food_groups()

# Nếu có dữ liệu nhóm món ăn, thiết lập combobox
group_combobox = ttk.Combobox(frame_top, values=list(food_groups.values()))
group_combobox.pack(side=tk.RIGHT, padx=5)
group_combobox.bind("<<ComboboxSelected>>", update_food_list)

# Tạo bảng hiển thị danh sách món ăn
columns = ("Mã món ăn", "Tên món ăn", "Đơn vị tính", "Đơn giá", "Nhóm")

tree = ttk.Treeview(root, columns=columns, show="headings", height=10)

# Đặt tiêu đề cột
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor=tk.CENTER, width=120)

tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Chọn nhóm đầu tiên nếu có dữ liệu
if food_groups:
    first_group = next(iter(food_groups.values()))
    group_combobox.set(first_group)  
    update_food_list()  # Gọi sau khi `tree` đã được tạo
else:
    group_combobox.set("Không có nhóm món ăn")  # Tránh lỗi khi danh sách rỗng

# Nút xóa món ăn
delete_button = ttk.Button(root, text="🗑️ Xóa món ăn", command=delete_food)
delete_button.pack(pady=5)

# Nút sửa món ăn
edit_button = ttk.Button(root, text="✏️ Sửa món ăn", command=edit_food)
edit_button.pack(pady=5)

# Nút thêm món ăn
add_button = ttk.Button(root, text="➕ Thêm món ăn", command=add_food)
add_button.pack(pady=5)

# Chạy giao diện
root.mainloop()
