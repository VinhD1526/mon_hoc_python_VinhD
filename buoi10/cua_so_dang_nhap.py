import sys
import os  # Thêm thư viện os để xử lý đường dẫn
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()
        
        # Tự động lấy đường dẫn thư mục chứa file code này
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Ghép với tên file .ui
        ui_path = os.path.join(current_dir, "form_dang_nhap.ui")
        
        # Nạp giao diện bằng đường dẫn tuyệt đối vừa tạo
        uic.loadUi(ui_path, self) 
        
        # Kết nối signal - slot
        self.nut_dang_nhap.clicked.connect(self.xu_ly_dang_nhap)

    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan.text()
        mat_khau = self.o_nhap_mat_khau.text()
        
        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(self, "Lỗi", "Vui lòng nhập đầy đủ tài khoản và mật khẩu.")
            return
        QMessageBox.information(self, "Thành công", f"Xin chào {tai_khoan}, đăng nhập thành công!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = CuaSoDangNhap()
    cua_so.show()
    sys.exit(app.exec_())