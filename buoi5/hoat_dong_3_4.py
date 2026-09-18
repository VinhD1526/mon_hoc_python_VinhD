# HOẠT ĐỘNG 3: VÒNG LẶP FOR
# For với range()
print("For voi range():")
for i in range(1, 6):
    print(i)

# For duyệt list
print("\nFor duyet list:")
diem_so = [8.5, 7.0, 9.2, 6.5]

for diem in diem_so:
    print("Diem:", diem)

# For duyệt tuple
print("\nFor duyet tuple:")
toa_do = (3, 5)

for gia_tri in toa_do:
    print(gia_tri)


# For duyệt dictionary
print("\nFor duyet dictionary:")
diem_mon = {
    "Toan": 8.0,
    "Ly": 7.5
}
for mon, diem in diem_mon.items():
    print(mon, "-", diem)

print("\nFor duyet string:")
ten = "Python"
for ky_tu in ten:
    print(ky_tu)

# BÀI TẬP VẬN DỤNG - BẢNG CỬU CHƯƠNG

print("\nBang cuu chuong 5:")

n = 5

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# HOẠT ĐỘNG 4: VÒNG LẶP WHILE

# Bài tập 4.1 - Tính giai thừa
print("\nTinh giai thua:")

n = 5
giai_thua = 1
i = 1

while i <= n:
    giai_thua = giai_thua * i
    i += 1

print(f"{n}! = {giai_thua}")


# Bài tập 4.2 - Tổng các chữ số
print("\nTinh tong cac chu so:")

so = 4527
so_tam = so
tong_chu_so = 0

while so_tam > 0:
    chu_so = so_tam % 10
    tong_chu_so += chu_so
    so_tam = so_tam // 10

print(f"Tong cac chu so cua {so} la: {tong_chu_so}")