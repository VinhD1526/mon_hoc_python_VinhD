from buoi7.quan_ly_thu_vien.utils.validators import nhap_so_nguyen
from buoi7.quan_ly_thu_vien.services.library_service import (
    hien_thi_danh_sach_sach,
    xem_sach_san_sang,
    them_sach_moi,
    muon_sach,
    tra_sach,
    thong_ke_doanh_thu
)

def hien_thi_menu():
    print("\n================ QUẢN LÝ THƯ VIỆN SÁCH ================")
    print("1. Hien thi danh sach tat ca sach")
    print("2. Xem danh sach sach dang san sang")
    print("3. Them dau sach moi")
    print("4. Cho muon sach")
    print("5. Tra sach & Thanh toan")
    print("6. Thong ke doanh thu cho thue")
    print("0. Thoat chuong trinh")

def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban (0-6): ").strip()
        
        if lua_chon == "1":
            hien_thi_danh_sach_sach()
        elif lua_chon == "2":
            xem_sach_san_sang()
        elif lua_chon == "3":
            ma_sach = input("Nhap ma sach moi: ").strip().upper()
            ten_sach = input("Nhap ten sach: ").strip().title()
            tac_gia = input("Nhap ten tac gia: ").strip().title()
            gia_thue = nhap_so_nguyen("Nhap gia thue (VND/ngay): ")
            them_sach_moi(ma_sach, ten_sach, tac_gia, gia_thue)
        elif lua_chon == "4":
            ma_sach = input("Nhap ma sach muon muon: ").strip().upper()
            nguoi_muon = input("Nhap ten doc gia: ").strip().title()
            muon_sach(ma_sach, nguoi_muon)
        elif lua_chon == "5":
            ma_sach = input("Nhap ma sach can tra: ").strip().upper()
            so_ngay = nhap_so_nguyen("Nhap so ngay da muon: ")
            tra_sach(ma_sach, so_ngay)
        elif lua_chon == "6":
            thong_ke_doanh_thu()
        elif lua_chon == "0":
            print("Cam on ban da su dung phan mem Quan ly Thu vien! Tam biet.")
            break
        else:
            print("-> Lua chon khong hop le! Vui long chon tu 0 den 6.")

if __name__ == "__main__":
    chay_chuong_trinh()