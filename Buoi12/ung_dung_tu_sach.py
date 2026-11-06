"""Giao diện Tkinter cho ứng dụng quản lý tủ sách cá nhân."""

import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

import matplotlib

matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import csdl_sach as db


DANH_SACH_THE_LOAI = [
    "Kỹ năng sống",
    "Tiểu thuyết",
    "Lịch sử",
    "Khoa học",
    "Kinh tế",
    "Khác",
]


class UngDungTuSach(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Quản lý tủ sách cá nhân")
        self.geometry("900x570")
        self.minsize(760, 500)

        self._tao_giao_dien()
        self._tai_lai_danh_sach_sach()

    def _tao_giao_dien(self) -> None:
        khung_chinh = ttk.Frame(self, padding=16)
        khung_chinh.pack(fill="both", expand=True)
        khung_chinh.columnconfigure(0, weight=1)
        khung_chinh.rowconfigure(2, weight=1)

        ttk.Label(
            khung_chinh,
            text="TỦ SÁCH CÁ NHÂN",
            font=("Segoe UI", 18, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 12))

        khung_nhap = ttk.LabelFrame(khung_chinh, text="Thông tin sách", padding=12)
        khung_nhap.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        khung_nhap.columnconfigure(1, weight=1)
        khung_nhap.columnconfigure(3, weight=1)

        ttk.Label(khung_nhap, text="Tên sách:").grid(
            row=0, column=0, sticky="w", padx=(0, 8), pady=5
        )
        self.o_nhap_ten_sach = ttk.Entry(khung_nhap)
        self.o_nhap_ten_sach.grid(row=0, column=1, sticky="ew", padx=(0, 16), pady=5)

        ttk.Label(khung_nhap, text="Tác giả:").grid(
            row=0, column=2, sticky="w", padx=(0, 8), pady=5
        )
        self.o_nhap_tac_gia = ttk.Entry(khung_nhap)
        self.o_nhap_tac_gia.grid(row=0, column=3, sticky="ew", pady=5)

        ttk.Label(khung_nhap, text="Thể loại:").grid(
            row=1, column=0, sticky="w", padx=(0, 8), pady=5
        )
        self.chon_the_loai = ttk.Combobox(
            khung_nhap,
            values=DANH_SACH_THE_LOAI,
            state="readonly",
        )
        self.chon_the_loai.current(0)
        self.chon_the_loai.grid(row=1, column=1, sticky="ew", padx=(0, 16), pady=5)

        ttk.Button(
            khung_nhap,
            text="Thêm sách",
            command=self._xu_ly_them_sach,
        ).grid(row=1, column=3, sticky="e", pady=5)

        khung_danh_sach = ttk.LabelFrame(
            khung_chinh, text="Danh sách sách", padding=8
        )
        khung_danh_sach.grid(row=2, column=0, sticky="nsew", pady=(0, 12))
        khung_danh_sach.columnconfigure(0, weight=1)
        khung_danh_sach.rowconfigure(0, weight=1)

        cot = ("ten_sach", "tac_gia", "the_loai", "trang_thai")
        self.bang_sach = ttk.Treeview(
            khung_danh_sach,
            columns=cot,
            show="headings",
            selectmode="browse",
        )
        self.bang_sach.heading("ten_sach", text="Tên sách")
        self.bang_sach.heading("tac_gia", text="Tác giả")
        self.bang_sach.heading("the_loai", text="Thể loại")
        self.bang_sach.heading("trang_thai", text="Trạng thái")
        self.bang_sach.column("ten_sach", width=270, minwidth=150)
        self.bang_sach.column("tac_gia", width=210, minwidth=120)
        self.bang_sach.column("the_loai", width=170, minwidth=110)
        self.bang_sach.column("trang_thai", width=130, minwidth=100, anchor="center")
        self.bang_sach.grid(row=0, column=0, sticky="nsew")

        thanh_cuon = ttk.Scrollbar(
            khung_danh_sach, orient="vertical", command=self.bang_sach.yview
        )
        thanh_cuon.grid(row=0, column=1, sticky="ns")
        self.bang_sach.configure(yscrollcommand=thanh_cuon.set)

        khung_thao_tac = ttk.Frame(khung_chinh)
        khung_thao_tac.grid(row=3, column=0, sticky="ew")
        ttk.Button(
            khung_thao_tac,
            text="Đánh dấu đã đọc",
            command=self._xu_ly_danh_dau_da_doc,
        ).pack(side="left", padx=(0, 8))
        ttk.Button(
            khung_thao_tac,
            text="Xóa sách",
            command=self._xu_ly_xoa_sach,
        ).pack(side="left", padx=8)
        ttk.Button(
            khung_thao_tac,
            text="Thống kê theo thể loại",
            command=self._xu_ly_thong_ke,
        ).pack(side="left", padx=8)
        ttk.Button(
            khung_thao_tac,
            text="Làm mới",
            command=self._tai_lai_danh_sach_sach,
        ).pack(side="right")

    def _tai_lai_danh_sach_sach(self) -> None:
        try:
            danh_sach_sach = db.lay_toan_bo_sach()
        except sqlite3.Error as loi:
            messagebox.showerror(
                "Lỗi cơ sở dữ liệu",
                f"Không thể tải danh sách sách.\nChi tiết: {loi}",
                parent=self,
            )
            return

        for ma_sach in self.bang_sach.get_children():
            self.bang_sach.delete(ma_sach)

        for id_sach, ten_sach, tac_gia, the_loai, da_doc in danh_sach_sach:
            trang_thai = "Đã đọc" if da_doc else "Chưa đọc"
            self.bang_sach.insert(
                "",
                "end",
                iid=str(id_sach),
                values=(ten_sach, tac_gia, the_loai, trang_thai),
            )

    def _lay_id_sach_dang_chon(self) -> int | None:
        lua_chon = self.bang_sach.selection()
        if not lua_chon:
            messagebox.showwarning(
                "Chưa chọn sách",
                "Vui lòng chọn một cuốn sách trong danh sách.",
                parent=self,
            )
            return None
        return int(lua_chon[0])

    def _xu_ly_them_sach(self) -> None:
        ten_sach = self.o_nhap_ten_sach.get().strip()
        tac_gia = self.o_nhap_tac_gia.get().strip()
        the_loai = self.chon_the_loai.get()

        if not ten_sach or not tac_gia:
            messagebox.showerror(
                "Thiếu thông tin",
                "Vui lòng nhập đầy đủ tên sách và tác giả.",
                parent=self,
            )
            return

        try:
            db.them_sach(ten_sach, tac_gia, the_loai)
        except sqlite3.Error as loi:
            messagebox.showerror(
                "Lỗi cơ sở dữ liệu",
                f"Không thể thêm sách.\nChi tiết: {loi}",
                parent=self,
            )
            return

        self.o_nhap_ten_sach.delete(0, tk.END)
        self.o_nhap_tac_gia.delete(0, tk.END)
        self._tai_lai_danh_sach_sach()

    def _xu_ly_danh_dau_da_doc(self) -> None:
        id_sach = self._lay_id_sach_dang_chon()
        if id_sach is None:
            return

        try:
            da_cap_nhat = db.danh_dau_da_doc(id_sach)
        except sqlite3.Error as loi:
            messagebox.showerror(
                "Lỗi cơ sở dữ liệu",
                f"Không thể cập nhật trạng thái sách.\nChi tiết: {loi}",
                parent=self,
            )
            return

        if not da_cap_nhat:
            messagebox.showinfo(
                "Thông tin",
                "Cuốn sách này đã được đánh dấu là đã đọc.",
                parent=self,
            )
        self._tai_lai_danh_sach_sach()

    def _xu_ly_xoa_sach(self) -> None:
        id_sach = self._lay_id_sach_dang_chon()
        if id_sach is None:
            return
        if not messagebox.askyesno(
            "Xác nhận xóa",
            "Bạn có chắc muốn xóa cuốn sách đã chọn khỏi tủ sách?",
            parent=self,
        ):
            return

        try:
            da_xoa = db.xoa_sach(id_sach)
        except sqlite3.Error as loi:
            messagebox.showerror(
                "Lỗi cơ sở dữ liệu",
                f"Không thể xóa sách.\nChi tiết: {loi}",
                parent=self,
            )
            return

        if not da_xoa:
            messagebox.showinfo(
                "Thông tin",
                "Cuốn sách không còn trong cơ sở dữ liệu.",
                parent=self,
            )
        self._tai_lai_danh_sach_sach()

    def _xu_ly_thong_ke(self) -> None:
        try:
            du_lieu = db.thong_ke_theo_the_loai()
        except sqlite3.Error as loi:
            messagebox.showerror(
                "Lỗi cơ sở dữ liệu",
                f"Không thể thống kê sách.\nChi tiết: {loi}",
                parent=self,
            )
            return

        if not du_lieu:
            messagebox.showinfo(
                "Chưa có dữ liệu",
                "Hãy thêm sách trước khi xem thống kê.",
                parent=self,
            )
            return

        cua_so_bieu_do = tk.Toplevel(self)
        cua_so_bieu_do.title("Số lượng sách theo thể loại")
        cua_so_bieu_do.geometry("760x480")
        cua_so_bieu_do.minsize(560, 360)
        cua_so_bieu_do.transient(self)

        hinh = Figure(figsize=(8, 5), dpi=100)
        truc = hinh.add_subplot(111)
        the_loai = [dong[0] for dong in du_lieu]
        so_luong = [dong[1] for dong in du_lieu]
        cot = truc.bar(the_loai, so_luong, color="#4f86c6")
        truc.bar_label(cot, padding=3)
        truc.set_title("Số lượng sách theo thể loại")
        truc.set_xlabel("Thể loại")
        truc.set_ylabel("Số lượng sách")
        truc.tick_params(axis="x", labelrotation=20)
        hinh.tight_layout()

        canvas = FigureCanvasTkAgg(hinh, master=cua_so_bieu_do)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        cua_so_bieu_do.protocol(
            "WM_DELETE_WINDOW",
            lambda: self._dong_cua_so_bieu_do(cua_so_bieu_do, hinh),
        )

    @staticmethod
    def _dong_cua_so_bieu_do(cua_so: tk.Toplevel, hinh: Figure) -> None:
        hinh.clear()
        cua_so.destroy()


def main() -> None:
    db.tao_bang_neu_chua_co()
    ung_dung = UngDungTuSach()
    ung_dung.mainloop()


if __name__ == "__main__":
    main()
