# BUỔI 6 - HOẠT ĐỘNG 1, 2, 3
# HÀM (FUNCTION)
# HOẠT ĐỘNG 1.1 - HÀM CƠ BẢN
def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def bscnn(a, b):
    return a * b // uscln(a, b)

def kiem_tra_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n
print("========== HOẠT ĐỘNG 1.1 ==========")
# USCLN - 3 bộ dữ liệu
print("USCLN:")
print(uscln(24, 36))
print(uscln(15, 25))
print(uscln(48, 18))
# BSCNN - 3 bộ dữ liệu
print("\nBSCNN:")
print(bscnn(4, 6))
print(bscnn(8, 12))
print(bscnn(15, 20))
# Kiểm tra số nguyên tố - 3 bộ dữ liệu
print("\nKiểm tra số nguyên tố:")
print(kiem_tra_nguyen_to(29))
print(kiem_tra_nguyen_to(17))
print(kiem_tra_nguyen_to(20))
# Kiểm tra số hoàn thiện - 3 bộ dữ liệu
print("\nKiểm tra số hoàn thiện:")
print(kiem_tra_so_hoan_thien(28))
print(kiem_tra_so_hoan_thien(6))
print(kiem_tra_so_hoan_thien(12))

# HOẠT ĐỘNG 1.2 - RETURN

def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return


def chia_lay_thuong_du(a, b):
    return a // b, a % b


print("\n========== HOẠT ĐỘNG 1.2 ==========")

in_loi_chao("An")

thuong, du = chia_lay_thuong_du(17, 5)

print(f"Thuong: {thuong}, du: {du}")

# HOẠT ĐỘNG 2 - THAM SỐ MẶC ĐỊNH

# VÀ THAM SỐ TỪ KHÓA

def gioi_thieu(ten, tuoi=18, lop="Chua ro"):
    print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")


print("\n========== HOẠT ĐỘNG 2 ==========")

# Dùng toàn bộ giá trị mặc định
gioi_thieu("An")

# Ghi đè tuổi
gioi_thieu("Binh", 20)

# Dùng tham số từ khóa
gioi_thieu("Chi", lop="CNTT01")

# Tham số từ khóa có thể đảo thứ tự
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19)

''' Khi sử dụng tham số từ khóa, Python xác định giá trị dựa vào tên của tham số, không dựa vào vị trí của tham số '''

# HOẠT ĐỘNG 3.1 - *args

def tinh_tong(*args):
    tong = 0

    for so in args:
        tong += so

    return tong


print("\n========== HOẠT ĐỘNG 3.1 ==========")

print(tinh_tong(1, 2, 3))
print(tinh_tong(5, 10, 15, 20, 25))
print(tinh_tong())

# HOẠT ĐỘNG 3.2 - **kwargs

def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Ho ten: {ho_ten} - Tuoi: {tuoi}")

    for khoa, gia_tri in kwargs.items():
        print(f" {khoa}: {gia_tri}")


print("\n========== HOẠT ĐỘNG 3.2 ==========")

in_thong_tin(
    "Nguyen Van A",
    20,
    lop="CNTT01",
    que_quan="Ha Noi"
)

in_thong_tin(
    "Tran Thi B",
    21,
    email="b@example.com"
)