import pandas as pd

# Hãy hiển thị giá xe cao nhất của mỗi hãng xe 

# Đọc file CSV
df = pd.read_csv("E:\\Python\\Automobile_data.csv")

# Đảm bảo cột 'price' là kiểu số
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Loại bỏ các dòng có giá trị NaN trong cột 'price'
df = df.dropna(subset=['price'])

# Tìm giá cao nhất của mỗi hãng xe
max_price_per_company = df.groupby('company')['price'].max()

# Xuất kết quả
print(max_price_per_company)
