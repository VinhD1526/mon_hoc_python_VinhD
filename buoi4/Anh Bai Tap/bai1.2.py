sinh_vien = {
"ho_ten": "Nguyen Van A",
"nam_sinh": 2004,
"diem_tb": 8.5
}
sinh_vien["lop"] = "CNTT01" # them khoa moi
sinh_vien["diem_tb"] = 9.0 # sua gia tri khoa da co
print(sinh_vien)
diem_cu = sinh_vien.pop("diem_tb") # xoa theo khoa, tra ve gia tri vua xoa

print(sinh_vien, "- diem da xoa:", diem_cu)
sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"}) # cap nhat/them nhieu khoa cung luc   
print(sinh_vien)