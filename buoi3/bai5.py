import math

cac_diem = [(0, 0), (3, 4), (6, 8)]

for diem in cac_diem:
    x, y = diem
    khoang_cach = math.sqrt(x ** 2 + y ** 2)
    print(f"Khoảng cách từ {diem} đến gốc (0, 0) là: {khoang_cach}")