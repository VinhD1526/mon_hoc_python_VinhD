import tkinter as tk
from tkinter import ttk, messagebox

cua_so = tk.Tk()
cua_so.title("Hoat dong 3 - Listbox va Combobox")
cua_so.geometry("350x400")

# Hoat dong 3.1: Listbox
tk.Label(
    cua_so, text="HOAT DONG 3.1 - LISTBOX",
    font=("Arial", 11, "bold")
).pack(pady=8)

listbox_mon_hoc = tk.Listbox(
    cua_so, selectmode="single", height=5
)

for mon in ["Toan", "Ly", "Hoa", "Van", "Anh"]:
    listbox_mon_hoc.insert(tk.END, mon)

listbox_mon_hoc.pack(pady=5)


def xem_mon_da_chon():
    lua_chon = listbox_mon_hoc.curselection()

    if lua_chon:
        mon = listbox_mon_hoc.get(lua_chon[0])
        messagebox.showinfo("Ket qua", f"Mon da chon: {mon}")
    else:
        messagebox.showerror("Loi", "Vui long chon mon hoc.")


tk.Button(
    cua_so, text="Xem mon da chon",
    command=xem_mon_da_chon
).pack(pady=5)

# Hoat dong 3.2: Combobox
tk.Label(
    cua_so, text="HOAT DONG 3.2 - COMBOBOX",
    font=("Arial", 11, "bold")
).pack(pady=10)

combobox_thanh_pho = ttk.Combobox(
    cua_so,
    values=["Ha Noi", "Da Nang", "TP.HCM", "Hue"],
    state="readonly"
)

combobox_thanh_pho.current(0)
combobox_thanh_pho.pack(pady=5)


def xem_thanh_pho():
    messagebox.showinfo(
        "Ket qua",
        f"Ban chon: {combobox_thanh_pho.get()}"
    )


tk.Button(
    cua_so, text="Xac nhan thanh pho",
    command=xem_thanh_pho
).pack(pady=10)

cua_so.mainloop()
