import math
# HOẠT ĐỘNG 3: NUMBER - INT, FLOAT, COMPLEX & BUILT-IN

#Bài 3.1:
print("BAI TAP 3.1")
so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j

print("Kieu du lieu:", type(so_nguyen), type(so_thuc), type(so_phuc))
print("Ep int -> float:", float(so_nguyen))
print("Ep float -> int:", int(so_thuc))

#Bài 3.2:
print("\nBAI TAP 3.2")
a = -7
b = 2.6789
c, d = 17, 5

print("abs(-7):", abs(a))
print("round(2.6789):", round(b))
print("round(2.6789, 2):", round(b, 2))
print("pow(17, 2):", pow(c, 2))
print("divmod(17, 5):", divmod(c, d))

# SO SÁNH pow(c, 2) VÀ c ** 2:
# - Cả 2 đều cho kết quả 289.
# - c ** 2 thực thi nhanh hơn một chút ở mức bytecode.
# - pow(x, y, z) có thêm tham số z để tính chia lấy dư (x^y % z) cực kỳ tối ưu.

#Bài 3.3:
print("\nBAI TAP 3.3")
a_pt, b_pt, c_pt = 1, -3, 2
delta = b_pt**2 - 4 * a_pt * c_pt

x1 = (-b_pt + math.sqrt(delta)) / (2 * a_pt)
x2 = (-b_pt - math.sqrt(delta)) / (2 * a_pt)

print(f"Phuong trinh: {a_pt}x^2 + ({b_pt})x + {c_pt} = 0")
print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")

# HOẠT ĐỘNG 4: STRING - INDEXING, SLICING & PHƯƠNG THỨC

#Bài 4.1:
print("\nBAI TAP 4.1")
cau = "Lap trinh Python rat thu vi"
print("Ky tu dau:", cau[0])
print("Ky tu cuoi:", cau[-1])
print("Cắt [4:10]:", cau[4:10])
print("Cắt [:8]:", cau[:8])
print("Cắt [11:]:", cau[11:])

chuoi_dao = cau[::-1]
print("Chuoi dao nguoc:", chuoi_dao)

# Kiểm tra Palindrome
is_palindrome = cau == cau[::-1]
print("Co phai Palindrome khong?:", is_palindrome)


#Bài 4.2:
print("\nBAI TAP 4.2")
ten = "Nam"
# ten[0] = "T" -> Lỗi TypeError do String trong Python không thể sửa trực tiếp.
ten_moi = "T" + ten[1:]
print("Sua 'Nam' thanh:", ten_moi)

#Bài 4.3:
print("\nBAI TAP 4.3")
cau_xl = " Toi dang HOC Python rat vui "

print("strip():", f"'{cau_xl.strip()}'")
print("upper():", cau_xl.strip().upper())
print("lower():", cau_xl.strip().lower())
print("replace():", cau_xl.strip().replace("HOC", "hoc"))
print("split():", cau_xl.strip().split())
print("So tu trong cau:", len(cau_xl.strip().split()))
print("Dem 'o':", cau_xl.count("o"))
print("Tim vị trí 'Python':", cau_xl.find("Python"))
print("startswith('Toi'):", cau_xl.strip().startswith("Toi"))
print("endswith('vui'):", cau_xl.strip().endswith("vui"))
print("join():", "-".join(["Python", "that", "thu", "vi"]))


#Bài tập 4.4
print("\nBAI TAP 4.4")
ho_ten_tho = " nguyen van an "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print(f"Ten tho: '{ho_ten_tho}'")
print(f"Ten da chuan hoa: '{ho_ten_sach}'")