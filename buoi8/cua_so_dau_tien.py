import tkinter as tk

# tạo cửa sổ chính
cua_so = tk.Tk()
cua_so.title("Ung dung demo - Cua so & Frame")
cua_so.geometry("400x300")

# Hoat dong 1.2: Thu nghiem resizable
# Doi thanh (True, False) de kiem tra keo rong/cao theo yêu cầu
cua_so.resizable(False, False)

# Hoat dong 2: To chuc giao dien bang Frame
khung_tren = tk.Frame(cua_so, bg="lightblue", height=100)
khung_tren.pack(fill="x")

khung_duoi = tk.Frame(cua_so, bg="lightyellow")
khung_duoi.pack(fill="both", expand=True)

# Them Widget vao cac Frame
nhan_tren = tk.Label(khung_tren, text="Xin chao Tkinter! (Khu vuc tieu de)", bg="lightblue", font=("Arial", 12, "bold"))
nhan_tren.pack(pady=15)

nhan_duoi = tk.Label(khung_duoi, text="Khu vuc noi dung chinh", bg="lightyellow", font=("Arial", 11))
nhan_duoi.pack(pady=20)

cua_so.mainloop()