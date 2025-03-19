import pandas as pd
import matplotlib.pyplot as plt

# Đọc file CSV
df = pd.read_csv("E:\\Python\\sales_data.csv")  

# Kiểm tra thông tin dữ liệu
print(df.info())

# Chuyển dữ liệu thành danh sách
profitList = df['total_profit'].tolist()
monthList = df['month_number'].tolist()

# Vẽ biểu đồ đường thẳng
plt.figure("Biểu đồ đoạn thẳng")
plt.plot(monthList, profitList, marker='o', linestyle='-', color='b', label="Tổng lợi nhuận")

# Thiết lập nhãn trục
plt.xlabel('Tháng')
plt.ylabel('Lợi nhuận ($)')
plt.xticks(monthList)
plt.yticks([10000, 20000, 30000, 40000, 50000])

# Thêm tiêu đề và chú thích
plt.title('Lợi nhuận hàng tháng năm 2021')
plt.legend()

# Hiển thị biểu đồ
plt.show()
