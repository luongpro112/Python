import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, 
    QListWidget, QVBoxLayout, QHBoxLayout, QMessageBox
)

class UngDungToDo(QWidget):
    def __init__(self):
        super().__init__()
        # List lưu công việc dưới dạng tuple: (nội dung, đã_hoàn_thành)
        self.danh_sach_cong_viec = [] 
        self.khoi_tao_giao_dien()
        
    def khoi_tao_giao_dien(self):
        self.setWindowTitle("Ung dung Ghi chu cong viec - PyQt")
        self.resize(420, 420)
        
        # 1. Tiêu đề
        tieu_de = QLabel("TO-DO LIST (PyQt)")
        tieu_de.setStyleSheet("font-size: 18px; font-weight: bold;")
        
        # 2. Khu vực nhập liệu và nút Thêm
        self.o_nhap_cong_viec = QLineEdit()
        self.o_nhap_cong_viec.setPlaceholderText("Nhap cong viec moi...")
        nut_them = QPushButton("Them")
        
        layout_nhap = QHBoxLayout()
        layout_nhap.addWidget(self.o_nhap_cong_viec)
        layout_nhap.addWidget(nut_them)
        
        # 3. Danh sách hiển thị công việc
        self.danh_sach_hien_thi = QListWidget()
        
        # 4. Các nút thao tác
        nut_xoa = QPushButton("Xoa")
        nut_hoan_thanh = QPushButton("Danh dau hoan thanh")
        
        layout_nut = QHBoxLayout()
        layout_nut.addWidget(nut_xoa)
        layout_nut.addWidget(nut_hoan_thanh)
        
        # 5. Layout tổng thể
        layout_chinh = QVBoxLayout()
        layout_chinh.addWidget(tieu_de)
        layout_chinh.addLayout(layout_nhap)
        layout_chinh.addWidget(self.danh_sach_hien_thi)
        layout_chinh.addLayout(layout_nut)
        
        self.setLayout(layout_chinh)
        
        # 6. Kết nối Signal - Slot
        nut_them.clicked.connect(self.them_cong_viec)
        nut_xoa.clicked.connect(self.xoa_cong_viec)
        nut_hoan_thanh.clicked.connect(self.danh_dau_hoan_thanh)
        
    def lam_moi_danh_sach(self):
        """Cập nhật lại giao diện QListWidget từ list dữ liệu"""
        self.danh_sach_hien_thi.clear()
        for noi_dung, da_hoan_thanh in self.danh_sach_cong_viec:
            if da_hoan_thanh:
                self.danh_sach_hien_thi.addItem(f"[x] {noi_dung}")
            else:
                self.danh_sach_hien_thi.addItem(f"[ ] {noi_dung}")
                
    def them_cong_viec(self):
        noi_dung = self.o_nhap_cong_viec.text().strip()
        if noi_dung == "":
            QMessageBox.warning(self, "Canh bao", "Vui long nhap noi dung cong viec.")
            return
        # Thêm vào list dữ liệu với trạng thái False (chưa hoàn thành)
        self.danh_sach_cong_viec.append((noi_dung, False))
        self.o_nhap_cong_viec.clear()
        self.lam_moi_danh_sach()
        
    def xoa_cong_viec(self):
        # Lấy vị trí dòng đang được chọn
        vi_tri = self.danh_sach_hien_thi.currentRow()
        if vi_tri < 0:
            QMessageBox.critical(self, "Loi", "Vui long chon mot cong viec trong danh sach de xoa.")
            return
        self.danh_sach_cong_viec.pop(vi_tri)
        self.lam_moi_danh_sach()
        
    def danh_dau_hoan_thanh(self):
        vi_tri = self.danh_sach_hien_thi.currentRow()
        if vi_tri < 0:
            QMessageBox.critical(self, "Loi", "Vui long chon mot cong viec de danh dau hoan thanh.")
            return
        
        # Cập nhật lại tuple tại vị trí đó thành True
        noi_dung, _ = self.danh_sach_cong_viec[vi_tri]
        self.danh_sach_cong_viec[vi_tri] = (noi_dung, True)
        self.lam_moi_danh_sach()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = UngDungToDo()
    cua_so.show()
    sys.exit(app.exec_())