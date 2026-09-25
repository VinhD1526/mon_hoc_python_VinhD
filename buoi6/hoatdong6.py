# BUỔI 6 - HOẠT ĐỘNG 6
# ĐỆ QUY

# HOẠT ĐỘNG 6.1 - GIAI THỪA BẰNG ĐỆ QUY

def giai_thua_de_quy(n):

    # Điều kiện dừng
    if n <= 1:
        return 1

    # Hàm tự gọi lại chính nó
    return n * giai_thua_de_quy(n - 1)

# GIAI THỪA BẰNG VÒNG LẶP

def giai_thua_lap(n):

    ket_qua = 1

    for i in range(1, n + 1):
        ket_qua *= i

    return ket_qua


print("========== HOẠT ĐỘNG 6.1 ==========")

print(
    giai_thua_de_quy(5),
    "-",
    giai_thua_lap(5)
)

''' Cả hai đều tính được giai thừa, nhưng bài này dùng đệ quy để minh họa cách một hàm tự gọi chính nó '''

# HOẠT ĐỘNG 6.2 - FIBONACCI ĐỆ QUY

def fibonacci_de_quy(n):

    # Điều kiện dừng
    if n <= 1:
        return n

    return (
        fibonacci_de_quy(n - 1)
        + fibonacci_de_quy(n - 2)
    )


print("\n========== HOẠT ĐỘNG 6.2 ==========")

for i in range(10):
    print(
        fibonacci_de_quy(i),
        end=" "
    )

print()

# Thử Fibonacci(30)
print(
    "Fibonacci(30) =",
    fibonacci_de_quy(30)
) 

''' Fibonacci đệ quy chậm hơn vì số lần gọi hàm tăng rất nhanh và nhiều giá trị bị tính lại nhiều lần
Đây chính là lý do Fibonacci đệ quy đơn giản trong bài học phù hợp để minh họa đệ quy, nhưng không phải cách tối ưu để tính Fibonacci lớn '''