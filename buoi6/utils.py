# MODULE UTILS
# CÁC HÀM XỬ LÝ CHUỖI VÀ SỐ

# Đảo ngược chuỗi
def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]


# Kiểm tra chuỗi Palindrome
def kiem_tra_palindrome(chuoi):
    return chuoi == chuoi[::-1]


# Chuẩn hóa họ tên
def chuan_hoa_ho_ten(chuoi):
    return " ".join(chuoi.split()).title()


# Tìm USCLN
def uscln(a, b):
    while b != 0:
        a, b = b, a % b

    return a
    
# Kiểm tra số nguyên tố
def kiem_tra_nguyen_to(n):

    if n < 2:
        return False

    for i in range(2, n):

        if n % i == 0:
            return False

    return True