import matplotlib.pyplot as plt

# Dữ liệu số lượng bán theo tháng
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
soap_sales = [9000, 6500, 9500, 8900, 8500, 8000, 9200, 10000, 8700, 11000, 13000, 14500]
facewash_sales = [5500, 6200, 5800, 4300, 4700, 5100, 5300, 5700, 5400, 5200, 3000, 2500]

# Tạo figure và các subplot
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Biểu đồ xà bông tắm (màu xanh)
axs[0].plot(months, soap_sales, marker='o', color='green', linestyle='-')
axs[0].set_title("Số lượng xà bông tắm đã bán", color='green')
axs[0].grid(True)

# Biểu đồ sữa rửa mặt (màu đỏ)
axs[1].plot(months, facewash_sales, marker='o', color='red', linestyle='-')
axs[1].set_title("Số lượng sữa rửa mặt đã bán", color='red')
axs[1].set_xlabel("Tháng")
axs[1].set_ylabel("Số lượng")
axs[1].grid(True)

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()
