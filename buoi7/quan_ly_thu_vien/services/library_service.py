    from buoi7.quan_ly_thu_vien.data.database import danh_sach_sach, lich_su_doanh_thu

def tim_sach_theo_ma(ma_sach):
    for sach in danh_sach_sach:
        if sach["ma_sach"] == ma_sach:
            return sach
    return None

def hien_thi_danh_sach_sach():
    print("\n" + "=" * 80)
    print(f"{'Ma sach':<10}{'Ten sach':<30}{'Tac gia':<18}{'Gia/ngay':<12}{'Trang thai':<12}")
    print("-" * 80)
    for sach in danh_sach_sach:
        print(f"{sach['ma_sach']:<10}{sach['ten_sach']:<30}{sach['tac_gia']:<18}"
              f"{sach['gia_thue']:>8,} {sach['trang_thai']:<12}")
    print("=" * 80)

def xem_sach_san_sang():
    sach_san_sang = [s for s in danh_sach_sach if s["trang_thai"] == "San sang"]
    if not sach_san_sang:
        print("-> Hien tai tat ca sach deu da duoc muon.")
        return
    print("\nDANH SÁCH SÁCH ĐANG SẮN SÀNG CHO MƯỢN:")
    for s in sach_san_sang:
        print(f" - [{s['ma_sach']}] {s['ten_sach']} - Tac gia: {s['tac_gia']} ({s['gia_thue']:,} VND/ngay)")

def them_sach_moi(ma_sach, ten_sach, tac_gia, gia_thue):
    if tim_sach_theo_ma(ma_sach) is not None:
        print(f"-> Ma sach {ma_sach} da ton tai! Khong the them.")
        return
    danh_sach_sach.append({
        "ma_sach": ma_sach, "ten_sach": ten_sach,
        "tac_gia": tac_gia, "gia_thue": gia_thue,
        "trang_thai": "San sang", "nguoi_muon": ""
    })
    print(f"-> Da them sach '{ten_sach}' ({ma_sach}) vao thu vien thanh cong.")

def muon_sach(ma_sach, nguoi_muon):
    sach = tim_sach_theo_ma(ma_sach)
    if sach is None:
        print(f"-> Khong tim thay sach co ma {ma_sach}.")
        return
    if sach["trang_thai"] == "Da muon":
        print(f"-> Sach '{sach['ten_sach']}' hien dang duoc muon boi {sach['nguoi_muon']}.")
        return
    sach["trang_thai"] = "Da muon"
    sach["nguoi_muon"] = nguoi_muon
    print(f"-> Cho muon sach '{sach['ten_sach']}' cho doc gia [{nguoi_muon}] thanh cong.")

def tra_sach(ma_sach, so_ngay_muon):
    sach = tim_sach_theo_ma(ma_sach)
    if sach is None:
        print(f"-> Khong tim thay sach co ma {ma_sach}.")
        return
    if sach["trang_thai"] == "San sang":
        print(f"-> Sach {ma_sach} dang o trong kho, khong co ai muon!")
        return
    
    thanh_tien = sach["gia_thue"] * so_ngay_muon
    lich_su_doanh_thu.append({
        "ma_sach": ma_sach,
        "ten_sach": sach["ten_sach"],
        "nguoi_muon": sach["nguoi_muon"],
        "so_ngay": so_ngay_muon,
        "thanh_tien": thanh_tien
    })
    print(f"-> Doc gia [{sach['nguoi_muon']}] da tra sach '{sach['ten_sach']}' sau {so_ngay_muon} ngay.")
    print(f"-> Tong tien thue sach: {thanh_tien:,} VND")
    
    sach["trang_thai"] = "San sang"
    sach["nguoi_muon"] = ""

def thong_ke_doanh_thu():
    if not lich_su_doanh_thu:
        print("-> Chua co giao dich muon/tra sach nao duoc ghi nhan.")
        return
    tong = 0
    print("\nLỊCH SỬ GIAO DỊCH VÀ DOANH THU:")
    print("-" * 75)
    for gd in lich_su_doanh_thu:
        print(f" + [{gd['ma_sach']}] {gd['ten_sach']} | Doc gia: {gd['nguoi_muon']} | {gd['so_ngay']} ngay -> {gd['thanh_tien']:,} VND")
        tong += gd["thanh_tien"]
    print("-" * 75)
    print(f">>> TỔNG DOANH THU CHO THUÊ SÁCH: {tong:,} VND")
    ''' limeted '''
    