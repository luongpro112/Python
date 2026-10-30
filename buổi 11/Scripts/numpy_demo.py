import numpy as np


diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_array = np.array(diem_list)

print(type(diem_list), type(diem_array))

# Phép toán vector hóa
diem_cong_them = diem_array + 0.5
print("Mảng sau khi cộng 0.5:", diem_cong_them)

# So sánh với list thường
diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print("List sau khi cộng 0.5:", diem_cong_them_list)

# Các hàm thống kê
print("Trung bình:", np.mean(diem_array))
print("Lớn nhất:", np.max(diem_array))
print("Nhỏ nhất:", np.min(diem_array))
print("Độ lệch chuẩn:", round(np.std(diem_array), 2))

# Ma trận
ma_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("Ma trận:\n", ma_tran)
print("Kích thước:", ma_tran.shape)
print("Ma trận nhân 2:\n", ma_tran * 2)