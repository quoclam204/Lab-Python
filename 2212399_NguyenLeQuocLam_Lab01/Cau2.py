import math

def dien_tich_hcn_tu_ban_kinh(r, k):
    """
    Tính diện tích hình chữ nhật nội tiếp đường tròn bán kính r,
    với tỷ lệ chiều dài : chiều rộng là k.
    
    Tham số:
    - r: bán kính đường tròn
    - k: tỷ lệ giữa chiều dài và chiều rộng (a = k * b)

    Trả về:
    - Diện tích hình chữ nhật
    """
    if r <= 0:
        raise ValueError("Bán kính phải lớn hơn 0.")
    if k <= 0:
        raise ValueError("Tỷ lệ k phải lớn hơn 0.")
    
    # Tính chiều rộng (b)
    b = (2 * r) / math.sqrt(k**2 + 1)
    # Tính chiều dài (a)
    a = k * b
    # Tính diện tích
    S = a * b
    return S

# Ví dụ sử dụng
r = 5  # Bán kính
k = 2  # Tỷ lệ chiều dài / chiều rộng
print("Diện tích hình chữ nhật:", dien_tich_hcn_tu_ban_kinh(r, k))