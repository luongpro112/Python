# HOẠT ĐỘNG 5:
print("CHƯƠNG TRÌNH ĐĂNG KÝ THÔNG TIN CÁ NHÂN")

ho_ten = input("Nhap ho ten: ")
sdt = input("Nhap so dien thoai: ")
email = input("Nhap email: ")

ho_ten_chuan = " ".join(ho_ten.split()).title()
sdt_hop_le = len(sdt) == 10
email_hop_le = "@" in email

print("\n--- KET QUA KIEM TRA THONG TIN ---")
print(f"Ho ten (da chuan hoa)          : {ho_ten_chuan}")
print(f"So dien thoai hop le (du 10 ky tu)?: {sdt_hop_le}")
print(f"Email hop le (co ky tu @)?        : {email_hop_le}")