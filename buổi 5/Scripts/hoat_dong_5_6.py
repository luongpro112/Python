#5.1
diem = 6.5
if diem >= 8.0:
    pass # chua cai dat logic cho truong hop nay, se bo sung sau
elif diem >= 5.0:
    print("Dat yeu cau")
else:
    pass

#5.2
so = 29
la_so_nguyen_to = True
if so < 2:
    la_so_nguyen_to = False
else:
    for i in range(2, so):
        if so % i == 0:
            la_so_nguyen_to = False
            break # thoat ngay khi tim thay uoc so, khong can kiem tra tiep
print(f"{so} co phai so nguyen to khong? {la_so_nguyen_to}")

#5.3
n = 20
so_hien_tai = n + 1
while True:
    la_so_nguyen_to = True
    for i in range(2, so_hien_tai):
        if so_hien_tai % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        break
    so_hien_tai += 1
print(f"So nguyen to dau tien lon hon {n} la: {so_hien_tai}")

#5.4
danh_sach = [5, -3, 8, 0, -1, 12, 7, -9]
danh_sach_hop_le = []
for so in danh_sach:
    if so <= 0:
        continue # bo qua cac so khong duong, khong them vao danh sach ket qua
    danh_sach_hop_le.append(so)
print("Cac so hop le (duong):", danh_sach_hop_le)

#6.1
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

#6.2
n = 4
# Nua tren cua hinh thoi
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Nua duoi cua hinh thoi
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))