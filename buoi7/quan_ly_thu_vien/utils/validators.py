def nhap_so_nguyen(loi_nhac):
    """Bắt lỗi try-except đảm bảo người dùng nhập đúng số nguyên dương."""
    while True:
        try:
            gia_tri = int(input(loi_nhac))
            if gia_tri > 0:
                return gia_tri
            print("-> So nhap vao phai lon hon 0. Vui long nhap lai!")
        except ValueError:
            print("-> Dinh dang khong hop le! Vui long nhap mot so nguyen.")