import pandas as pd

# Hiển thị giá xe trung bình của mỗi hãng xe 

# Đọc file CSV
df = pd.read_csv("E:\\Python\\Automobile_data.csv")

# Chuyển đổi cột 'price' sang kiểu số (nếu có lỗi thì chuyển thành NaN)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Loại bỏ các dòng có giá trị NaN trong cột 'price'
df = df.dropna(subset=['price'])

# Tính giá trung bình của mỗi hãng xe
avg_price_per_company = df.groupby('company')['price'].mean()

# Xuất kết quả
print(avg_price_per_company)
