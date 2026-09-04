# Hoạt động 4:
# bài 4.1:
toa_do = (3, 5) 
print(toa_do, type(toa_do)) 
# Thu gan lai: toa_do[0] = 10 -> quan sat loi TypeError (tuple bat bien)

# bài 4.2:
x, y = toa_do 
print("x =", x, "- y =", y) 
# Doi gia tri 2 bien bang unpacking (khong can bien tam) 
a, b = 10, 20 
a, b = b, a 
print("a =", a, "- b =", b)

# bài 4.3:
c, d = 17, 5 
thuong_du = divmod(c, d) # divmod tra ve mot tuple (thuong, du) 
thuong, du = thuong_du # unpacking ket qua 
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")

# Hoạt động 5:
# bài 5.1:
import math 
diem_a = (2, 3) 
diem_b = (7, 8) 
xa, ya = diem_a 
xb, yb = diem_b
khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2) 
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

import math

cac_diem = [(0, 0), (3, 4), (6, 8)]

for diem in cac_diem:
    x, y = diem  # Unpacking tuple
    # Khoang cach toi goc to a do (0,0) bang sqrt(x^2 + y^2)
    khoang_cach = math.sqrt(x**2 + y**2)
    print(f"Khoang cach tu diem {diem} den goc toa do (0, 0) la: {round(khoang_cach, 2)}")