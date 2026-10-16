
import tkinter as tk
from tkinter import messagebox
import ast
import operator

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("320x400")

bien_bieu_thuc = tk.StringVar()

tk.Entry(
    cua_so, textvariable=bien_bieu_thuc,
    font=("Arial", 18), justify="right"
).grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=8)


def tinh_bieu_thuc(node):
    phep_toan = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv
    }

    if isinstance(node, ast.Expression):
        return tinh_bieu_thuc(node.body)

    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value

    if isinstance(node, ast.UnaryOp):
        if isinstance(node.op, ast.UAdd):
            return tinh_bieu_thuc(node.operand)
        if isinstance(node.op, ast.USub):
            return -tinh_bieu_thuc(node.operand)

    if isinstance(node, ast.BinOp) and type(node.op) in phep_toan:
        trai = tinh_bieu_thuc(node.left)
        phai = tinh_bieu_thuc(node.right)
        return phep_toan[type(node.op)](trai, phai)

    raise ValueError("Bieu thuc khong hop le")


def bam_nut(ky_tu):
    hien_tai = bien_bieu_thuc.get()

    if ky_tu == "C":
        bien_bieu_thuc.set("")
    elif ky_tu == "=":
        try:
            cay = ast.parse(hien_tai, mode="eval")
            ket_qua = tinh_bieu_thuc(cay)

            if isinstance(ket_qua, float) and ket_qua.is_integer():
                ket_qua = int(ket_qua)

            bien_bieu_thuc.set(str(ket_qua))
        except ZeroDivisionError:
            messagebox.showerror("Loi", "Khong the chia cho 0.")
        except (ValueError, SyntaxError, TypeError, OverflowError):
            messagebox.showerror("Loi", "Bieu thuc khong hop le.")
    else:
        bien_bieu_thuc.set(hien_tai + ky_tu)


cac_nut = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", ".", "+"],
    ["=", "", "", ""]
]

for hang, dong in enumerate(cac_nut, start=1):
    for cot, ky_tu in enumerate(dong):
        if ky_tu == "":
            continue

        tk.Button(
            cua_so, text=ky_tu, width=5, height=2,
            font=("Arial", 12),
            command=lambda k=ky_tu: bam_nut(k)
        ).grid(row=hang, column=cot, padx=3, pady=3)

cua_so.mainloop()
