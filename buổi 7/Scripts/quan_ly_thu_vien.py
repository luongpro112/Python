# =============================================================
# ĐỒ ÁN NHỎ: QUẢN LÝ THƯ VIỆN MƯỢN/TRẢ SÁCH
# Môn: Lập trình Python cơ bản - Buổi 7
# =============================================================

# ---------- Bước 4.1: Khai báo dữ liệu ban đầu ----------
danh_sach_sach = [
    {"ma_sach": "S001", "ten_sach": "Lap Trinh Python", "tac_gia": "Nguyen Van A", "nam_xb": 2020, "trang_thai": "Co san", "nguoi_muon": ""},
    {"ma_sach": "S002", "ten_sach": "Cau Truc Du Lieu", "tac_gia": "Tran Thi B", "nam_xb": 2019, "trang_thai": "Co san", "nguoi_muon": ""},
    {"ma_sach": "S003", "ten_sach": "Tri Tue Nhan Tao", "tac_gia": "Le Van C", "nam_xb": 2021, "trang_thai": "Co san", "nguoi_muon": ""},
    {"ma_sach": "S004", "ten_sach": "Co So Du Lieu", "tac_gia": "Pham Van D", "nam_xb": 2018, "trang_thai": "Co san", "nguoi_muon": ""},
]

lich_su_giao_dich = []   # lưu các lượt mượn/trả để thống kê


# ---------- Bước 4.2: Hàm hiển thị & tìm kiếm ----------
def hien_thi_danh_sach_sach():
    """Hiển thị toàn bộ sách trong thư viện."""
    print("\n" + "=" * 78)
    print(f"{'Ma sach':<10}{'Ten sach':<22}{'Tac gia':<18}{'Nam':<6}" f"{'Trang thai':<12}{'Nguoi muon':<15}")
    print("-" * 78)
    for s in danh_sach_sach:
        print(f"{s['ma_sach']:<10}{s['ten_sach']:<22}{s['tac_gia']:<18}" f"{s['nam_xb']:<6}{s['trang_thai']:<12}{s['nguoi_muon']:<15}")
    print("=" * 78)


def tim_sach_theo_ma(ma_sach):
    """Tìm sách theo mã, trả về dict hoặc None."""
    for s in danh_sach_sach:
        if s["ma_sach"] == ma_sach:
            return s
    return None


def xem_sach_co_san():
    """Liệt kê các sách chưa được mượn."""
    sach_co_san = [s for s in danh_sach_sach if s["trang_thai"] == "Co san"]
    if len(sach_co_san) == 0:
        print("-> Hien khong con sach nao co san.")
        return
    print("\nCAC SACH DANG CO SAN:")
    for s in sach_co_san:
        print(f"  {s['ma_sach']} - {s['ten_sach']} - {s['tac_gia']} ({s['nam_xb']})")


# ---------- Bước 4.3: Hàm thêm / mượn / trả sách ----------
def them_sach(ma_sach, ten_sach, tac_gia, nam_xb):
    """Thêm sách mới vào thư viện."""
    if tim_sach_theo_ma(ma_sach) is not None:
        print(f"-> Ma sach {ma_sach} da ton tai, khong the them.")
        return
    danh_sach_sach.append({
        "ma_sach": ma_sach, "ten_sach": ten_sach, "tac_gia": tac_gia,
        "nam_xb": nam_xb, "trang_thai": "Co san", "nguoi_muon": ""
    })
    print(f"-> Da them sach {ma_sach} thanh cong.")


def muon_sach(ma_sach, ten_nguoi_muon):
    """Đặt sách cho người mượn: Co san -> Da muon."""
    s = tim_sach_theo_ma(ma_sach)
    if s is None:
        print(f"-> Khong tim thay sach {ma_sach}.")
        return
    if s["trang_thai"] == "Da muon":
        print(f"-> Sach {ma_sach} da co nguoi muon, khong the muon.")
        return
    s["trang_thai"] = "Da muon"
    s["nguoi_muon"] = ten_nguoi_muon
    lich_su_giao_dich.append({
        "ma_sach": ma_sach, "ten_sach": s["ten_sach"],
        "nguoi_muon": ten_nguoi_muon, "hanh_dong": "Muon",
        "phi_phat": 0
    })
    print(f"-> Muon sach {ma_sach} cho {ten_nguoi_muon} thanh cong.")


