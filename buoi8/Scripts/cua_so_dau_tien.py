import tkinter as tk

# Khoi tao cua so
cua_so = tk.Tk()
cua_so.title("Cua so Tkinter dau tien & Vi du Frame")
cua_so.geometry("400x300")

# Cho phep thay doi chieu rong, khong cho thay doi chieu cao
cua_so.resizable(True, False)

# Hoat dong 2: Tạo Frame to chuc giao dien
khung_tren = tk.Frame(cua_so, bg="lightblue", height=100)
khung_tren.pack(fill="x")

khung_duoi = tk.Frame(cua_so, bg="lightyellow")
khung_duoi.pack(fill="both", expand=True)

# Them Label vao cac Frame
tk.Label(khung_tren, text="Khu vuc tieu de", bg="lightblue", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(khung_duoi, text="Khu vuc noi dung", bg="lightyellow", font=("Arial", 12)).pack(pady=10)

cua_so.mainloop()