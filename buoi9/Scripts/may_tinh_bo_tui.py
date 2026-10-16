import tkinter as tk
from tkinter import messagebox

def bam_nut(ky_tu):
    hien_tai = bien_bieu_thuc.get()
    bien_bieu_thuc.set(hien_tai + str(ky_tu))

def xoa_man_hinh():
    bien_bieu_thuc.set("")

def tinh_ket_qua():
    try:
        ket_qua = eval(bien_bieu_thuc.get())
        bien_bieu_thuc.set(str(ket_qua))
    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le!")
        bien_bieu_thuc.set("")

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("300x420")
cua_so.resizable(False, False)

bien_bieu_thuc = tk.StringVar()

entry_man_hinh = tk.Entry(cua_so, textvariable=bien_bieu_thuc, font=("Arial", 18), justify="right", bd=5)
entry_man_hinh.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="we")

danh_sach_nut = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 3)
]

for (text, row, col) in danh_sach_nut:
    tk.Button(cua_so, text=text, font=("Arial", 14), width=4, height=2,
              command=lambda t=text: bam_nut(t)).grid(row=row, column=col, padx=5, pady=5)

tk.Button(cua_so, text="C", font=("Arial", 14), width=4, height=2, bg="#ff7675", fg="white",
          command=xoa_man_hinh).grid(row=4, column=2, padx=5, pady=5)

tk.Button(cua_so, text="=", font=("Arial", 14), width=22, height=2, bg="#0984e3", fg="white",
          command=tinh_ket_qua).grid(row=5, column=0, columnspan=4, padx=5, pady=10)

cua_so.mainloop()