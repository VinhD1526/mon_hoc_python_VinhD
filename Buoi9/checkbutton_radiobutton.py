import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Hoat dong 1 va 2")
cua_so.geometry("350x360")

# Hoat dong 1: Checkbutton
bien_doc_sach = tk.BooleanVar()
bien_the_thao = tk.BooleanVar()
bien_am_nhac = tk.BooleanVar()

tk.Label(
    cua_so, text="HOAT DONG 1 - CHECKBUTTON",
    font=("Arial", 12, "bold")
).pack(pady=8)

tk.Checkbutton(
    cua_so, text="Doc sach", variable=bien_doc_sach
).pack(anchor="w", padx=35)

tk.Checkbutton(
    cua_so, text="The thao", variable=bien_the_thao
).pack(anchor="w", padx=35)

tk.Checkbutton(
    cua_so, text="Am nhac", variable=bien_am_nhac
).pack(anchor="w", padx=35)


def xem_so_thich():
    print("Doc sach:", bien_doc_sach.get())
    print("The thao:", bien_the_thao.get())
    print("Am nhac:", bien_am_nhac.get())


tk.Button(
    cua_so, text="Xem lua chon",
    command=xem_so_thich
).pack(pady=8)

# Hoat dong 2: Radiobutton
bien_loai_tai_khoan = tk.StringVar(value="ca_nhan")

tk.Label(
    cua_so, text="HOAT DONG 2 - RADIOBUTTON",
    font=("Arial", 12, "bold")
).pack(pady=8)

tk.Radiobutton(
    cua_so, text="Ca nhan",
    variable=bien_loai_tai_khoan,
    value="ca_nhan"
).pack(anchor="w", padx=35)

tk.Radiobutton(
    cua_so, text="Doanh nghiep",
    variable=bien_loai_tai_khoan,
    value="doanh_nghiep"
).pack(anchor="w", padx=35)


def xem_tai_khoan():
    nhan_ket_qua.config(
        text="Loai tai khoan: " + bien_loai_tai_khoan.get()
    )


tk.Button(
    cua_so, text="Xac nhan tai khoan",
    command=xem_tai_khoan
).pack(pady=5)

nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()

cua_so.mainloop()
