# Hoạt dộng 1:
# bài 1.1:
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
print(diem_so[0]) # phan tu dau tien
print(diem_so[-1]) # phan tu cuoi cung
print(diem_so[1:4]) # cat tu vi tri 1 den truoc 4
print(diem_so[::2]) # lay cach 1 phan tu (step = 2)
print(diem_so[::-1]) # dao nguoc danh sach
#bài 1.2:
ten_sv = ["An", "Binh", "Chi"]
ten_sv.append("Dung") # them vao cuoi
ten_sv.insert(1, "Em") # chen vao vi tri 1
print(ten_sv)
ten_sv.remove("Chi") # xoa theo gia tri
pop_ra = ten_sv.pop() # xoa va lay ra phan tu cuoi
print(ten_sv, "- da xoa:", pop_ra)
ten_sv.sort() # sap xep tang dan (theo bang chu cai)
print(ten_sv)
ten_sv.reverse() # dao nguoc thu tu hien tai
print(ten_sv)
ten_sv.extend(["Giang", "Hoa"]) # noi them mot list khac vao
print(ten_sv)
# remove(x): Xóa phần tử đầu tiên tìm thấy trong list có giá trị bằng x. Phương thức này không trả về giá trị.
# pop(i): Xóa phần tử ở vị trí chỉ số i (mặc định xóa vị trí cuối -1) và trả về giá trị vừa bị xóa để có thể lưu vào biến khác.

# Hoạt động 2:
# bài 2.1:
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5] 
tong = 0 
for diem in diem_so: 
 print(diem) 
 tong = tong + diem 
print("Tong diem:", tong) 
print("Diem trung binh:", round(tong / len(diem_so), 2))

# bài 2.2:
ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

tong_ma_tran = 0
for hang in ma_tran:
    for phan_tu in hang:
        tong_ma_tran += phan_tu

print("Tong tat ca cac phan tu trong ma tran:", tong_ma_tran)

# Hoạt động 3:
# bài 3.1: 
day_so = list(range(1, 21)) # day so tu 1 den 20 
so_chan = [x for x in day_so if x % 2 == 0] 
so_le = [x for x in day_so if x % 2 != 0] 
print("So chan:", so_chan) 
print("So le:", so_le)
# bài 3.2:
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5] 
diem_cong = [round(diem + 0.5, 2) for diem in diem_so] 
print(diem_cong)
