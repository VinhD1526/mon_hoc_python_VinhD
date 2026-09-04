# Danh sách dạng (điểm, tên)
danh_sach_sv = [
    (8.5, "An"),
    (7.0, "Binh"),
    (9.2, "Chi"),
    (6.5, "Dung")
]

# Thêm sinh viên mới
danh_sach_sv.append((8.0, "Em"))

# Xóa sinh viên biết chính xác điểm và tên
danh_sach_sv.remove((7.0, "Binh"))

# Sửa điểm sinh viên ở vị trí 0
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])

# Kiểm tra sinh viên có trong danh sách
print("Chi có trong danh sách không?", (9.2, "Chi") in danh_sach_sv)

# Sắp xếp điểm tăng dần
danh_sach_sv.sort()
print("\nDanh sách theo điểm tăng dần:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")

# Sắp xếp điểm giảm dần
danh_sach_sv.sort(reverse=True)
print("\nDanh sách theo điểm giảm dần:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")