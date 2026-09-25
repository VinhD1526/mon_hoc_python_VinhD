# CHƯƠNG TRÌNH CHÍNH
# MODULE HÓA
# Import module utils
import utils

# SỬ DỤNG CÁC HÀM TRONG utils.py

print("========== MINI PROJECT MODULE HOA ==========")

# Đảo ngược chuỗi
print(
    utils.dao_nguoc_chuoi("Python")
)

# Kiểm tra Palindrome
print(
    utils.kiem_tra_palindrome("madam")
)

# Chuẩn hóa họ tên
print(
    utils.chuan_hoa_ho_ten(
        " nguyen van an "
    )
)

# Tính USCLN
print(
    utils.uscln(24, 36)
)


# Kiểm tra số nguyên tố
print(
    utils.kiem_tra_nguyen_to(29)
)

''' Đặt utils.py và main.py cùng thư mục giúp import utils hoạt động đơn giản và đúng với yêu cầu của bài thực hành '''