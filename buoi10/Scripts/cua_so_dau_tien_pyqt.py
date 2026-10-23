import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class CuaSoDauTien(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cua so PyQt dau tien")
        self.resize(300, 200)
        
        layout = QVBoxLayout()
        nhan = QLabel("Xin chao PyQt!")
        layout.addWidget(nhan)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = CuaSoDauTien()
    cua_so.show()
    sys.exit(app.exec_())