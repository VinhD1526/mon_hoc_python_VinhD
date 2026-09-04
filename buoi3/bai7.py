# Danh sách dạng: (tên sản phẩm, giá, số lượng)
kho_hang = [
    ("Ban phim", 250000, 10),
    ("Chuot", 150000, 20),
    ("Man hinh", 2500000, 5),
]

# Thêm sản phẩm mới
kho_hang.append(("Tai nghe", 300000, 15))

# Xóa sản phẩm
kho_hang.remove(("Chuot", 150000, 20))

# Hiển thị danh sách kho hàng
print("DANH SACH KHO HANG:")
for ten, gia, so_luong in kho_hang:
    print(f"{ten:<12} - Gia: {gia:>10,} VND - SL: {so_luong}")

# Tính tổng giá trị kho bằng vòng lặp cộng dồn
tong_gia_tri = 0

for ten, gia, so_luong in kho_hang:
    tong_gia_tri = tong_gia_tri + gia * so_luong

print(f"\nTong gia tri kho hang: {tong_gia_tri:,} VND")