def tra_sach(ma_sach, so_ngay_tre):
    """
    Trả sách: Da muon -> Co san.
    Nếu trả trễ (so_ngay_tre > 0) thì phạt 5.000 VND/ngày.
    """
    s = tim_sach_theo_ma(ma_sach)
    if s is None:
        print(f"-> Khong tim thay sach {ma_sach}.")
        return
    if s["trang_thai"] == "Co san":
        print(f"-> Sach {ma_sach} dang co san, khong co ai muon.")
        return

    phi_phat = so_ngay_tre * 5000 if so_ngay_tre > 0 else 0
    nguoi_muon = s["nguoi_muon"]

    lich_su_giao_dich.append({
        "ma_sach": ma_sach, "ten_sach": s["ten_sach"],
        "nguoi_muon": nguoi_muon, "hanh_dong": "Tra",
        "phi_phat": phi_phat
    })

    print(f"-> {nguoi_muon} da tra sach {ma_sach}.")
    if phi_phat > 0:
        print(f"-> Tra tre {so_ngay_tre} ngay. Phi phat: {phi_phat:,} VND")
    else:
        print("-> Tra dung han, khong co phi phat.")

    s["trang_thai"] = "Co san"
    s["nguoi_muon"] = ""


# ---------- Bước 4.4: Hàm thống kê & nhập số nguyên an toàn ----------
def thong_ke_doanh_thu():
    """Thống kê số lượt mượn, số lượt trả và tổng phí phạt."""
    if len(lich_su_giao_dich) == 0:
        print("-> Chua co giao dich muon/tra nao.")
        return

    tong_muon = 0
    tong_tra = 0
    tong_phi_phat = 0

    print("\nLICH SU GIAO DICH:")
    print("-" * 70)
    for gd in lich_su_giao_dich:
        if gd["hanh_dong"] == "Muon":
            tong_muon += 1
            print(f"  [MUON] {gd['ma_sach']} - {gd['ten_sach']} - {gd['nguoi_muon']}")
        else:
            tong_tra += 1
            print(f"  [TRA ] {gd['ma_sach']} - {gd['ten_sach']} - {gd['nguoi_muon']}" f" - Phi phat: {gd['phi_phat']:,} VND")
            tong_phi_phat += gd["phi_phat"]
    print("-" * 70)
    print(f">>> Tong so luot muon : {tong_muon}")
    print(f">>> Tong so luot tra  : {tong_tra}")
    print(f">>> TONG PHI PHAT THU: {tong_phi_phat:,} VND")


def nhap_so_nguyen(loi_nhac):
    """Nhập số nguyên an toàn, lặp đến khi đúng."""
    while True:
        try:
            return int(input(loi_nhac))
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")


# ---------- Bước 4.5: Menu chính & vòng lặp chương trình ----------
def hien_thi_menu():
    print("\n===== QUAN LY THU VIEN MUON/TRA SACH =====")
    print("1. Hien thi danh sach tat ca sach")
    print("2. Xem cac sach dang co san")
    print("3. Them sach moi")
    print("4. Muon sach")
    print("5. Tra sach")
    print("6. Thong ke doanh thu / phi phat")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach_sach()

        elif lua_chon == "2":
            xem_sach_co_san()

        elif lua_chon == "3":
            ma_sach   = input("Nhap ma sach moi: ").strip().upper()
            ten_sach  = input("Nhap ten sach: ").strip().title()
            tac_gia   = input("Nhap tac gia: ").strip().title()
            nam_xb    = nhap_so_nguyen("Nhap nam xuat ban: ")
            them_sach(ma_sach, ten_sach, tac_gia, nam_xb)

        elif lua_chon == "4":
            ma_sach       = input("Nhap ma sach can muon: ").strip().upper()
            ten_nguoi_muon = input("Nhap ten nguoi muon: ").strip().title()
            muon_sach(ma_sach, ten_nguoi_muon)

        elif lua_chon == "5":
            ma_sach      = input("Nhap ma sach can tra: ").strip().upper()
            so_ngay_tre  = nhap_so_nguyen("Nhap so ngay tra tre (0 neu dung han): ")
            tra_sach(ma_sach, so_ngay_tre)

        elif lua_chon == "6":
            thong_ke_doanh_thu()

        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break

        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


# ---------- Điểm khởi chạy ----------
if __name__ == "__main__":
    chay_chuong_trinh()