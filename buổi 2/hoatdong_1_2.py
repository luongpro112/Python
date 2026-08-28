#Hoạt động 1:
#bài 1.1
print("BAI TAP 1.1")
ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))

# GIẢI THÍCH 1.1:
# - input() luôn trả về chuỗi (str).
# - ho_ten là chữ nên giữ nguyên str.
# - nam_sinh và diem_tb cần tính toán/so sánh nên phải ép sang int và float.

#Bài 1.2:
print("\n BAI TAP 1.2")
print("In voi sep='-':")
print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")

print("In voi sep=', ':")
print("Python", "la", "ngon", "ngu", "lap trinh", sep=", ")

print("In voi sep='\\n':")
print("Python", "la", "ngon", "ngu", "lap trinh", sep="\n")

print("In voi end=' | ':")
print("Dong 1", end=" | ")
print("Dong 2")

# GIẢI THÍCH 1.2:
# - sep quy định ký tự phân cách giữa các đối số in ra.
# - end quy định ký tự kết thúc (mặc định là xuống dòng \n).

#Bài 1.3: 
print("\n BAI TAP 1.3")

print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")

print(
    "Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(ho_ten, nam_sinh, diem_tb)
)

print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" % (ho_ten, nam_sinh, diem_tb))

# THẢO LUẬN 1.3:
# f-string được khuyến khích nhất vì cú pháp ngắn gọn, dễ đọc, tốc độ xử lý
# nhanh nhất và cho phép chèn thẳng các biểu thức tính toán vào bên trong {}.

#Hoạt động 2:
#Bài 2.1: 
# Chú thích một dòng: Khai báo thông tin sinh viên
"""
Chú thích nhiều dòng (Docstring):
Chương trình thực hành Buổi 2 - Nhập xuất & Chuỗi
Sinh viên thực hiện: Nguyễn Văn A
"""
ten_sv = "Tran Thi B"  

#Bài 2.2:
print("\nBAI TAP 2.2")
s1 = "Xin chao"
s2 = "Ban co khoe khong?"
s3 = """Day la
mot chuoi
nhieu dong"""
s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = 'Toi ten la "Nam", con ban ten gi?'

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

# GIẢI THÍCH 2.2:
# - s4 dùng \\ để thoát ký tự (escape) dấu \ tránh bị nhầm với \n, \t...
# - s5 dùng raw string (tiền tố r) giúp giữ nguyên mọi ký tự thô mà không cần \\.
# - Raw string dùng khi làm việc với đường dẫn file Windows hoặc Regex.