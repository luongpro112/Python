def tinh_toan(a, phep_tinh, b):
    if phep_tinh == "+":
        return a + b
    elif phep_tinh == "-":
        return a - b
    elif phep_tinh == "*":
        return a * b
    elif phep_tinh == "/":
        if b == 0:
            return "Loi: khong the chia cho 0"
        return a / b
    else:
        return "Phep tinh khong hop le"

def main():
    print("===== MAY TINH BO TUI (console) =====")
    while True:
        bieu_thuc = input("Nhập biểu thức (vd: 5 + 3), hoặc 'thoat' để dừng: ").strip()
        if bieu_thuc.lower() == "thoat":
            print("Tạm biệt!")
            break
        try:
            # Tách chuỗi theo khoảng trắng
            a_str, phep_tinh, b_str = bieu_thuc.split()
            ket_qua = tinh_toan(float(a_str), phep_tinh, float(b_str))
            print("Kết quả:", ket_qua)
        except ValueError:
            print("Định dạng không hợp lệ. Ví dụ đúng: 5 + 3")

if __name__ == "__main__":
    main()