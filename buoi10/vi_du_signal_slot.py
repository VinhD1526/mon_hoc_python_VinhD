import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

class ViDuSignalSlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vi du Signal - Slot")
        self.resize(300, 180)
        
        self.o_nhap = QLineEdit()
        nut_hien_thi = QPushButton("Hien thi noi dung")
        self.nhan_ket_qua = QLabel("Chua co noi dung")
        
        layout = QVBoxLayout()
        layout.addWidget(self.o_nhap)
        layout.addWidget(nut_hien_thi)
        layout.addWidget(self.nhan_ket_qua)
        self.setLayout(layout)
        
        # Ket noi 1 signal toi 2 slot (Yêu cầu bài 3.2)
        nut_hien_thi.clicked.connect(self.hien_thi_noi_dung)
        nut_hien_thi.clicked.connect(lambda: print("Nut vua duoc bam!"))

    def hien_thi_noi_dung(self):
        noi_dung = self.o_nhap.text()
        self.nhan_ket_qua.setText(f"Ban vua nhap: {noi_dung}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = ViDuSignalSlot()
    cua_so.show()
    sys.exit(app.exec_())

    ''' Signal - Slot là gì? Đây là cơ chế giao tiếp cốt lõi trong PyQt.

Signal (Tín hiệu): Là sự kiện xảy ra (ví dụ: người dùng click chuột, nhập chữ, kéo cửa sổ...). Trong bài, clicked là signal của nút bấm.

Slot (Khe cắm/Hàm xử lý): Là hàm sẽ được tự động gọi khi signal phát ra. Trong bài, hien_thi_noi_dung là slot. Một signal có thể kết nối tới nhiều slot, và ngược lại.

'''