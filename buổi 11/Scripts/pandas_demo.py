import pandas as pd

# 2.1 Đọc CSV
df = pd.read_csv("diem_sinh_vien.csv")
print("--- 5 dòng đầu ---")
print(df.head())
print("Số dòng, số cột:", df.shape)
print("Danh sách cột:", df.columns.tolist())

# 2.2 Thống kê môn học
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
print("\n--- Điểm trung bình môn ---")
print(diem_trung_binh_mon)

print("\nĐiểm trung bình toàn bộ:", df["diem"].mean())
print("Điểm cao nhất:", df["diem"].max())
print("Điểm thấp nhất:", df["diem"].min())

# 2.3 Tính ĐTB từng sinh viên & lọc
diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)
print("\n--- Điểm TB từng sinh viên ---")
print(diem_tb_sv)

sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\nSinh viên đạt:")
print(sinh_vien_dat)
print("\nSinh viên không đạt:")
print(sinh_vien_khong_dat)