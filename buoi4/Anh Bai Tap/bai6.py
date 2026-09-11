doan_van = "python la ngon ngu lap trinh python de hoc python de dung"
danh_sach_tu = doan_van.split()
tan_suat = {}
for tu in danh_sach_tu:
    tan_suat[tu] = tan_suat.get(tu, 0) + 1
print("Tan suat xuat hien cac tu:")
for tu, so_lan in tan_suat.items():
    print(f"{tu}: {so_lan}")
'''“Lấy số lần xuất hiện của từ tu; nếu từ chưa tồn tại thì coi như nó xuất hiện 0 lần.”

Sau đó + 1 để tăng số lần xuất hiện lên 1.

 Vì vậy, chỉ một dòng này đã thay thế được việc phải dùng if/else kiểm tra từ đã xuất hiện hay chưa.'''