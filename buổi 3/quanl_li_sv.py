danh_sach_sv = [(8.5, "An"), (7.0, "Binh"), (9.2, "Chi"), (6.5, "Dung")]

# Them sinh vien moi
danh_sach_sv.append((8.0, "Em"))

# Xoa mot sinh vien
danh_sach_sv.remove((7.0, "Binh"))

# Sua diem sinh vien o vi tri 0
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])

# Kiem tra sinh vien co trong danh sach
print("Chi co trong danh sach khong?", (9.2, "Chi") in danh_sach_sv)

# Sap xep tang dan
danh_sach_sv.sort()
print("\nDanh sach sau khi sap xep theo diem tang dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")

# Sap xep giam dan
danh_sach_sv.sort(reverse=True)
print("\nDanh sach sau khi sap xep theo diem giam dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")