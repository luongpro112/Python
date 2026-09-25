#1.1
def uscln(a,b):
    while b != 0:
        a, b = b, a % b
        return a

def bscnn(a,b):
    return a * b // uscln(a,b)

def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

print(uscln(24, 36))
print(bscnn(4, 6))
print(kiem_tra_so_nguyen_to(29))
print(kiem_tra_so_hoan_thien(28))

#1.2
def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return

def chia_lay_thuong_du(a, b):
    return a // b, a % b

in_loi_chao("Nguyen Van A")
thuong, du = chia_lay_thuong_du(10, 3)
print(f"Thuong: {thuong}, Du: {du}")

#2
def gioi_thieu(ten, tuoi= 20, lop="chua ro"):
    print(f"Ten: {ten}, Tuoi: {tuoi}, Lop: {lop}")
    gioi_thieu("Nguyen Van A")
    gioi_thieu("Binh", 20)
    gioi_thieu("Chi", lop="CNTT")
    gioi_thieu("Dung", lop="CNTT02", tuoi=19)

#3.1
def tinh_tong(*args):
    tong=0
    for so in args:
        tong += so
    return tong

print(tinh_tong(1, 2, 3))
print(tinh_tong(5, 10, 15, 20, 25))
print(tinh_tong())

#3.2
def in_thong_tin(ho_ten, tuoi, *kwargs):
    print(f"Ho ten: {ho_ten}, Tuoi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f"{khoa}: {gia_tri}")

in_thong_tin("Nguyen Van A", 20, lop="CNTT", que_quan="Ha Noi")
in_thong_tin("Tran Thi B", 21, email="b@example.com")
